"""Config flow for daikinskyport integration."""
import logging

import voluptuous as vol

from homeassistant import config_entries, core, exceptions
from homeassistant.const import CONF_EMAIL, CONF_PASSWORD

from .const import DOMAIN  # pylint:disable=unused-import

_LOGGER = logging.getLogger(__name__)

# TODO adjust the data schema to the data that you need
DATA_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {vol.Required(CONF_EMAIL): str, vol.Required(CONF_PASSWORD): str}
        )
    }
)


async def validate_input(hass: core.HomeAssistant, data):
    """Validate the user input allows us to connect.

    Data has the keys from DATA_SCHEMA with values provided by the user.
    """
    _LOGGER.warning("daikinskyport validate_input")
    _LOGGER.info("validate_input data: %s", data)
    # TODO validate the data can be used to set up a connection.
    # If you cannot connect:
    # throw ConnectError
    # If the authentication is wrong:
    # InvalidAuth

    # Return some info we want to store in the config entry.
    return {"title": "DaikinOne+ Thermostat"}


class DaikinSkyPortConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for daikinskyport."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    def __init__(self):
        """Initialize the DaikinSkyPort config flow."""
        _LOGGER.debug("DaikinSkyPortConfigFlow init")

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        if user_input is not None:
            try:
                info = await validate_input(self.hass, user_input)

                return self.async_create_entry(title=info["title"], data=user_input)
            except ConnectError:
                errors["base"] = "cannot_connect"
            except InvalidAuth:
                errors["base"] = "invalid_auth"
            except Exception:  # pylint: disable=broad-except
                _LOGGER.exception("Unexpected exception")
                errors["base"] = "unknown"

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {vol.Required("email"): str, vol.Required("password"): str}
            ),
            errors=errors,
        )


class ConnectError(exceptions.HomeAssistantError):
    """Error to indicate we cannot connect."""


class InvalidAuth(exceptions.HomeAssistantError):
    """Error to indicate there is invalid auth."""
