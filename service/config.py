"""
Get current environment values from a defined collection of variables
"""

import os

INITIALIZED = False  # pragma: no mutate
DEFAULTS = {}


def update_defaults(defaults):
    '''
    Updates the default values. This needs to be called at least once for this
    module to be useful.
    '''
    global INITIALIZED

    DEFAULTS.update(defaults)
    INITIALIZED = True


def _check_initialized():
    if not INITIALIZED:
        raise RuntimeError(
            'update_defaults() must be called before get_config() or get_config_list().'
        )


def _get_value(key):
    _check_initialized()
    default_value = DEFAULTS[key]
    value = os.getenv(key, default_value)

    # empty string, use default value
    if value == '':
        value = default_value
    if isinstance(DEFAULTS[key], bool) and not isinstance(value, bool):
        if value.upper() != 'FALSE':
            value = True
        else:
            value = False
    elif isinstance(DEFAULTS[key], int) and not isinstance(value, int):
        try:
            value = int(value)
        except ValueError:
            value = 0
    return value


def get_config(single_key=None):
    '''
    Returns the value of a single key or, if no key is given, a dict of all keys
    and their values.
    '''
    _check_initialized()
    if single_key:
        return _get_value(single_key)
    else:
        return {k: _get_value(k) for k in DEFAULTS}


def get_config_list(key):
    '''
    Return a list of values from the comma-separated string corresponding to
    key.
    '''
    _check_initialized()
    return [x.strip() for x in _get_value(key).split(',')]
