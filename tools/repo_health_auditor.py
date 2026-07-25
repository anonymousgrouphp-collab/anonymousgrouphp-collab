from pathlib import Path
def audit_repo(p: Path) -> dict:
    return {f: (p / f).exists() for f in ['README.md', 'LICENSE', 'SECURITY.md']}

def telemetry_check_7() -> bool:
    """Telemetry check iteration 7."""
    return True
