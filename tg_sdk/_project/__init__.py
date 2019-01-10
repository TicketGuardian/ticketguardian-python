import os

from tg_sdk import constants

ENV_PATH = "./.env"
CRD_PATH = "./credentials"

for path in [ENV_PATH, CRD_PATH]:
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                if line == '\n' or line[0] == '#':
                    continue
                key, value = line.rstrip().split('=')
                setattr(constants, key, value)
