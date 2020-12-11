import platform
from environs import Env
from loguru import logger
from os.path import dirname, abspath, join

env = Env()
env.read_env()

# definition of flags
IS_WINDOWS = platform.system().lower() == 'windows'

# definition of dirs
ROOT_DIR = dirname(dirname(abspath(__file__)))
LOG_DIR = join(ROOT_DIR, env.str('LOG_DIR', 'Logs'))

# log set
logger.add(env.str('LOG_RUNTIME_FILE', join(LOG_DIR, 'runtime.log')), level='DEBUG', rotation='1 week',
           retention='20 days')
logger.add(env.str('LOG_ERROR_FILE', join(LOG_DIR, 'error.log')), level='ERROR', rotation='1 week')
