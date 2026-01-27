#!/usr/bin/env python3
"""
Tests for Tier-2 Structural Transformation Library.
Only verifies structural guarantees, not semantics.
"""

import sys
sys.path.insert(0, 'src')

import base64
import json
from structural.orchestrator import StructuralOrchestrator, verify_envelope_structure


class TestStructuralTransformation:
    """Test only structural guarantees, not semantics."""
    
    def test_envelope_structure(self):
        """Test that envelope has correct structure."""
        orchestrator = StructuralOrchestrator()
        tier1_input = {"type": "test", "intensity": 0.5}
        
        envelope = orchestrator.create_envelope(tier1_input)
        
        # Tier-2 structural guarantees ONLY
        assert "payload" in envelope
        assert "meta" in envelope
        assert isinstance(envelope["payload"], str)
        assert isinstance(envelope["meta"], dict)
        
        # Meta structural guarantees
        meta = envelope["meta"]
        assert "id" in meta
        assert "timestamp" in meta
        assert isinstance(meta["id"], str)
        assert isinstance(meta["timestamp"], str)
        assert meta["timestamp"].endswith("Z")
    
    def test_payload_opacity(self):
        """Test payload is opaque base64 that decodes to JSON."""
        orchestrator = StructuralOrchestrator()
        envelope = orchestrator.create_envelope({"type": "test"})
        
        payload = envelope["payload"]
        
        # Should be valid base64
        decoded = base64.b64decode(payload)
        
        # Should be valid UTF-8 JSON (opaque serialization only)
        json_str = decoded.decode('utf-8')
        data = json.loads(json_str)
        
        # No semantic guarantees about JSON structure
        assert isinstance(data, dict)
    
    def test_verification_function(self):
        """Test the structural verification function."""
        orchestrator = StructuralOrchestrator()
        
        # Valid envelope should verify
        valid_envelope = orchestrator.create_envelope({"type": "test"})
        assert verify_envelope_structure(valid_envelope) is True
        
        # Invalid envelopes should fail
        assert verify_envelope_structure({}) is False
        assert verify_envelope_structure({"payload": "notbase64", "meta": {}}) is False
        assert verify_envelope_structure({"payload": "bm90anNvbg==", "meta": {}}) is False
    
    def test_determinism(self):
        """Test deterministic behavior (same input = same envelope structure)."""
        orchestrator1 = StructuralOrchestrator()
        orchestrator2 = StructuralOrchestrator()
        
        tier1_input = {"type": "deterministic", "intensity": 0.7}
        
        envelope1 = orchestrator1.create_envelope(tier1_input)
        envelope2 = orchestrator2.create_envelope(tier1_input)
        
        # Structure should be identical
        assert set(envelope1.keys()) == set(envelope2.keys())
        assert set(envelope1["meta"].keys()) == set(envelope2["meta"].keys())
        
        # IDs should be different (timestamps differ)
        assert envelope1["meta"]["id"] != envelope2["meta"]["id"]
    
    def test_stats_tracking(self):
        """Test library statistics tracking."""
        orchestrator = StructuralOrchestrator()
        
        initial_stats = orchestrator.get_stats()
        assert initial_stats["transformations_performed"] == 0
        
        orchestrator.create_envelope({"type": "test"})
        stats_after = orchestrator.get_stats()
        assert stats_after["transformations_performed"] == 1
        
        orchestrator.reset_stats()
        stats_reset = orchestrator.get_stats()
        assert stats_reset["transformations_performed"] == 0
