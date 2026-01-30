# Tier-2 → Tier-3 Structural Contract

## Contract Version: 1.0.0
**Status**: Structural only
**Tier-2 Provider**: `seekreap-tier2-structural`
**Tier-3 Freedom**: Any consumption pattern

## 1. Structural Guarantees
Tier-2 guarantees ONLY this output structure:
```python
{
    "payload": "base64_string",  # Valid base64 → JSON (opaque)
    "meta": {
        "id": "string",          # Unique identifier
        "timestamp": "ISO8601"   # With Z suffix
    }
}
```

## 2. What Tier-2 Does NOT Guarantee
- Semantic meaning of payload
- Validation rules
- Performance characteristics
- Schema compliance

## 3. Verification
Use only `verify_envelope_structure()` from the library.
