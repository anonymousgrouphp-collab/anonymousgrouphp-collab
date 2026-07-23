def aggregate_languages(stats: dict) -> dict:
    total = sum(stats.values())
    return {k: round((v/total)*100, 2) for k, v in stats.items()} if total else {}
