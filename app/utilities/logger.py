import logging
import logging.config
import pathlib
import os

logging_conf_path = os.path.join(os.path.dirname(__file__), '../config/log.conf')
logging.config.fileConfig(fname=logging_conf_path, disable_existing_loggers=False)

logger = logging.getLogger('appLogger')

