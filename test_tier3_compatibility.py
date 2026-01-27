"""
Verify Tier-2 output matches Tier-3 expectations
"""
import json
import base64
from src.semantic.orchestrator import SemanticOrchestrator

def test_tier3_envelope_schema():
    """Verify envelope matches Tier-3 expected schema"""
    orchestrator = SemanticOrchestrator()
    
    # Create semantic data matching Tier-3 example
    semantic_data = {
        "behavior_type": "deep_research",
        "intensity": 0.85,
        "duration": 180,
        "premium_indicator": True,
        "user_segment": "professional",
        "features_used": ["advanced_search", "export", "analytics"],
        "_version": "1.0",
        "_semantic": True
    }
    
    envelope = orchestrator.create_envelope(semantic_data)
    
    # Check envelope structure (from Tier-3 README expectations)
    required_fields = ["envelope_id", "timestamp", "payload", "signature"]
    for field in required_fields:
        assert field in envelope, f"Missing required field: {field}"
    
    # Verify payload can be decoded
    decoded = base64.b64decode(envelope["payload"]).decode('utf-8')
    payload_data = json.loads(decoded)
    
    # Check semantic data preserved
    assert payload_data["behavior_type"] == "deep_research"
    assert payload_data["intensity"] == 0.85
    assert payload_data["duration"] == 180
    assert payload_data["premium_indicator"] is True
    assert payload_data["user_segment"] == "professional"
    assert payload_data["features_used"] == ["advanced_search", "export", "analytics"]
    
    print("✅ Tier-3 compatibility verified")

if __name__ == "__main__":
    test_tier3_envelope_schema()
