# Water Pulse Meter

**Convert a cumulative water-meter pulse sensor into calibrated liters in Home Assistant.**

Many DIY water meters expose a pulse counter rather than a volume. This integration applies a configurable liters-per-pulse factor to the cumulative count, without sending data anywhere.

## Features

- Total water volume in liters, marked as a monotonically increasing total for Home Assistant statistics.
- The configured factor is applied to the source's cumulative pulse count plus the starting offset.

## Install with HACS

1. In Home Assistant, open **HACS → Integrations**.
2. Add `https://github.com/CodeArcade-ctrl/water-pulse-meter` as a custom repository of type **Integration**.
3. Install **Water Pulse Meter** and restart Home Assistant.
4. Open **Settings → Devices & services → Add integration** and select **Water Pulse Meter**.

The catalog request is pending review. Until it is accepted, users must add this repository as a custom repository.

## Privacy and limitations

All calculations run locally in Home Assistant. The integration reads only the selected entities and makes no external network requests. Inputs must have valid numeric states; derived values are unavailable while source values are unknown or invalid.

## License

MIT. See [LICENSE](LICENSE).
