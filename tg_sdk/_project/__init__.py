import os

DEFAULT_ENV_NAME = '.env'
DEFAULT_ENV_PATH = "../../{}".format(DEFAULT_ENV_NAME)

if os.path.exists(DEFAULT_ENV_PATH):
    with open(DEFAULT_ENV_PATH) as f:
        for line in f:
            key, value = line.split('=')
            if os.environ.get(key) is None:
                os.environ.setdefault(key, value)
