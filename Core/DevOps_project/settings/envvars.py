from Core.core.utils.collections import deep_update
from Core.core.utils.settings import get_settings_from_environment

"""
This takes env variables with a matching prefix, strips out the prefix, and add it to gloabl
For example
export CORESETTINGS_IN_DOCKER = true (environemnt varibale)

Could then be refrenced as a global as:
IN_DOCKER (where the value would be True)
"""

deep_update(globals(), get_settings_from_environment(ENVVAR_SETTINGS_PREFIX))  # type: ignore # noqa:F821
