#!/usr/bin/env python3
"""
Clean Tier-2 library usage example.
Demonstrates proper library usage without any runtime patterns.
"""
import json
import base64
import sys
import os

# Add src to path for this example
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from semantic.orchestrator import SemanticOrchestrator

def demonstrate_clean_usage():
    """Demonstrate clean library usage pattern."""
    print("Clean Tier-2 Library Usage")
    print("=" * 40)

    # Instantiate library
    orchestrator = SemanticOrchestrator()

    # Example Tier-1 atomic behavior
    atomic = {
        "type": "calculate",
        "intensity": 0.75,
        "duration": 45,
        "features": ["add", "multiply"]
    }

    print("Input (Tier-1 atomic behavior):")
    print(json.dumps(atomic, indent=2))

    # Transform using library
    semantic = orchestrator.transform_to_semantic(atomic)
    print("\nSemantic transformation (Tier-2):")
    print(f"  Type: {semantic['behavior_type']}")
    print(f"  Intensity: {semantic['intensity']}")

    # Create envelope using library
    envelope = orchestrator.create_envelope(semantic)
    print("\nEnvelope for Tier-3:")
    print(f"  ID: {envelope['envelope_id']}")
    print(f"  Timestamp: {envelope['timestamp']}")

    # Verify envelope structure
    print("\nEnvelope verification:")
    print(f"  Has payload: {'payload' in envelope}")
    print(f"  Has signature: {'signature' in envelope}")

    # Library statistics (volatile, for demonstration)
    stats = orchestrator.get_stats()
    print(f"\nLibrary statistics (volatile):")
    print(f"  Transformations: {stats['transformations_performed']}")
    print(f"  Envelopes created: {stats['envelopes_created']}")

    print("\n✅ Clean library usage demonstrated")
    print("\nNote: This is a pure library example.")
    print("Actual integration would use this library within")
    print("external systems for queue management, monitoring,")
    print("and orchestration.")

if __name__ == "__main__":
    demonstrate_clean_usage()
