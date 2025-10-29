<?php
// lookup.php - Z-Wave Device Lookup using local devices.json
header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    exit;
}

$manufacturerId = $_GET['manufacturerId'] ?? '';
$productType = $_GET['productType'] ?? '';
$productId = $_GET['productId'] ?? '';

if (empty($manufacturerId) || empty($productType) || empty($productId)) {
    echo json_encode(['success' => false, 'error' => 'Missing parameters']);
    exit;
}

// Clean and normalize hex values
$cleanMfrId = str_pad(strtolower(str_replace('0x', '', $manufacturerId)), 4, '0', STR_PAD_LEFT);
$cleanProdType = str_pad(strtolower(str_replace('0x', '', $productType)), 4, '0', STR_PAD_LEFT);
$cleanProdId = str_pad(strtolower(str_replace('0x', '', $productId)), 4, '0', STR_PAD_LEFT);

// Load devices.json
$devicesFile = __DIR__ . '/devices.json';
if (!file_exists($devicesFile)) {
    echo json_encode(['success' => false, 'error' => 'Device database not found']);
    exit;
}

$database = json_decode(file_get_contents($devicesFile), true);
if (!$database || !isset($database['devices'])) {
    echo json_encode(['success' => false, 'error' => 'Invalid database']);
    exit;
}

// Search for matching device
foreach ($database['devices'] as $device) {
    $dbMfrId = str_pad(strtolower(str_replace('0x', '', $device['manufacturerId'] ?? '')), 4, '0', STR_PAD_LEFT);
    
    if ($dbMfrId !== $cleanMfrId) continue;
    
    foreach ($device['devices'] as $variant) {
        $dbProdType = str_pad(strtolower(str_replace('0x', '', $variant['productType'] ?? '')), 4, '0', STR_PAD_LEFT);
        $dbProdId = str_pad(strtolower(str_replace('0x', '', $variant['productId'] ?? '')), 4, '0', STR_PAD_LEFT);
        
        if ($dbProdType === $cleanProdType && $dbProdId === $cleanProdId) {
            echo json_encode([
                'success' => true,
                'manufacturer' => $device['manufacturer'] ?? 'Unknown',
                'label' => $device['label'] ?? '',
                'description' => $device['description'] ?? '',
                'productType' => "0x" . $cleanProdType,
                'productId' => "0x" . $cleanProdId
            ]);
            exit;
        }
    }
}

// Not found
echo json_encode([
    'success' => false,
    'message' => 'Device not found',
    'searchUrls' => [
        'zwaveJs' => "https://devices.zwave-js.io/?jumpTo=0x{$cleanMfrId}:0x{$cleanProdType}:0x{$cleanProdId}"
    ]
]);