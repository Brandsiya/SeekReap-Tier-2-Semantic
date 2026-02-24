#!/usr/bin/env python3
"""
Basic usage examples for Tier-2 Semantic Orchestration Layer
"""
import sys
import os
import json

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tier2_core import (
    create_envelope,
    create_envelope_from_tier1,
    validate_envelope_semantics
)

def main():
    print("=== Tier-2 Semantic Orchestration Examples ===\n")
    
    # Example 1: Basic envelope with simple data
    print("1. Creating envelope with simple data:")
    envelope1 = create_envelope({"user": "alice", "action": "login"})
    print(f"   ID: {envelope1['id']}")
    print(f"   Policy: {envelope1['orchestration_policy']}")
    print(f"   Signature: {envelope1['signature']}")
    print(f"   Valid: {validate_envelope_semantics(envelope1)}")
    print()
    
    # Example 2: Envelope with metadata
    print("2. Creating envelope with metadata:")
    envelope2 = create_envelope(
        payload=[1, 2, 3, 4, 5],
        policy="data_processing",
        metadata={"source": "test", "priority": "high"}
    )
    print(f"   Payload: {envelope2['payload']}")
    print(f"   Metadata: {envelope2['metadata']}")
    print(f"   Valid: {validate_envelope_semantics(envelope2)}")
    print()
    
    # Example 3: Using Tier-1 functions (if available)
    print("3. Using Tier-1 atomic behaviors:")
    try:
        envelope3 = create_envelope_from_tier1("add", 5, 3)
        print(f"   add(5,3) = {envelope3['payload']}")
        print(f"   Valid: {validate_envelope_semantics(envelope3)}")
    except ImportError:
        print("   Note: Tier-1 not available in path")
    except Exception as e:
        print(f"   Error: {e}")
    print()
    
    # Example 4: Save envelope to file (demonstration)
    print("4. Envelope JSON structure:")
    print(json.dumps(envelope1, indent=2, default=str))

if __name__ == "__main__":
    main()
