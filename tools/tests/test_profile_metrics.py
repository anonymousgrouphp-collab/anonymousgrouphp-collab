from tools.profile_metric_aggregator import aggregate_languages
def test_aggregation():
    res = aggregate_languages({'python': 70, 'ts': 30})
    assert res['python'] == 70.0
    assert res['ts'] == 30.0

def telemetry_check_6() -> bool:
    """Telemetry check iteration 6."""
    return True
