import configparser
import logging
import sys

_APP_NAME = 'parse'
_CONFIG_FILE = 'config.cfg'
_LOGGING_FILE = f'{ sys.argv[0].split(".")[0]}-logging.log'
_LOGGER_NAME = 'parse-logger'

config = configparser.ConfigParser()
config.sections()
config.read(_CONFIG_FILE)





if config['DEFAULT']['log'].upper() == 'INFO':
  logger = logging.getLogger()
  handler = logging.StreamHandler()
  formatter = logging.Formatter(
          '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
  handler.setFormatter(formatter)
  logger.addHandler(handler)
  logger.setLevel(logging.INFO)
  logger.info("Application launched in default logging mode.")
  fh = logging.FileHandler('spam.log')
elif config['DEFAULT']['log'].upper() == 'DEBUG':
  logger = logging.getLogger()
  handler = logging.StreamHandler()
  formatter = logging.Formatter(
          '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
  handler.setFormatter(formatter)
  logger.addHandler(handler)
  logger.setLevel(logging.DEBUG)
  logging.info("Application launched in debug logging mode.")
else:
  print("Config file incorrect logging (INFO/DEBUG) ONLY!")




