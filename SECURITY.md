# Security Policy

## Supported Versions

This project is currently in active development. Security updates will be applied to the latest version.

| Version | Supported          |
| ------- | ------------------ |
| 1.x     | :white_check_mark: |

## Reporting a Vulnerability

We take security seriously. If you discover a security vulnerability, please follow these steps:

### 🔒 For Security Issues

**DO NOT** open a public issue for security vulnerabilities.

Instead:

1. **Email** the repository maintainer directly (check GitHub profile for contact)
2. **Include** detailed information:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)
3. **Wait** for acknowledgment (typically within 48 hours)
4. **Allow** time for a fix before public disclosure

### 📧 What to Include

```
Subject: [SECURITY] Brief description of vulnerability

Description:
- What is the vulnerability?
- Where is it located? (file, line, function)
- What is the potential impact?

Steps to Reproduce:
1. Step one
2. Step two
3. Step three

Environment:
- Browser: Chrome 120
- OS: Windows 11
- Version: Latest commit hash

Additional Context:
Any other relevant information
```

### ⏱️ Response Timeline

- **Acknowledgment**: Within 48 hours
- **Initial Assessment**: Within 1 week
- **Status Updates**: Every 2 weeks
- **Fix Timeline**: Varies by severity

### 🏆 Recognition

Security researchers who responsibly disclose vulnerabilities will be:
- Acknowledged in the CHANGELOG (if desired)
- Credited in the security advisory
- Given our sincere thanks! 🙏

## Security Best Practices

### For Users

1. **HTTPS Only**: Always use HTTPS when deploying
2. **Update Regularly**: Keep the tool updated
3. **Review Code**: This is open source - review before deploying
4. **Secure Hosting**: Use secure web hosting
5. **Input Validation**: Be cautious with QR codes from untrusted sources

### For Developers

1. **Sanitize Input**: All user input is escaped
2. **CORS**: API endpoints use appropriate CORS headers
3. **No Secrets**: Never commit API keys or secrets
4. **Dependencies**: Keep QRCode.js and other dependencies updated
5. **XSS Prevention**: All dynamic content is properly escaped

## Known Security Considerations

### Client-Side Processing
- All QR code processing happens client-side
- No data is sent to external servers (except device lookups)
- Device lookups use public APIs

### PHP API (lookup.php)
- Input validation on all parameters
- No database writes (read-only)
- No user authentication (public tool)
- JSON sanitization

### Data Privacy
- No personal data collected
- No cookies or tracking
- No analytics
- Local storage not used

## Security Features

✅ Input validation and sanitization  
✅ CSP-friendly (no inline scripts in production use)  
✅ No external data transmission (except device DB lookups)  
✅ Read-only operations  
✅ Client-side processing  

## Disclosure Policy

We follow responsible disclosure practices:

1. Security issues are fixed privately
2. Fixes are tested thoroughly
3. A security advisory is published
4. Users are notified of the update
5. Detailed disclosure after fix is deployed

## Questions?

For general security questions (non-vulnerabilities):
- Open a GitHub Discussion
- Tag with `security` label

---

**Remember:** This tool processes Z-Wave QR codes which may contain device-specific keys. Always protect device DSKs and use the tool responsibly.

*Security is everyone's responsibility. Thank you for helping keep this project safe!* 🔐
