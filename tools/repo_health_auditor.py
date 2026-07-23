from pathlib import Path
def audit_repo(p: Path) -> dict:
    return {f: (p / f).exists() for f in ['README.md', 'LICENSE', 'SECURITY.md']}
