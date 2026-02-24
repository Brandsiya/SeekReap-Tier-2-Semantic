import sys
import os

print("=== Testing Tier-1 Adapter ===")

# Check if the adapter file exists
adapter_path = "tier2_core/tier1_adapter.py"
if os.path.exists(adapter_path):
    print(f"✅ Adapter file exists at {adapter_path}")
else:
    print(f"❌ Adapter file NOT found at {adapter_path}")

# Check Tier-1 directories
tier1_paths = [
    os.path.expanduser("~/SeekReap-Tier-1-PURE"),
    os.path.expanduser("~/SeekReap-Tier-1-Pure"),
]

for path in tier1_paths:
    if os.path.exists(path):
        print(f"✅ Tier-1 directory exists: {path}")
        print(f"   Contents: {os.listdir(path)}")
    else:
        print(f"❌ Tier-1 directory NOT found: {path}")

# Try importing from the adapter
try:
    print("\nAttempting to import from tier1_adapter...")
    from tier2_core.tier1_adapter import add
    print(f"✅ Successfully imported add from adapter")
    print(f"   add(5,3) = {add(5,3)}")
except Exception as e:
    print(f"❌ Failed to import from adapter: {e}")

# Check Python path
print(f"\nPython path includes: {sys.path}")
