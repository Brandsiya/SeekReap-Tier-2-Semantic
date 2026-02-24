import unittest
import sys
import os

# Add parent directory to path so we can import tier2_core
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from tier2_core.orchestration.envelope import create_envelope
from tier2_core.orchestration.validation import (
    validate_envelope_structure,
    validate_envelope_semantics
)

class TestEnvelope(unittest.TestCase):
    
    def test_create_basic_envelope(self):
        """Test creating a basic envelope"""
        payload = {"test": "data", "value": 42}
        envelope = create_envelope(payload)
        
        # Check required fields exist
        self.assertIn("id", envelope)
        self.assertIn("timestamp", envelope)
        self.assertIn("payload", envelope)
        self.assertIn("schema_version", envelope)
        self.assertIn("orchestration_policy", envelope)
        self.assertIn("signature", envelope)
        
        # Check payload is deep copied (not same reference)
        self.assertEqual(envelope["payload"]["test"], "data")
        self.assertEqual(envelope["payload"]["value"], 42)
        
        # Check signature format
        self.assertTrue(envelope["signature"].startswith("tier2-semantic-"))
    
    def test_envelope_with_metadata(self):
        """Test envelope with metadata"""
        payload = "test string"
        metadata = {"source": "test", "version": 1}
        
        envelope = create_envelope(payload, policy="test_policy", metadata=metadata)
        
        self.assertEqual(envelope["payload"], "test string")
        self.assertEqual(envelope["orchestration_policy"], "test_policy")
        self.assertEqual(envelope["metadata"]["source"], "test")
        self.assertEqual(envelope["metadata"]["version"], 1)
    
    def test_validation(self):
        """Test envelope validation"""
        envelope = create_envelope(42)
        
        self.assertTrue(validate_envelope_structure(envelope))
        self.assertTrue(validate_envelope_semantics(envelope))
        
        # Corrupt the envelope
        bad_envelope = envelope.copy()
        del bad_envelope["id"]
        
        self.assertFalse(validate_envelope_structure(bad_envelope))

if __name__ == '__main__':
    unittest.main()
