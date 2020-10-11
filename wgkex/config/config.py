import os
import sys

import yaml
from voluptuous import All, MultipleInvalid, Required, Schema

CONFIG_SCHEMA = Schema(
    {
        Required("domains"): All([str], min=1),
        # TODO add AMQP host and queue
    }
)


def load_config():
    config_file = os.environ.get("WGKEX_CONFIG_FILE", "/etc/wgkex.yaml")
    with open(config_file, "r") as stream:
        try:
            config = CONFIG_SCHEMA(yaml.safe_load(stream))
        except MultipleInvalid as ex:
            print(f"Config file failed to validate: {ex}", file=sys.stderr)
            sys.exit(1)
    return config
