import logging
import logging.config
import pathlib


log_config_path = str(pathlib.Path(__file__).parent.absolute()) + "\\log.conf"
logging.config.fileConfig(fname=log_config_path, disable_existing_loggers=False)

logger = logging.getLogger('appLogger')

