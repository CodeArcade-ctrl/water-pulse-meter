"""Config flow for Water Pulse Meter."""
from __future__ import annotations
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.helpers import selector
from .const import DOMAIN

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Configure an instance from existing Home Assistant sensors."""
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            await self.async_set_unique_id("-".join(str(user_input[key]) for key in ['pulse_entity']))
            self._abort_if_unique_id_configured()
            return self.async_create_entry(title="Water Pulse Meter", data=user_input)
        schema = vol.Schema({
            vol.Required("pulse_entity"): selector.EntitySelector(selector.EntitySelectorConfig(domain=["sensor"])),
            vol.Required("liters_per_pulse", default=1.0): selector.NumberSelector(selector.NumberSelectorConfig(min=0.001 if "liters_per_pulse" in ("liters_per_pulse", "capacity_wh", "capacity_liters") else 0, max=100000000, step=0.1, mode=selector.NumberSelectorMode.BOX)),
            vol.Required("starting_liters", default=0.0): selector.NumberSelector(selector.NumberSelectorConfig(min=0.001 if "starting_liters" in ("liters_per_pulse", "capacity_wh", "capacity_liters") else 0, max=100000000, step=0.1, mode=selector.NumberSelectorMode.BOX)),
        })
        return self.async_show_form(step_id="user", data_schema=schema)

