"""Implementation of a daikin one+ thermostat."""
import logging

from homeassistant.components.climate import ClimateDevice
from homeassistant.components.climate.const import (
    SUPPORT_AUX_HEAT,
    SUPPORT_FAN_MODE,
    SUPPORT_PRESET_MODE,
    SUPPORT_TARGET_TEMPERATURE,
    SUPPORT_TARGET_TEMPERATURE_RANGE,
)

SUPPORT_FLAGS = (
    SUPPORT_TARGET_TEMPERATURE
    | SUPPORT_PRESET_MODE
    | SUPPORT_AUX_HEAT
    | SUPPORT_TARGET_TEMPERATURE_RANGE
    | SUPPORT_FAN_MODE
)

_LOGGER = logging.getLogger(__name__)


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the Daikin Skyport Thermostat Platform."""
    _LOGGER.debug("Daikin Climate Platform setup_platform")
    _LOGGER.debug("config: %s", config)
    if discovery_info is None:
        return


async def async_setup_entry(hass, entry, async_add_entities):
    """Set up the Nest climate device based on a config entry."""
    temp_unit = hass.config.units.temperature_unit
    _LOGGER.debug("Daikin Climate Platform async_setup_entry")
    _LOGGER.debug("entry: %s", entry)
    _LOGGER.debug("temp_unit: %s", temp_unit)

    # thermostats = await hass.async_add_job(hass.data[DATA_NEST].thermostats)

    all_devices = [
        # Thermostat(structure, device, temp_unit)
        # for structure, device in thermostats
    ]

    async_add_entities(all_devices, True)


class DaikinOneThermostat(ClimateDevice):
    """A thermostat class for Daikin Skyport Thermostats."""

    def __init__(self, data, thermostat_index):
        """Initialize the thermostat."""
        self.data = data
        self.thermostat_index = thermostat_index
        _LOGGER.debug("Thermostat init")
        _LOGGER.debug("data: %s", data)
        _LOGGER.debug("thermostat_index: %s", thermostat_index)

    def update(self):
        """Get the latest state from the thermostat."""
        _LOGGER.debug("Thermostat update")

    @property
    def available(self):
        """Return if device is available."""
        return True  # TBD: Need to determine how to tell if the thermostat is available or not

    @property
    def supported_features(self):
        """Return the list of supported features."""
        return SUPPORT_FLAGS
