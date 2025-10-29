# Changelog

All notable changes to the Z-Wave SmartStart QR Decoder will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2025-10-29

### 🎉 New Features

#### 📷 Camera QR Code Scanning
- Added camera scanning functionality with live QR code detection
- Camera icon button in QR code input field
- Full-screen camera modal with video preview
- Visual target box to guide QR code positioning
- Automatic QR code detection using jsQR library
- Auto-populate and decode after successful scan
- Mobile-optimized (uses back camera on phones)
- Works on desktop with webcams

#### 🧹 Label Clearing on Decode
- Automatically clears previous label when decoding new QR code
- Prevents downloading wrong labels by mistake
- Forces regeneration of label for each device
- Improves workflow safety

### Technical
- Added jsQR library for QR code scanning
- Implemented getUserMedia API for camera access
- Added Canvas API for frame capture
- Enhanced error handling for camera permissions
- HTTPS/localhost required for camera access

### UI/UX Improvements
- Camera button with hover effects
- Status messages during scanning
- Success notification when QR detected
- Smooth modal transitions
- Click outside modal to close
- Mobile-responsive camera view

---

## [1.0.0] - 2025-10-29

### 🎉 Initial Release

The first public release of Z-Wave SmartStart QR Decoder, vibe coded with Claude.ai!

### Added
- QR code decoding functionality
  - Parse Z-Wave SmartStart QR codes
  - Extract Device Specific Key (DSK)
  - Decode manufacturer ID, product type, and product ID
  - Display security classes and supported protocols
  
- Label generation system
  - Generate printable device labels
  - Embedded QR codes
  - SVG export format
  - PNG export format (high resolution)
  - Compact 250px width design
  
- Device database integration
  - Local `devices.json` database
  - PHP API endpoint (`lookup.php`)
  - Fallback to Z-Wave JS online database
  - Device manufacturer and model lookup
  
- User interface
  - Clean, modern purple gradient design
  - Responsive layout
  - Mobile-friendly
  - Accessible design
  
- Debug tools
  - TLV parsing visualization
  - API request/response logging
  - Collapsible debug sections

### Fixed
- PNG export QR code rendering bug
  - QR codes now properly render in exported PNG files
  - Implemented direct canvas drawing method
  
### Technical
- Single-file architecture (index.html)
- Vanilla JavaScript (no frameworks)
- QRCode.js for QR generation
- PHP backend for device lookups
- CORS-enabled API endpoints

### Documentation
- Comprehensive README.md
- MIT License
- Contributing guidelines
- Security policy
- This changelog

---

## [Unreleased]

### Planned Features
- [ ] Batch QR code processing
- [ ] Custom label templates
- [ ] Multi-language support
- [ ] Export to PDF
- [ ] Label size customization
- [ ] Dark mode theme
- [ ] Keyboard shortcuts
- [ ] Import/export device database
- [ ] CSV export of decoded data
- [ ] History of decoded QR codes

### Potential Improvements
- [ ] Add more devices to database
- [ ] Improve label design options
- [ ] Support additional TLV types
- [ ] Offline PWA support
- [ ] Print directly from browser
- [ ] QR code camera scanning
- [ ] Advanced search in device database

---

## Release Notes

### What is Z-Wave SmartStart?
Z-Wave SmartStart is a feature that simplifies the process of adding Z-Wave devices to a smart home network. Each device has a QR code containing its Device Specific Key (DSK) and other identifying information.

### Why This Tool?
This tool helps you:
- Decode QR codes without adding devices to your network
- Generate backup labels for devices
- Identify unknown Z-Wave devices
- Document your Z-Wave installation

### Credits
**Vibe coded with Claude.ai** - This entire project was created through an AI-assisted development process, demonstrating the power of human-AI collaboration in software development.

---

## Version History

- **1.0.0** (2025-10-29) - Initial release

---

## How to Update

To get the latest version:

```bash
git pull origin main
```

Or download the latest release from the [Releases](https://github.com/yourusername/zwave-qr-decoder/releases) page.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute to future versions.

---

*For support and questions, please open an issue on GitHub.*
