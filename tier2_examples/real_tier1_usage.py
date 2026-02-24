#!/usr/bin/env python3
"""
Example using real Tier-1 functions with Tier-2 envelopes
"""
import sys
import os
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tier2_core import create_envelope
from tier2_core.tier1_adapter import (
    create_seeker, create_reap, record_behavior,
    verify_reap, TIER1_AVAILABLE
)

def main():
    print("=== Tier-2 with Real Tier-1 Functions ===\n")
    
    if not TIER1_AVAILABLE:
        print("❌ Real Tier-1 functions not available")
        return
    
    # Step 1: Create seeker and wrap in envelope
    print("1. Creating seeker envelope...")
    seeker = create_seeker()
    seeker_envelope = create_envelope(
        payload=seeker,
        policy="seeker_creation",
        metadata={"source": "tier2_example"}
    )
    print(f"   Seeker ID: {seeker.id}")
    print(f"   Envelope ID: {seeker_envelope['id']}")
    print()
    
    # Step 2: Create reap and wrap in envelope
    print("2. Creating reap envelope...")
    reap = create_reap(seeker.id)
    reap_envelope = create_envelope(
        payload=reap,
        policy="reap_creation",
        metadata={"seeker_id": seeker.id}
    )
    print(f"   Reap ID: {reap.id}")
    print(f"   Envelope ID: {reap_envelope['id']}")
    print()
    
    # Step 3: Record behaviors and wrap each in envelope
    print("3. Recording behavior envelopes...")
    behaviors = []  # Store actual behavior objects
    behavior_envelopes = []
    
    for i in range(3):
        # Create the actual behavior
        behavior = record_behavior(reap.id, {
            "type": "playback",
            "intensity": 0.8 + (i * 0.05)
        })
        behaviors.append(behavior)
        
        # Create envelope around the behavior
        behavior_envelope = create_envelope(
            payload=behavior,
            policy="behavior_recording",
            metadata={"reap_id": reap.id, "sequence": i+1}
        )
        behavior_envelopes.append(behavior_envelope)
        
        print(f"   Behavior {i+1}:")
        print(f"      ID: {behavior.id}")
        print(f"      Type: {behavior.type}")
        print(f"      Intensity: {behavior.intensity}")
        print(f"      Envelope: {behavior_envelope['id']}")
        print()
    
    # Add behavior IDs to reap (using the actual behavior objects, not envelopes)
    reap.behaviors = [b.id for b in behaviors]
    print(f"   Added {len(reap.behaviors)} behavior IDs to reap")
    print()
    
    # Step 4: Verify reap and wrap result in envelope
    print("4. Creating verification envelope...")
    verified_reap = verify_reap(reap)
    verification_envelope = create_envelope(
        payload=verified_reap,
        policy="reap_verification",
        metadata={
            "reap_id": reap.id,
            "status": verified_reap.status,
            "score": verified_reap.score
        }
    )
    print(f"   Verification status: {verified_reap.status}")
    print(f"   Verification score: {verified_reap.score}")
    print(f"   Envelope ID: {verification_envelope['id']}")
    print()
    
    # Step 5: Save all envelopes to a file
    print("5. Saving all envelopes to 'tier2_output.json'...")
    output = {
        "seeker": seeker_envelope,
        "reap": reap_envelope,
        "behaviors": behavior_envelopes,
        "verification": verification_envelope,
        "summary": {
            "seeker_id": seeker.id,
            "reap_id": reap.id,
            "behavior_ids": [b.id for b in behaviors],
            "verification_status": verified_reap.status,
            "verification_score": verified_reap.score
        }
    }
    
    with open("tier2_output.json", "w") as f:
        json.dump(output, f, indent=2, default=str)
    
    print("✅ Done! Check tier2_output.json")
    
    # Show a preview
    print("\n📋 Summary from output file:")
    print(json.dumps(output["summary"], indent=2))

if __name__ == "__main__":
    main()
