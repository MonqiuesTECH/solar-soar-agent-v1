import codex_sdk

def on_threat_detected(event):
    # Analyze the Sophos telemetry via the CodeX Intelligence Module
    analysis = codex_sdk.analyze(event.telemetry, mode="Autonomous-SOC")
    
    if analysis.score > 0.8:  # If high confidence threat
        print(f"Triggering Remediation Playbook for {event.device_id}")
        codex_sdk.execute_playbook("isolate-compromised-endpoint", target=event.device_id)
        codex_sdk.emit_finding(analysis.report)

# Hooking into the Sentinel Stream defined in the manifest
codex_sdk.subscribe("sentinel_incident_log", on_threat_detected)
