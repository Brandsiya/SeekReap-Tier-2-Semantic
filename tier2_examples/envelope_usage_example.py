"""
REAL-WORLD EXAMPLE: Semantic Envelope Usage Patterns

PURPOSE: Demonstrate realistic usage of tier2 orchestration envelopes
STATUS: Working examples with production-like patterns
TIER-2 CONFORMANCE: Shows proper semantic envelope patterns
"""

import json
import time
from tier2_core.orchestration import orchestrate, validate_semantic_policy


def example_basic_envelope_creation():
    """
    Example 1: Basic envelope creation with different payload types.
    
    Demonstrates:
    - Creating envelopes with various payload types
    - Metadata handling
    - Basic validation
    """
    print("=== EXAMPLE 1: Basic Envelope Creation ===")
    print()
    
    # Example 1a: Simple string payload
    simple_string = "Hello, Tier-2 World!"
    envelope1 = orchestrate(simple_string)
    print(f"1a. String envelope:")
    print(f"    ID: {envelope1['id']}")
    print(f"    Payload: {envelope1['payload']}")
    print(f"    Valid: {validate_semantic_policy(envelope1)}")
    print()
    
    # Example 1b: JSON-like dictionary payload
    json_payload = {
        "event": "user_login",
        "user_id": "usr_12345",
        "timestamp": time.time(),
        "metadata": {
            "browser": "Chrome/120.0",
            "ip_address": "192.168.1.100"
        }
    }
    envelope2 = orchestrate(json_payload)
    print(f"1b. JSON envelope:")
    print(f"    ID: {envelope2['id']}")
    print(f"    Event: {envelope2['payload']['event']}")
    print(f"    User: {envelope2['payload']['user_id']}")
    print(f"    Valid: {validate_semantic_policy(envelope2)}")
    print()
    
    # Example 1c: With metadata
    sensor_data = {
        "temperature": 22.5,
        "humidity": 65,
        "location": "server_room_a"
    }
    sensor_metadata = {
        "sensor_id": "temp_sensor_001",
        "unit": "celsius",
        "calibration_date": "2024-01-15",
        "tags": ["environment", "monitoring", "critical"]
    }
    envelope3 = orchestrate(sensor_data, sensor_metadata)
    print(f"1c. Sensor data with metadata:")
    print(f"    ID: {envelope3['id']}")
    print(f"    Temperature: {envelope3['payload']['temperature']}°C")
    print(f"    Sensor: {envelope3['metadata']['sensor_id']}")
    print(f"    Tags: {envelope3['metadata']['tags']}")
    print(f"    Valid: {validate_semantic_policy(envelope3)}")
    print()


def example_workflow_composition():
    """
    Example 2: Workflow composition with multiple envelopes.
    
    Demonstrates:
    - Creating workflow chains
    - Referencing previous envelopes
    - Maintaining causality
    """
    print("=== EXAMPLE 2: Workflow Composition ===")
    print()
    
    # Simulate a user registration workflow
    workflow_envelopes = []
    
    # Step 1: User submits registration
    registration_data = {
        "step": "registration_submit",
        "email": "user@example.com",
        "username": "newuser123",
        "timestamp": time.time()
    }
    reg_envelope = orchestrate(registration_data)
    workflow_envelopes.append(reg_envelope)
    print(f"2a. Registration submitted:")
    print(f"    Envelope ID: {reg_envelope['id']}")
    print(f"    Username: {reg_envelope['payload']['username']}")
    print()
    
    # Step 2: Validate email (simulated async step)
    validation_data = {
        "step": "email_validation",
        "original_envelope_id": reg_envelope['id'],
        "validation_result": "success",
        "validation_timestamp": time.time(),
        "details": {
            "email_sent": True,
            "email_verified": True
        }
    }
    validation_metadata = {
        "workflow_step": 2,
        "depends_on": reg_envelope['id'],
        "timeout_seconds": 300
    }
    validation_envelope = orchestrate(validation_data, validation_metadata)
    workflow_envelopes.append(validation_envelope)
    print(f"2b. Email validation completed:")
    print(f"    Envelope ID: {validation_envelope['id']}")
    print(f"    Depends on: {validation_envelope['metadata']['depends_on']}")
    print(f"    Result: {validation_envelope['payload']['validation_result']}")
    print()
    
    # Step 3: Create user profile
    profile_data = {
        "step": "profile_creation",
        "original_envelope_id": reg_envelope['id'],
        "user_id": "usr_" + reg_envelope['id'].split('-')[-1][:8],
        "profile_data": {
            "display_name": "New User",
            "preferences": {"theme": "dark", "language": "en"},
            "account_type": "standard"
        }
    }
    profile_metadata = {
        "workflow_step": 3,
        "depends_on": [reg_envelope['id'], validation_envelope['id']],
        "permissions": ["read_profile", "write_profile"]
    }
    profile_envelope = orchestrate(profile_data, profile_metadata)
    workflow_envelopes.append(profile_envelope)
    print(f"2c. Profile created:")
    print(f"    Envelope ID: {profile_envelope['id']}")
    print(f"    User ID: {profile_envelope['payload']['user_id']}")
    print(f"    Dependencies: {len(profile_envelope['metadata']['depends_on'])} envelopes")
    print()
    
    # Validate entire workflow
    print(f"2d. Workflow validation:")
    valid_count = sum(1 for env in workflow_envelopes if validate_semantic_policy(env))
    print(f"    Total envelopes: {len(workflow_envelopes)}")
    print(f"    Valid envelopes: {valid_count}")
    print(f"    Workflow complete: {valid_count == len(workflow_envelopes)}")
    print()


def example_data_pipeline():
    """
    Example 3: Data processing pipeline with envelopes.
    
    Demonstrates:
    - Data transformation chains
    - Audit trail maintenance
    - Pipeline state management
    """
    print("=== EXAMPLE 3: Data Processing Pipeline ===")
    print()
    
    # Simulate a data processing pipeline
    raw_data = {
        "source": "api_gateway",
        "records": [
            {"id": 1, "value": 100, "timestamp": time.time() - 3600},
            {"id": 2, "value": 200, "timestamp": time.time() - 1800},
            {"id": 3, "value": 300, "timestamp": time.time()}
        ],
        "total_records": 3
    }
    
    # Stage 1: Raw data ingestion
    ingestion_metadata = {
        "pipeline_stage": "ingestion",
        "data_source": "external_api",
        "quality_checks": ["schema_validation", "null_check"]
    }
    ingestion_envelope = orchestrate(raw_data, ingestion_metadata)
    
    # Stage 2: Data transformation
    transformed_data = {
        "source_envelope_id": ingestion_envelope['id'],
        "transformed_records": [
            {
                "original_id": record["id"],
                "processed_value": record["value"] * 2,
                "processing_timestamp": time.time(),
                "anomaly_score": 0.1 if record["value"] > 250 else 0.0
            }
            for record in raw_data["records"]
        ],
        "transformations_applied": ["value_doubling", "anomaly_scoring"]
    }
    transformation_metadata = {
        "pipeline_stage": "transformation",
        "depends_on": ingestion_envelope['id'],
        "transform_version": "1.2.0",
        "processing_time_ms": 45
    }
    transformation_envelope = orchestrate(transformed_data, transformation_metadata)
    
    # Stage 3: Aggregation
    aggregated_data = {
        "source_envelope_ids": [ingestion_envelope['id'], transformation_envelope['id']],
        "aggregations": {
            "total_value": sum(r["value"] for r in raw_data["records"]),
            "average_processed": sum(t["processed_value"] for t in transformed_data["transformed_records"]) / 3,
            "anomaly_count": sum(1 for t in transformed_data["transformed_records"] if t["anomaly_score"] > 0)
        },
        "summary_statistics": {
            "record_count": 3,
            "processing_window_seconds": 3600,
            "data_quality_score": 0.95
        }
    }
    aggregation_metadata = {
        "pipeline_stage": "aggregation",
        "depends_on": [ingestion_envelope['id'], transformation_envelope['id']],
        "aggregation_type": "summary_statistics",
        "serving_ready": True
    }
    aggregation_envelope = orchestrate(aggregated_data, aggregation_metadata)
    
    print(f"3a. Pipeline stages completed:")
    print(f"    Ingestion: {ingestion_envelope['id']}")
    print(f"    Transformation: {transformation_envelope['id']}")
    print(f"    Aggregation: {aggregation_envelope['id']}")
    print()
    
    print(f"3b. Pipeline results:")
    print(f"    Total records processed: {aggregated_data['aggregations']['total_value']}")
    print(f"    Average processed value: {aggregated_data['aggregations']['average_processed']:.2f}")
    print(f"    Anomalies detected: {aggregated_data['aggregations']['anomaly_count']}")
    print(f"    Data quality score: {aggregated_data['summary_statistics']['data_quality_score']}")
    print()
    
    # Validate pipeline integrity
    pipeline_envelopes = [ingestion_envelope, transformation_envelope, aggregation_envelope]
    all_valid = all(validate_semantic_policy(env) for env in pipeline_envelopes)
    
    print(f"3c. Pipeline validation:")
    print(f"    All envelopes valid: {all_valid}")
    print(f"    Pipeline complete: {aggregation_envelope['metadata']['serving_ready']}")
    print()


def example_error_handling_and_recovery():
    """
    Example 4: Error handling and recovery patterns.
    
    Demonstrates:
    - Error envelope creation
    - Recovery workflows
    - Retry patterns with envelopes
    """
    print("=== EXAMPLE 4: Error Handling and Recovery ===")
    print()
    
    # Simulate an error scenario
    error_data = {
        "error_type": "connection_timeout",
        "error_message": "Database connection timeout after 30 seconds",
        "component": "database_connector",
        "timestamp": time.time(),
        "context": {
            "database_host": "db-prod-01",
            "query": "SELECT * FROM users WHERE active = true",
            "retry_count": 3
        }
    }
    
    error_metadata = {
        "severity": "high",
        "recovery_action": "retry_with_backoff",
        "notify_teams": ["database_team", "oncall_engineer"],
        "error_id": "err_" + str(int(time.time()))[-8:]
    }
    
    error_envelope = orchestrate(error_data, error_metadata)
    
    print(f"4a. Error captured:")
    print(f"    Error ID: {error_envelope['metadata']['error_id']}")
    print(f"    Type: {error_envelope['payload']['error_type']}")
    print(f"    Severity: {error_envelope['metadata']['severity']}")
    print(f"    Component: {error_envelope['payload']['component']}")
    print()
    
    # Simulate recovery
    recovery_data = {
        "original_error_id": error_envelope['metadata']['error_id'],
        "recovery_action": "connection_retry",
        "recovery_result": "success",
        "recovery_timestamp": time.time() + 5,
        "new_connection_details": {
            "database_host": "db-prod-02",
            "connection_time_ms": 150,
            "query_completed": True
        }
    }
    
    recovery_metadata = {
        "recovery_strategy": "failover_to_backup",
        "downtime_seconds": 5,
        "data_loss": "none",
        "recovery_validated": True
    }
    
    recovery_envelope = orchestrate(recovery_data, recovery_metadata)
    
    print(f"4b. Recovery completed:")
    print(f"    Original error: {recovery_envelope['payload']['original_error_id']}")
    print(f"    Action: {recovery_envelope['payload']['recovery_action']}")
    print(f"    Result: {recovery_envelope['payload']['recovery_result']}")
    print(f"    Downtime: {recovery_envelope['metadata']['downtime_seconds']} seconds")
    print(f"    Data loss: {recovery_envelope['metadata']['data_loss']}")
    print()


def example_audit_and_compliance():
    """
    Example 5: Audit and compliance logging.
    
    Demonstrates:
    - Audit trail creation
    - Compliance metadata
    - Immutable audit records
    """
    print("=== EXAMPLE 5: Audit and Compliance ===")
    print()
    
    # Simulate a compliance audit event
    audit_data = {
        "event_type": "user_permission_change",
        "user_id": "usr_admin_001",
        "target_user_id": "usr_standard_123",
        "action": "add_permission",
        "permission": "write_sensitive_data",
        "justification": "temporary_access_for_migration",
        "timestamp": time.time(),
        "previous_permissions": ["read_data", "write_basic"],
        "new_permissions": ["read_data", "write_basic", "write_sensitive_data"]
    }
    
    compliance_metadata = {
        "compliance_standard": "GDPR",
        "audit_requirement": "access_logging",
        "retention_period_days": 365 * 7,  # 7 years
        "encryption_level": "aes-256",
        "auditor": "system_automation",
        "review_required": True,
        "review_deadline": time.time() + (7 * 24 * 3600)  # 7 days
    }
    
    audit_envelope = orchestrate(audit_data, compliance_metadata)
    
    print(f"5a. Audit event recorded:")
    print(f"    Envelope ID: {audit_envelope['id']}")
    print(f"    Event: {audit_envelope['payload']['event_type']}")
    print(f"    User: {audit_envelope['payload']['user_id']}")
    print(f"    Action: {audit_envelope['payload']['action']}")
    print()
    
    print(f"5b. Compliance metadata:")
    print(f"    Standard: {audit_envelope['metadata']['compliance_standard']}")
    print(f"    Requirement: {audit_envelope['metadata']['audit_requirement']}")
    print(f"    Retention: {audit_envelope['metadata']['retention_period_days']} days")
    print(f"    Review required: {audit_envelope['metadata']['review_required']}")
    print(f"    Review deadline: {time.ctime(audit_envelope['metadata']['review_deadline'])}")
    print()
    
    # Demonstrate immutability of audit trail
    print(f"5c. Audit trail immutability:")
    print(f"    Envelope signature: {audit_envelope['signature'][:50]}...")
    print(f"    Schema version: {audit_envelope['schema_version']}")
    print(f"    Timestamp: {audit_envelope['timestamp']} ({time.ctime(audit_envelope['timestamp'])})")
    print(f"    Validation: {validate_semantic_policy(audit_envelope)}")
    print()


def main():
    """Run all examples."""
    print("=" * 60)
    print("TIER-2 SEMANTIC ENVELOPE REAL-WORLD EXAMPLES")
    print("=" * 60)
    print()
    
    # Run all examples
    example_basic_envelope_creation()
    example_workflow_composition()
    example_data_pipeline()
    example_error_handling_and_recovery()
    example_audit_and_compliance()
    
    print("=" * 60)
    print("ALL EXAMPLES COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()
