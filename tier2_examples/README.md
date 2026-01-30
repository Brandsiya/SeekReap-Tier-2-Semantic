# Tier-2 Semantic Envelope Examples

Real-world usage examples demonstrating semantic envelope patterns in production-like scenarios.

## Purpose

These examples show how to use Tier-2 semantic envelopes for:
- Workflow composition and orchestration
- Data processing pipelines
- Error handling and recovery patterns
- Audit and compliance logging
- Real-world application scenarios

## Examples Included

### 1. Basic Envelope Creation (`example_basic_envelope_creation()`)
Demonstrates creating envelopes with different payload types:
- Simple string payloads
- JSON-like dictionary structures
- Payloads with metadata (sensor data example)

### 2. Workflow Composition (`example_workflow_composition()`)
Shows how to create workflow chains with multiple envelopes:
- User registration workflow simulation
- Envelope dependencies and causality
- Workflow validation and completeness checking

### 3. Data Processing Pipeline (`example_data_pipeline()`)
Illustrates data transformation pipelines:
- Multi-stage processing (ingestion → transformation → aggregation)
- Audit trail maintenance
- Pipeline state management and validation

### 4. Error Handling and Recovery (`example_error_handling_and_recovery()`)
Demonstrates error patterns and recovery workflows:
- Error envelope creation with context
- Recovery strategies and actions
- Retry patterns with semantic metadata

### 5. Audit and Compliance (`example_audit_and_compliance()`)
Shows compliance and audit logging:
- GDPR-compliant audit trails
- Immutable audit records
- Compliance metadata patterns

## Key Patterns Demonstrated

### Semantic Metadata
Each example shows appropriate metadata for different scenarios:
- Workflow steps and dependencies
- Pipeline stages and transformations
- Error severity and recovery actions
- Compliance requirements and retention

### Immutability Guarantees
All examples leverage the immutability properties:
- Deep copies prevent accidental data modification
- Unique signatures ensure envelope authenticity
- Timestamps provide temporal ordering

### Validation Patterns
Examples include validation at different levels:
- Individual envelope validation
- Workflow completeness validation
- Pipeline integrity checking

## Running the Examples

```bash
# Run all examples
python3 tier2_examples/envelope_usage_example.py

# Test example functionality
python3 tier2_examples/test_examples.py

## Integration Points

These examples can be extended for:

### Microservices Communication
- Service-to-service envelope exchange
- Event-driven architectures
- Distributed workflow coordination

### Data Engineering
- ETL pipeline orchestration
- Data quality monitoring
- Batch and stream processing

### Security and Compliance
- Audit trail generation
- Compliance evidence collection
- Security incident logging

## Best Practices Demonstrated

1. **Meaningful Metadata**: Each envelope includes context-appropriate metadata
2. **Clear Dependencies**: Workflow envelopes explicitly reference their dependencies
3. **Complete Audit Trails**: All actions are logged with sufficient context
4. **Error Context**: Errors include enough information for debugging and recovery
5. **Validation Integration**: All examples include validation checks

## Extending These Examples

To adapt these patterns to your use case:

1. **Define Your Domain Metadata**: What metadata is important for your domain?
2. **Map Your Workflows**: How do your processes translate to envelope chains?
3. **Identify Compliance Needs**: What audit and compliance requirements do you have?
4. **Design Recovery Patterns**: How should errors be handled and recovered from?

## Related Documentation

- [Property-Based Tests](../tier2_tests/property/test_envelope_properties.py) - Tests verifying envelope properties
- [Orchestration Implementation](../tier2_core/orchestration/) - Core envelope creation logic
- [Behavior Constants](../tier2_core/behaviors/constants.py) - Default policies and constants
