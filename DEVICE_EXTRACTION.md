# 🔧 Device Database Extraction Guide

## Overview

The `extract_devices.py` script extracts Z-Wave device information from the official [Z-Wave JS](https://github.com/zwave-js/node-zwave-js) repository and converts it into a format compatible with this QR decoder tool.

**What it does:**
- Scans the Z-Wave JS device configuration files
- Extracts manufacturer info, product IDs, labels, and descriptions
- Creates a clean JSON database for offline device lookup
- Skips template files and malformed entries

## Prerequisites

### Required Software
- **Python 3.6+** - [Download Python](https://www.python.org/downloads/)
- **Git** - [Download Git](https://git-scm.com/downloads)

### Check Versions
```bash
python3 --version  # Should show 3.6 or higher
git --version      # Should show any recent version
```

## Step-by-Step Instructions

### Step 1: Download Z-Wave JS Repository

The Z-Wave JS repository contains thousands of device configuration files.

```bash
# Create a working directory
mkdir zwave-extraction
cd zwave-extraction

# Clone the Z-Wave JS repository (this may take a few minutes)
git clone https://github.com/zwave-js/node-zwave-js.git

# Navigate into the repository
cd node-zwave-js

# The device configs are in: packages/config/config/devices/
ls packages/config/config/devices/
```

**Repository size:** ~200 MB  
**Time to clone:** 1-5 minutes depending on connection

### Step 2: Copy the Extraction Script

Copy `extract_devices.py` to the `node-zwave-js` directory:

```bash
# If you're in the node-zwave-js directory
cp /path/to/extract_devices.py .

# Or download directly if you uploaded to GitHub
curl -O https://raw.githubusercontent.com/yourusername/zwave-qr-decoder/main/extract_devices.py
```

### Step 3: Run the Extraction Script

```bash
# Basic usage (uses default paths)
python3 extract_devices.py

# Or specify custom paths
python3 extract_devices.py packages/config/config/devices my_devices.json
```

**What happens:**
1. Script scans all `.json` files in the devices folder
2. Extracts relevant fields from each file
3. Skips files with missing required fields
4. Creates a consolidated JSON database
5. Shows progress and statistics

**Expected output:**
```
Scanning packages/config/config/devices...
Found 3847 device files
Success! Extracted 3821 devices
Skipped 26 files (missing required fields)
Output: zwave_devices_db.json
```

**Time to complete:** 5-30 seconds depending on your system

### Step 4: Verify the Output

```bash
# Check file size
ls -lh zwave_devices_db.json

# Preview first few lines
head -n 20 zwave_devices_db.json

# Count total devices
grep -c '"manufacturer"' zwave_devices_db.json
```

### Step 5: Use the Database

Replace the `devices.json` in your web tool:

```bash
# Copy to your web tool directory
cp zwave_devices_db.json /path/to/zwave-qr-decoder/devices.json

# Or rename if needed
mv zwave_devices_db.json devices.json
```

## Script Usage

### Basic Syntax
```bash
python3 extract_devices.py [devices_folder] [output_file]
```

### Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `devices_folder` | Path to Z-Wave JS device configs | `packages/config/config/devices` |
| `output_file` | Output JSON filename | `zwave_devices_db.json` |

### Examples

**Example 1: Default usage**
```bash
python3 extract_devices.py
# Uses: packages/config/config/devices → zwave_devices_db.json
```

**Example 2: Custom output filename**
```bash
python3 extract_devices.py packages/config/config/devices my_custom_db.json
```

**Example 3: Different devices folder**
```bash
python3 extract_devices.py /path/to/other/devices/ output.json
```

## Output Format

The script generates a JSON file with this structure:

```json
{
  "metadata": {
    "total_devices": 3821,
    "source": "z-wavejs/zwave-js device configurations"
  },
  "devices": [
    {
      "manufacturer": "AEON Labs",
      "manufacturerId": "0x0086",
      "label": "ZW096",
      "description": "Smart Switch 6",
      "devices": [
        {
          "productType": "0x0003",
          "productId": "0x0060"
        },
        {
          "productType": "0x0103",
          "productId": "0x0060"
        }
      ],
      "_sourceFile": "packages/config/config/devices/0x0086/zw096.json"
    }
  ]
}
```

### Field Descriptions

| Field | Description | Example |
|-------|-------------|---------|
| `manufacturer` | Company name | "AEON Labs" |
| `manufacturerId` | Hex manufacturer ID | "0x0086" |
| `label` | Device model/label | "ZW096" |
| `description` | Device description | "Smart Switch 6" |
| `devices` | Array of product variants | See below |
| `_sourceFile` | Original config file path | For reference |

**Devices array items:**

| Field | Description | Example |
|-------|-------------|---------|
| `productType` | Hex product type | "0x0003" |
| `productId` | Hex product ID | "0x0060" |

## Troubleshooting

### Error: "packages/config/config/devices not found"

**Solution:**
```bash
# Make sure you're in the node-zwave-js directory
pwd  # Should end with /node-zwave-js

# Check if devices folder exists
ls packages/config/config/devices/
```

### Error: "Python not found"

**Solution:**
```bash
# Try python instead of python3
python --version

# Or install Python 3
# macOS: brew install python3
# Ubuntu: sudo apt install python3
# Windows: Download from python.org
```

### Script runs but extracts 0 devices

**Solution:**
```bash
# Check if you're in the right directory
ls packages/config/config/devices/*.json

# Verify the path is correct
python3 extract_devices.py packages/config/config/devices
```

### Permission denied

**Solution:**
```bash
# Make script executable (Unix/Mac/Linux)
chmod +x extract_devices.py

# Then run with
./extract_devices.py
```

### Output file is empty or malformed

**Solution:**
```bash
# Delete and try again
rm zwave_devices_db.json
python3 extract_devices.py

# Check Python version (needs 3.6+)
python3 --version
```

## Updating the Database

Z-Wave JS is actively maintained with new devices added regularly.

### Update Workflow

```bash
# Navigate to z-wave-js repository
cd node-zwave-js

# Pull latest changes
git pull origin master

# Re-run extraction
python3 extract_devices.py

# Copy to your web tool
cp zwave_devices_db.json /path/to/zwave-qr-decoder/devices.json
```

**Recommended update frequency:** Monthly or when you encounter unknown devices

## Advanced Usage

### Extract Specific Manufacturers

Modify the script to filter by manufacturer:

```python
# After line: if device:
if device and device['manufacturerId'] == '0x0086':  # Only AEON Labs
    devices.append(device)
```

### Add Additional Fields

The script currently extracts:
- manufacturer
- manufacturerId  
- label
- description
- devices (productType, productId)

To extract more fields, modify the `extract_first_block()` function.

### Batch Processing

Process multiple Z-Wave JS versions:

```bash
#!/bin/bash
for version in v12.0.0 v12.1.0 v12.2.0; do
  git checkout $version
  python3 extract_devices.py packages/config/config/devices devices_${version}.json
done
```

## Script Details

### What Gets Extracted

✅ **Included:**
- Manufacturer name and ID
- Device label and description
- Product type and ID combinations
- Source file reference

❌ **Excluded:**
- Firmware versions
- Configuration parameters
- Command classes
- Association groups
- Device images
- Template files

### Why Some Files Are Skipped

Files are skipped if they:
- Missing `manufacturer` field
- Missing `manufacturerId` field
- Missing `devices` array
- Malformed JSON syntax
- Located in `/templates/` directory

### Performance

- **Speed:** ~150-200 files per second
- **Memory:** <100 MB RAM usage
- **Output size:** ~1-2 MB for full database

## Integration with Web Tool

### Automatic Fallback

The web tool uses a layered lookup approach:

1. **Local database** (`devices.json`) - Fast, offline
2. **Z-Wave JS API** - Online fallback if not in local DB

### Benefits of Local Database

✅ **Fast lookups** - No network required  
✅ **Privacy** - No external API calls  
✅ **Reliability** - Works offline  
✅ **Customizable** - Add your own devices  

### Manual Device Addition

You can manually add devices to the JSON:

```json
{
  "manufacturer": "Your Company",
  "manufacturerId": "0xABCD",
  "label": "Custom Device",
  "description": "My custom Z-Wave device",
  "devices": [
    {
      "productType": "0x1234",
      "productId": "0x5678"
    }
  ]
}
```

## FAQ

### Q: How often should I update the database?
**A:** Monthly is usually sufficient. Update sooner if you encounter unknown devices.

### Q: Can I use a partial database?
**A:** Yes! Extract only manufacturers you need to reduce file size.

### Q: What if a device isn't in Z-Wave JS?
**A:** You can manually add it to `devices.json` or it will fallback to the online API.

### Q: Does this work on Windows?
**A:** Yes! Use `python` instead of `python3` in commands.

### Q: How do I contribute extracted devices?
**A:** Update `devices.json` in your fork and submit a pull request!

### Q: Can I automate updates?
**A:** Yes! Set up a cron job or GitHub Action to run monthly.

## Quick Reference

### One-Line Commands

**Complete workflow:**
```bash
git clone https://github.com/zwave-js/node-zwave-js.git && cd node-zwave-js && curl -O https://raw.githubusercontent.com/yourusername/zwave-qr-decoder/main/extract_devices.py && python3 extract_devices.py
```

**Update only:**
```bash
cd node-zwave-js && git pull && python3 extract_devices.py && cp zwave_devices_db.json ../zwave-qr-decoder/devices.json
```

**Check device count:**
```bash
python3 -c "import json; d=json.load(open('devices.json')); print(f\"Devices: {d['metadata']['total_devices']}\")"
```

## Resources

- **Z-Wave JS Repository:** https://github.com/zwave-js/node-zwave-js
- **Z-Wave JS Device Database:** https://devices.zwave-js.io/
- **Z-Wave Alliance:** https://z-wavealliance.org/
- **Python Documentation:** https://docs.python.org/3/

## Support

If you encounter issues:

1. Check the [Troubleshooting](#troubleshooting) section
2. Verify Python and Git are installed correctly
3. Ensure you're in the right directory
4. Check file permissions
5. Open an issue on GitHub with error details

---

**Created with Claude.ai** 🤖

This extraction script makes it easy to maintain an up-to-date device database for offline use!
