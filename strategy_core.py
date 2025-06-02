import json

def analyze_webhook(data):
    try:
        parsed = json.loads(data)
        price = float(parsed.get("price", 0))
        trend = parsed.get("trend", "").lower()
        zone = parsed.get("zone", "").lower()

        if trend == "breakout" and "shadow" in zone:
            return f"Breakout in Shadow Zone at {price}"
        return None
    except Exception as e:
        return None