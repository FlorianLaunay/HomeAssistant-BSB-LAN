# HomeAssistant - BSB-LAN

Custom component to add your [BSB-LAN](https://github.com/fredlcore/BSB-LAN) device into Home Assistant.

It's a fork from the official [BSB-Lan integration](https://www.home-assistant.io/integrations/bsblan).

## Installation

Copy contents of `custom_components/bsb_lan/` to `custom_components/bsb_lan/` in your Home Assistant config folder.

## Installation using HACS

HACS is a community store for Home Assistant. You can install [HACS](https://github.com/custom-components/hacs), add the custom repository `https://github.com/FlorianLaunay/HomeAssistant-BSB-LAN` (with `Integration` type) and then install `BSB-LAN`

## Usage

Add your device via Integrations (search for BSB-LAN) in Home Assistant UI. You can also simply click the button below if you have MyHomeAssistant redirects set up.

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=bsb_lan)

## Have a comment or a suggestion?

Please [open a new issue](https://github.com/FlorianLaunay/HomeAssistant-BSB-LAN/issues)

## Special thanks

- [Frederik Holst](https://github.com/fredlcore) for its awesome work on [BSB-LAN](https://github.com/fredlcore/BSB-LAN)
- [Willem-Jan van Rootselaar](https://github.com/liudger) for its Python library [python-bsblan](https://github.com/liudger/python-bsblan)

# Disclaimer

This integration is using a forked version of the python module `python-bsblan` which is an unofficial module for achieving interoperability with a [BSB-LAN](https://github.com/fredlcore/BSB-LAN) device.

Author is in no way affiliated with the manufacturer of your heating system.

All the api requests used within the `bsblan` library are available and published on the [BSB-LAN Github repository](https://github.com/fredlcore/BSB-LAN) (specification [is here](https://github.com/fredlcore/BSB-LAN/blob/master/openapi.yaml)) and the `bsblan` module is purely just a wrapper around those https requests.

Author does not guarantee functionality of this integration and is not responsible for any damage.

All product names, trademarks and registered trademarks in this repository, are property of their respective owners.
