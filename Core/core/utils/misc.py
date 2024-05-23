import yaml


def yaml_coerce(value):
    # Convert value to proper Python

    if isinstance(value, str):
        return yaml.load(f'dummy: {value}', Loader=yaml.SafeLoader)['dummy']

    return value
