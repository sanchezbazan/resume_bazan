from resume_core.general.utils.cus_collections import deep_update
from resume_core.general.utils.cus_settings import get_settings_from_environment

deep_update(globals(), get_settings_from_environment(ENVVAR_SETTINGS_PREFIX))  # type: ignore # noqa: F821