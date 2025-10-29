#!/usr/bin/env python3
"""
Z-Wave Device Database Extraction Script
=========================================

Extracts device information from Z-Wave JS configuration files and creates
a consolidated JSON database for the Z-Wave SmartStart QR Decoder tool.

Usage:
    python3 extract_devices.py [devices_folder] [output_file]
    
    devices_folder: Path to Z-Wave JS device configs (default: packages/config/config/devices)
    output_file: Output JSON filename (default: zwave_devices_db.json)

Examples:
    # Use defaults
    python3 extract_devices.py
    
    # Custom paths
    python3 extract_devices.py /path/to/devices/ my_output.json

Requirements:
    - Python 3.6+
    - Z-Wave JS repository cloned locally

Output Format:
    {
      "metadata": { "total_devices": 3821, "source": "..." },
      "devices": [
        {
          "manufacturer": "AEON Labs",
          "manufacturerId": "0x0086",
          "label": "ZW096",
          "description": "Smart Switch 6",
          "devices": [
            { "productType": "0x0003", "productId": "0x0060" }
          ]
        }
      ]
    }

Created with Claude.ai for the Z-Wave QR Decoder project
"""

import json
import re
from pathlib import Path

def extract_first_block(file_path):
    """
    Extract device information block from a Z-Wave JS config file.
    
    This function parses Z-Wave JS device configuration files (which may contain
    comments and complex nested structures) and extracts only the essential
    device identification information needed for QR code lookups.
    
    Args:
        file_path: Path to a Z-Wave JS device config JSON file
        
    Returns:
        Dictionary with device info, or None if parsing fails
        
    Extracted Fields:
        - manufacturer: Company name (e.g., "AEON Labs")
        - manufacturerId: Hex ID (e.g., "0x0086")
        - label: Device model (e.g., "ZW096")
        - description: Device description (e.g., "Smart Switch 6")
        - devices: Array of {productType, productId} combinations
        - _sourceFile: Original file path for reference
    """
    try:
        # Read the entire file as text
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Z-Wave JS config files may contain // comments - remove them
        # This makes the content valid JSON for parsing
        content = re.sub(r'//.*?$', '', content, flags=re.MULTILINE)
        
        # --- Extract Required Fields ---
        
        # Find manufacturer name (required field)
        manufacturer_match = re.search(r'"manufacturer"\s*:\s*"([^"]*)"', content)
        if not manufacturer_match:
            return None  # Skip files without manufacturer
        
        # Find manufacturer ID in hex format (required field)
        mfr_id_match = re.search(r'"manufacturerId"\s*:\s*"([^"]*)"', content)
        if not mfr_id_match:
            return None  # Skip files without manufacturer ID
        
        # Find device label (optional - e.g., "ZW096")
        label_match = re.search(r'"label"\s*:\s*"([^"]*)"', content)
        label = label_match.group(1) if label_match else ''
        
        # Find device description (optional - e.g., "Smart Switch 6")
        desc_match = re.search(r'"description"\s*:\s*"([^"]*)"', content)
        description = desc_match.group(1) if desc_match else ''
        
        # --- Extract Devices Array ---
        # The devices array contains product type/ID combinations for this device
        # Example: [{"productType": "0x0003", "productId": "0x0060"}]
        
        # Find the start of the devices array
        devices_start = re.search(r'"devices"\s*:\s*\[', content)
        if not devices_start:
            return None  # Skip files without devices array
        
        # Find the matching closing bracket using bracket counting
        # This handles nested arrays properly
        start_pos = devices_start.end() - 1  # Position of opening '['
        bracket_count = 0
        end_pos = start_pos
        
        # Count brackets to find where the devices array ends
        for i in range(start_pos, len(content)):
            if content[i] == '[':
                bracket_count += 1
            elif content[i] == ']':
                bracket_count -= 1
                if bracket_count == 0:
                    end_pos = i + 1  # Include the closing bracket
                    break
        
        # Extract just the devices array JSON
        devices_str = content[start_pos:end_pos]
        
        # Parse the devices array (now valid JSON)
        devices = json.loads(devices_str)
        
        # Return the extracted device information
        return {
            'manufacturer': manufacturer_match.group(1),
            'manufacturerId': mfr_id_match.group(1),
            'label': label,
            'description': description,
            'devices': devices,
            '_sourceFile': str(file_path)  # Keep track of source for debugging
        }
        
    except Exception as e:
        # If anything goes wrong (malformed JSON, encoding issues, etc.),
        # skip this file and continue processing others
        return None

def main():
    """
    Main execution function - scans Z-Wave JS config files and creates database.
    
    Command line arguments:
        sys.argv[1]: devices folder path (optional)
        sys.argv[2]: output filename (optional)
    """
    import sys
    
    # Parse command line arguments with defaults
    devices_folder = sys.argv[1] if len(sys.argv) > 1 else 'packages/config/config/devices'
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'zwave_devices_db.json'
    
    # Verify the devices folder exists
    devices_path = Path(devices_folder)
    if not devices_path.exists():
        print(f"Error: {devices_folder} not found")
        print("\nMake sure you've cloned the Z-Wave JS repository:")
        print("  git clone https://github.com/zwave-js/node-zwave-js.git")
        return
    
    print(f"Scanning {devices_folder}...")
    
    # Find all JSON files recursively
    all_files = list(devices_path.rglob("*.json"))
    
    # Filter out template files (they're not actual device configs)
    json_files = [f for f in all_files if '/templates/' not in str(f)]
    
    print(f"Found {len(json_files)} device files")
    
    # Process each file
    devices = []
    skipped = 0
    skipped_files = []
    
    for file_path in json_files:
        # Extract device info from this config file
        device = extract_first_block(file_path)
        
        if device:
            # Successfully extracted - add to database
            devices.append(device)
        else:
            # Failed to extract (missing required fields or malformed)
            skipped += 1
            skipped_files.append(file_path.name)
    
    # Create output structure with metadata
    output = {
        'metadata': {
            'total_devices': len(devices),
            'source': 'z-wavejs/zwave-js device configurations',
            'extraction_date': None  # Could add: datetime.now().isoformat()
        },
        'devices': devices
    }
    
    # Write to output file with nice formatting
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    # Print summary
    print(f"\n✅ Success! Extracted {len(devices)} devices")
    print(f"⏭️  Skipped {skipped} files (missing required fields)")
    print(f"📄 Output: {output_file}")
    
    # Show skipped files if any (for debugging)
    if skipped_files and skipped < 50:  # Don't spam if too many
        print(f"\n⚠️  Skipped files:")
        for filename in sorted(skipped_files)[:10]:  # Show first 10
            print(f"  - {filename}")
        if len(skipped_files) > 10:
            print(f"  ... and {len(skipped_files) - 10} more")

if __name__ == '__main__':
    main()