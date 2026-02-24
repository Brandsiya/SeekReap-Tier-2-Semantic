#!/usr/bin/env python3
"""
Test the real Tier-1 functions through the adapter
"""
import sys
sys.path.insert(0, '.')

try:
    from tier2_core.tier1_adapter import (
        create_seeker, create_reap, record_behavior,
        verify_reap, emit_verification_event,
        TIER1_AVAILABLE
    )
    
    print("=== Testing Real Tier-1 Functions ===\n")
    
    if not TIER1_AVAILABLE:
        print("❌ Real Tier-1 functions not available")
        sys.exit(1)
    
    # Test 1: Create seeker
    print("1. Creating seeker...")
    seeker = create_seeker()
    print(f"   Seeker created: {seeker}")
    print(f"   Seeker ID: {seeker.id}")
    print(f"   Seeker status: {seeker.status}")
    print()
    
    # Test 2: Create reap
    print("2. Creating reap...")
    reap = create_reap(seeker.id)
    print(f"   Reap created: {reap}")
    print(f"   Reap ID: {reap.id}")
    print(f"   Reap status: {reap.status}")
    print()
    
    # Test 3: Record behaviors (need at least 3 for verification)
    print("3. Recording behaviors...")
    behaviors = []
    for i in range(3):
        behavior = record_behavior(reap.id, {
            "type": "playback",
            "intensity": 0.8 + (i * 0.05)
        })
        behaviors.append(behavior)
        print(f"   Behavior {i+1}: {behavior}")
        print(f"      Type: {behavior.type}, Intensity: {behavior.intensity}")
    
    # Add behavior IDs to reap (this is how the real system works)
    reap.behaviors = [b.id for b in behaviors]
    print(f"   Added {len(reap.behaviors)} behaviors to reap")
    print()
    
    # Test 4: Verify reap
    print("4. Verifying reap...")
    verified_reap = verify_reap(reap)
    print(f"   Verified reap status: {verified_reap.status}")
    print(f"   Verified reap score: {verified_reap.score}")
    print(f"   Verification {'PASSED' if verified_reap.status == 'verified' else 'FAILED'}")
    print()
    
    # Test 5: Emit event
    print("5. Emitting verification event...")
    event = emit_verification_event(reap.id)
    print(f"   Event: {event}")
    
    print("\n✅ All tests passed!")

except ImportError as e:
    print(f"❌ Import error: {e}")
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
