import logging

from service.logs import GelfFormatter
from service.config import (
    update_defaults,
    get_config,
)

from service.default_config import ENV_VARS


def _create_service_logger():
    config = get_config()
    log_level = getattr(logging, config['LOG_LEVEL'].upper(), logging.INFO)
    logger = logging.getLogger(__name__)
    if config['LOG_FILE'] is not None:
        fh = logging.FileHandler(config['LOG_FILE'])
    else:
        fh = logging.StreamHandler()
    fh.setFormatter(GelfFormatter())
    fh.setLevel(log_level)
    logger.setLevel(log_level)
    logger.addHandler(fh)
    return logger


update_defaults(ENV_VARS)
logger = _create_service_logger()
