"""Set up the Water Pulse Meter integration."""
from __future__ import annotations
from datetime import timedelta
import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from .const import DOMAIN
from .engine import calculate

PLATFORMS = ['sensor']
_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up a configured instance."""
    async def async_update_data():
        raw = {key: hass.states.get(entry.data[key]) for key in ['pulse_entity']}
        values = {key: state.state if state is not None else None for key, state in raw.items()}
        units = {key: state.attributes.get("unit_of_measurement") if state else None for key, state in raw.items()}
        return calculate(entry.data, values, units)

    coordinator = DataUpdateCoordinator(
        hass, _LOGGER, name=DOMAIN, update_method=async_update_data,
        update_interval=timedelta(seconds=30),
    )
    await coordinator.async_config_entry_first_refresh()
    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = coordinator
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a configured instance."""
    if not await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        return False
    hass.data[DOMAIN].pop(entry.entry_id)
    return True

