# Contributing to Z-Wave SmartStart QR Decoder

First off, thank you for considering contributing to this project! 🎉

This project was initially vibe coded with Claude.ai, and we welcome contributions from humans and AI-assisted developers alike!

## Ways to Contribute

### 🐛 Report Bugs
- Use the GitHub Issues tab
- Include clear description and steps to reproduce
- Add screenshots if applicable
- Mention browser/OS information

### 💡 Suggest Enhancements
- Open an issue with the `enhancement` label
- Describe the feature and its benefits
- Include mockups or examples if possible

### 📝 Add Device Data
The most valuable contribution! Help expand the `devices.json` database:

1. Find a device in the [Z-Wave JS Database](https://devices.zwave-js.io/)
2. Add it to `devices.json` following the existing format
3. Test with a real QR code if possible
4. Submit a pull request

### 🔧 Code Contributions

#### Getting Started
```bash
git clone https://github.com/yourusername/zwave-qr-decoder.git
cd zwave-qr-decoder
# Open index.html in browser or run PHP server
php -S localhost:8000
```

#### Development Guidelines
- Keep it simple - vanilla JS preferred
- Comment complex logic
- Test across browsers
- Maintain the single-file architecture (index.html)
- Update README if adding features

#### Code Style
- Use clear, descriptive variable names
- Add comments for complex algorithms
- Keep functions focused and small
- Use consistent indentation (4 spaces)

### 📋 Pull Request Process

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
   - Test thoroughly
   - Update documentation if needed
4. **Commit with clear messages**
   ```bash
   git commit -m "Add: Device database entries for Aeotec sensors"
   ```
5. **Push to your fork**
   ```bash
   git push origin feature/amazing-feature
   ```
6. **Open a Pull Request**
   - Describe your changes
   - Link related issues
   - Add screenshots for UI changes

### 🎨 Design Contributions
- UI/UX improvements welcome
- Keep the tool accessible
- Maintain mobile responsiveness
- Stick to the purple gradient theme (or propose alternatives!)

### 📚 Documentation
- Fix typos
- Improve clarity
- Add examples
- Translate to other languages

## Device Database Format

When adding devices to `devices.json`:

```json
{
  "manufacturerId": "0x0086",        // 4-digit hex with 0x prefix
  "manufacturer": "AEON Labs",       // Official manufacturer name
  "devices": [
    {
      "productType": "0x0003",       // 4-digit hex with 0x prefix
      "productId": "0x0084",         // 4-digit hex with 0x prefix
      "label": "ZW096",              // Device model/label
      "description": "Smart Switch 6" // Short description
    }
  ]
}
```

**Tips:**
- Use official manufacturer names
- Include model numbers in labels
- Keep descriptions concise
- Verify hex IDs are lowercase
- Pad hex values to 4 digits

## Testing Your Changes

### Manual Testing Checklist
- [ ] Decode sample QR code successfully
- [ ] Device lookup works (if database changed)
- [ ] Label generates correctly
- [ ] SVG export works
- [ ] PNG export includes QR code
- [ ] Debug panels toggle properly
- [ ] Mobile responsive
- [ ] No console errors

### Sample QR Codes for Testing
```
# Aeotec Smart Switch 6
9001621570034149504483534436062309043170212686520047001006144025600220006342867261443005120803003
```

## Questions?

Feel free to:
- Open an issue for discussion
- Tag maintainers in comments
- Join discussions on existing issues

## Recognition

Contributors will be:
- Listed in the README (if desired)
- Mentioned in release notes
- Forever appreciated! 🙏

## Code of Conduct

### Our Standards
- Be respectful and inclusive
- Accept constructive criticism
- Focus on what's best for the community
- Show empathy toward others

### Unacceptable Behavior
- Harassment or discrimination
- Trolling or insulting comments
- Publishing private information
- Unprofessional conduct

---

**Note:** As an AI-assisted project, we especially welcome contributions that improve documentation, explain complex logic, and make the tool more accessible to all skill levels!

**Happy Contributing! 🚀**

*This project was vibe coded with Claude.ai*
