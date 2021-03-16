import logging
import logging.config
import pathlib
# TODO ask about that method

log_config_path = str(pathlib.Path(__file__).parent.absolute()) + "\\log.conf"
logging.config.fileConfig(fname=log_config_path, disable_existing_loggers=False)

logger = logging.getLogger('appLogger')

# short_format = logging.Formatter("%(levelname)5s%(filename)s:%(lineno)s - %(funcName)10s() %(message)s")
# detailed_format = logging.Formatter('%(asctime)s %(levelname)5s %(filename)s:%(lineno)s - %(funcName)10s() %(message)s')

# # Console handler
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.WARNING)
# console_handler.setFormatter(short_format)


# path = str(pathlib.Path(__file__).parent.absolute()) + "\\file.log"
# # File handler
# file_handler = logging.FileHandler(path)
# file_handler.setLevel(logging.DEBUG)
# file_handler.setFormatter(detailed_format)


# logger = logging.getLogger('MY_APP')
# logger.setLevel(level = logging.DEBUG)
# logger.addHandler(console_handler)
# logger.addHandler(file_handler)
