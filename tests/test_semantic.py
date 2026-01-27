#!/usr/bin/env python3
"""
Tests for Tier-2 semantic functionality
"""
import json
import base64
import sys
import os

# Add src to path for testing (temporary fix)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.semantic.orchestrator import SemanticOrchestrator
from src.semantic import constants


def test_constants():
    """Test that required constants are defined"""
    assert constants.TIER3_ENVELOPE_VERSION == "1.0"
    assert "envelope_id" in constants.ENVELOPE_SCHEMA
    assert "behavior_type" in constants.SEMANTIC_FIELDS
    assert "calculate" in constants.BEHAVIOR_TYPES


def test_orchestrator_creation():
    """Test orchestrator creation"""
    orchestrator = SemanticOrchestrator()
    assert orchestrator.envelopes_created == 0
    assert orchestrator.transformations_performed == 0


def test_semantic_transformation():
    """Test atomic → semantic transformation"""
    orchestrator = SemanticOrchestrator()

    atomic_behavior = {
        "type": "calculate",
        "intensity": 0.75,
        "duration": 30,
        "features": ["addition", "multiplication"],
        "metadata": {"operation": "math"}
    }

    semantic = orchestrator.transform_to_semantic(atomic_behavior)

    assert semantic["behavior_type"] == "computation"
    assert semantic["intensity"] == 0.75
    assert semantic["duration"] == 30
    assert semantic["features_used"] == ["addition", "multiplication"]
    assert semantic["_version"] == "1.0"
    assert semantic["_semantic"] is True
    assert "metadata" in semantic

    assert orchestrator.transformations_performed == 1


def test_envelope_creation():
    """Test envelope creation from semantic data"""
    orchestrator = SemanticOrchestrator()

    semantic_data = {
        "behavior_type": "data_processing",
        "intensity": 0.6,
        "duration": 45,
        "features_used": ["filter", "sort"]
    }

    envelope = orchestrator.create_envelope(semantic_data)

    # Check envelope structure
    assert "envelope_id" in envelope
    assert envelope["envelope_id"].startswith("env_")
    assert "timestamp" in envelope
    assert "payload" in envelope
    assert "signature" in envelope
    assert envelope["signature"].startswith("sig_")

    # Verify payload can be decoded
    decoded = base64.b64decode(envelope["payload"]).decode('utf-8')
    payload_data = json.loads(decoded)

    assert payload_data["behavior_type"] == "data_processing"
    assert payload_data["intensity"] == 0.6
    assert payload_data["_version"] == "1.0"

    # Check stats
    assert orchestrator.envelopes_created == 1


def test_intensity_normalization():
    """Test intensity normalization"""
    orchestrator = SemanticOrchestrator()

    # Test too high
    atomic_high = {"type": "test", "intensity": 1.5}
    semantic_high = orchestrator.transform_to_semantic(atomic_high)
    assert semantic_high["intensity"] == 1.0

    # Test too low
    atomic_low = {"type": "test", "intensity": -0.5}
    semantic_low = orchestrator.transform_to_semantic(atomic_low)
    assert semantic_low["intensity"] == 0.0

    # Test in range
    atomic_normal = {"type": "test", "intensity": 0.7}
    semantic_normal = orchestrator.transform_to_semantic(atomic_normal)
    assert semantic_normal["intensity"] == 0.7


def test_behavior_type_mapping():
    """Test behavior type mapping"""
    orchestrator = SemanticOrchestrator()

    # Test known mapping
    atomic_calc = {"type": "calculate", "intensity": 0.5}
    semantic_calc = orchestrator.transform_to_semantic(atomic_calc)
    assert semantic_calc["behavior_type"] == "computation"

    # Test unknown mapping (pass through)
    atomic_unknown = {"type": "custom_action", "intensity": 0.5}
    semantic_unknown = orchestrator.transform_to_semantic(atomic_unknown)
    assert semantic_unknown["behavior_type"] == "custom_action"


def test_full_pipeline():
    """Test full atomic → semantic → envelope pipeline"""
    orchestrator = SemanticOrchestrator()

    atomic_behavior = {
        "type": "process_data",
        "intensity": 0.8,
        "duration": 120,
        "features": ["clean", "transform", "analyze"],
        "user_segment": "premium",
        "premium_indicator": True
    }

    # Transform to semantic
    semantic = orchestrator.transform_to_semantic(atomic_behavior)
    assert semantic["behavior_type"] == "data_processing"
    assert semantic["intensity"] == 0.8
    assert semantic["user_segment"] == "premium"
    assert semantic["premium_indicator"] is True

    # Create envelope
    envelope = orchestrator.create_envelope(semantic)
    assert "envelope_id" in envelope
    assert "payload" in envelope

    # Decode and verify
    decoded = base64.b64decode(envelope["payload"]).decode('utf-8')
    payload = json.loads(decoded)

    assert payload["behavior_type"] == "data_processing"
    assert payload["intensity"] == 0.8
    assert payload["user_segment"] == "premium"
    assert payload["premium_indicator"] is True

    # Check stats
    stats = orchestrator.get_stats()
    assert stats["transformations_performed"] == 1
    assert stats["envelopes_created"] == 1


if __name__ == "__main__":
    print("Running Tier-2 tests...")

    test_constants()
    print("✅ Constants test passed")

    test_orchestrator_creation()
    print("✅ Orchestrator creation test passed")

    test_semantic_transformation()
    print("✅ Semantic transformation test passed")

    test_envelope_creation()
    print("✅ Envelope creation test passed")

    test_intensity_normalization()
    print("✅ Intensity normalization test passed")

    test_behavior_type_mapping()
    print("✅ Behavior type mapping test passed")

    test_full_pipeline()
    print("✅ Full pipeline test passed")

    print("\n🎉 All Tier-2 tests passed!")
