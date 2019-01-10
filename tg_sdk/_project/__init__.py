import os

ENV_PATH = "./.env"
CRD_PATH = "./credentials"

for path in [ENV_PATH, CRD_PATH]:
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                if line == '\n' or line[0] == '#':
                    continue
                key, value = line.rstrip().split('=')
                os.environ.setdefault(key, value)
