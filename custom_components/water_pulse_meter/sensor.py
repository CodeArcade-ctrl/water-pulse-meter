"""Sensor entities for Water Pulse Meter."""
from __future__ import annotations
from homeassistant.components.sensor import SensorEntity, SensorDeviceClass, SensorStateClass
from homeassistant.const import UnitOfTemperature, UnitOfTime, UnitOfVolume, UnitOfPower, PERCENTAGE
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN

DESCRIPTIONS = [("volume", "Total water", SensorDeviceClass.WATER, UnitOfVolume.LITERS, SensorStateClass.TOTAL_INCREASING)]

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([DerivedSensor(coordinator, entry, key, title, device_class, unit, state_class)
        for key, title, device_class, unit, state_class in DESCRIPTIONS])

class DerivedSensor(CoordinatorEntity, SensorEntity):
    """Expose one calculated value."""
    _attr_has_entity_name = True
    def __init__(self, coordinator, entry, key, title, device_class, unit, state_class):
        super().__init__(coordinator)
        self.key = key
        self._attr_name = title
        self._attr_unique_id = f"{entry.entry_id}_{key}"
        self._attr_device_class = device_class
        self._attr_native_unit_of_measurement = unit
        self._attr_state_class = state_class
        self._attr_device_info = {"identifiers": {(DOMAIN, entry.entry_id)}, "name": "Water Pulse Meter", "manufacturer": "CodeArcade-ctrl"}
    @property
    def native_value(self):
        return self.coordinator.data.get(self.key)
