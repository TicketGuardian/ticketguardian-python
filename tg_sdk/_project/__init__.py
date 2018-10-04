import os

DEFAULT_ENV_NAME = '.env'
DEFAULT_ENV_PATH = "./{}".format(DEFAULT_ENV_NAME)

if os.path.exists(DEFAULT_ENV_PATH):
    with open(DEFAULT_ENV_PATH) as f:
        for line in f:
            if line == '\n' or line[0] == '#':
                continue
            key, value = line.rstrip().split('=')
            if os.environ.get(key) is None:
                os.environ.setdefault(key, value)
