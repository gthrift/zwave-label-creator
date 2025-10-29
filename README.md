# Z-Wave SmartStart QR Decoder & Label Generator

A web-based tool to decode Z-Wave SmartStart QR codes and generate printable device labels. Perfect for home automation enthusiasts and Z-Wave device management.

![Z-Wave QR Decoder](https://img.shields.io/badge/Z--Wave-SmartStart-blue)
![License](https://img.shields.io/badge/license-MIT-green)

> **Note:** This project was vibe coded with [Claude.ai](https://claude.ai) 🤖

## Features

✨ **QR Code Decoding**
- Decode Z-Wave SmartStart QR codes instantly
- Extract Device Specific Key (DSK)
- Parse manufacturer ID, product type, and product ID
- Display security classes and supported protocols

🏷️ **Label Generation**
- Generate professional device labels
- Embedded QR codes for easy re-scanning
- Multiple export formats: SVG, PNG
- Compact 250px width design perfect for label printers

🔍 **Device Lookup**
- Automatic device identification from local database
- Fallback to Z-Wave JS database API
- Display manufacturer name, device label, and description
- Search links for unknown devices

🛠️ **Developer-Friendly**
- Built-in debug tools
- API lookup debugging
- TLV parsing visualization
- Clean, modern interface

## Demo

### Decode QR Code
Paste your Z-Wave SmartStart QR code text to instantly decode device information:

```
9001621570034149504483534436062309043170212686520047001006144025600220006342867261443005120803003
```

### Generated Label Preview
The tool generates compact labels with:
- QR code for device provisioning
- Manufacturer and product information
- Product Type and ID
- Full DSK (Device Specific Key)

## Installation

### Option 1: Direct Use (Static HTML)
Simply open `index.html` in a web browser. No server required for basic functionality!

```bash
git clone https://github.com/yourusername/zwave-qr-decoder.git
cd zwave-qr-decoder
open index.html  # or double-click the file
```

### Option 2: Local Web Server (Recommended)
For full device lookup functionality using the PHP API:

```bash
# Clone the repository
git clone https://github.com/yourusername/zwave-qr-decoder.git
cd zwave-qr-decoder

# Start a PHP development server
php -S localhost:8000

# Open in browser
open http://localhost:8000
```

### Option 3: Deploy to Web Server
Upload all files to your web server:
- `index.html` - Main application
- `lookup.php` - Device lookup API endpoint
- `devices.json` - Local device database

Ensure PHP is enabled on your web server.

## Usage

### Basic Usage

1. **Obtain QR Code Text**
   - Scan Z-Wave device QR code with any QR scanner app
   - Or locate the printed code text on device packaging

2. **Decode**
   - Paste the QR code text into the input field
   - Click "🔍 Decode QR Code"
   - View decoded device information

3. **Generate Label**
   - Click "🏷️ Generate Label" button (appears after decoding)
   - Preview the generated label
   - Download as SVG or PNG

### Export Options

- **SVG**: Vector format, perfect for scaling and editing
- **PNG**: High-quality raster image (2x resolution)
- ~~**JPEG**: Currently hidden but available in code~~

## Device Database

The tool includes a local `devices.json` database for offline device lookup. To add devices:

```json
{
  "devices": [
    {
      "manufacturerId": "0x0086",
      "manufacturer": "AEON Labs",
      "devices": [
        {
          "productType": "0x0003",
          "productId": "0x0084",
          "label": "ZW096",
          "description": "Smart Switch 6"
        }
      ]
    }
  ]
}
```

### Database Sources
- [Z-Wave JS Device Database](https://devices.zwave-js.io/)
- [OpenSmartHouse Database](https://opensmarthouse.org/zwavedatabase/)

## File Structure

```
zwave-qr-decoder/
├── index.html          # Main application (single-file app)
├── lookup.php          # PHP API for device lookups
├── devices.json        # Local device database
├── README.md           # This file
├── LICENSE             # MIT License
└── .gitignore          # Git ignore rules
```

## Technical Details

### QR Code Format
Z-Wave SmartStart QR codes follow the format:
- **Lead-in**: `90` (SmartStart identifier)
- **Version**: 2 digits
- **Checksum**: 5 digits
- **Requested Keys**: 3 digits (security classes)
- **DSK**: 40 digits (Device Specific Key)
- **TLVs**: Variable length (Type-Length-Value pairs)

### TLV Types Supported
- **Type 2**: Manufacturer/Product information
- **Type 8**: Supported protocols (Z-Wave, Z-Wave LR)

### Label Specifications
- **Dimensions**: 250px × 140px
- **QR Code**: 100px × 100px
- **Text**: Variable size (10-14pt)
- **Format**: SVG with embedded QR code

## Browser Support

- ✅ Chrome/Edge (Recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Mobile browsers

## API Endpoints

### Local Lookup
```
GET /lookup.php?manufacturerId=0x0086&productType=0x0003&productId=0x0084
```

### Z-Wave JS Fallback
```
GET https://devices.zwave-js.io/api/devices?manufacturerId=0x0086&productType=0x0003&productId=0x0084
```

## Development

Built with vanilla JavaScript - no frameworks required!

**Dependencies:**
- [QRCode.js](https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js) - QR code generation

### Debug Mode
Enable debug information to see:
- TLV parsing details
- API request/response logs
- Device lookup process

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Ideas for Contributions
- Add more devices to `devices.json`
- Improve label designs
- Add support for additional TLV types
- Multi-language support
- Batch QR code processing

## Known Issues

- JPEG export is currently disabled (available in code)
- Some older browsers may have issues with SVG export

## Changelog

### v1.0.0 (2025)
- Initial release
- QR code decoding
- Label generation (SVG/PNG)
- Device database lookup
- Debug tools
- Fixed PNG export QR code rendering bug

## Credits

**Vibe coded with [Claude.ai](https://claude.ai)** 🎉

This project was created using Claude, an AI assistant by Anthropic, demonstrating the power of AI-assisted development for creating practical tools.

## License

MIT License - see [LICENSE](LICENSE) file for details

## Support

If you find this tool useful, please:
- ⭐ Star this repository
- 🐛 Report issues
- 🔧 Submit pull requests
- 📢 Share with other Z-Wave enthusiasts

## Links

- [Z-Wave Alliance](https://z-wavealliance.org/)
- [Z-Wave JS](https://zwave-js.github.io/node-zwave-js/)
- [SmartStart Specification](https://z-wavealliance.org/smartstart/)

---

**Made with ❤️ and Claude.ai for the Z-Wave community**
