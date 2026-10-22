"""Convert a monotonic pulse count to water volume."""
from __future__ import annotations

def calculate(config, values, units):
    try:
        pulses = float(values["pulse_entity"])
        factor = float(config["liters_per_pulse"])
        offset = float(config["starting_liters"])
        if pulses < 0 or factor <= 0 or offset < 0:
            raise ValueError("invalid meter values")
        return {"volume": round(offset + pulses * factor, 3)}
    except (TypeError, ValueError, OverflowError):
        return {"volume": None}
