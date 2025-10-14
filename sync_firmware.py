import json

# Load firmwarecheck.json
with open('FirmwareCheck.json', 'r') as f:
    firmware_data = json.load(f)

# Load updateFirmware_V2.json
with open('UpdateFirmware_V2.json', 'r') as f:
    update_data = json.load(f)

# Take the WifiFW_version as the main version
version_str = str(firmware_data['WifiFW_version'])
update_data['version'] = version_str

# Save updated updateFirmware_V2.json
with open('UpdateFirmware_V2.json', 'w') as f:
    json.dump(update_data, f, indent=2)

print(f"✅ UpdateFirmware_V2.json synced to version: {version_str}")
