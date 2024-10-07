"""Support for BSB-LAN sensors."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import UnitOfTemperature
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import StateType

from . import BSBLanData
from .const import DOMAIN
from .coordinator import BSBLanCoordinatorData
from .entity import BSBLanEntity


@dataclass(frozen=True, kw_only=True)
class BSBLanSensorEntityDescription(SensorEntityDescription):
    """Describes BSB-LAN sensor entity."""

    value_fn: Callable[[BSBLanCoordinatorData], StateType]

# pylint: disable=E1123
SENSOR_TYPES: tuple[BSBLanSensorEntityDescription, ...] = (
    BSBLanSensorEntityDescription(
        key="current_temperature",
        translation_key="current_temperature",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda data: data.sensor.current_temperature.value,
    ),
    BSBLanSensorEntityDescription(
        key="outside_temperature",
        translation_key="outside_temperature",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda data: data.sensor.outside_temperature.value,
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up BSB-LAN sensor based on a config entry."""
    data: BSBLanData = hass.data[DOMAIN][entry.entry_id]
    async_add_entities(BSBLanSensor(data, description) for description in SENSOR_TYPES)


class BSBLanSensor(BSBLanEntity, SensorEntity):
    """Defines a BSB-LAN sensor."""

    entity_description: BSBLanSensorEntityDescription

    def __init__(
        self,
        data: BSBLanData,
        description: BSBLanSensorEntityDescription,
    ) -> None:
        """Initialize BSB-LAN sensor."""
        super().__init__(data.coordinator, data)
        self.entity_description = description
        self._attr_unique_id = f"{data.device.MAC}-{description.key}"

    @property
    def native_value(self) -> StateType:
        """Return the state of the sensor."""
        value = self.entity_description.value_fn(self.coordinator.data)
        if value == "---":
            return None
        return value
