import os

ENV_PATH = "./.env"
CRD_PATH = "./credentials"

for path in [ENV_PATH, CRD_PATH]:
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                if line == '\n' or line[0] == '#':
                    continue

                if line.count('=') == 1:
                    # .env should just be used to set public and secret keys
                    # for testing.
                    key, value = line.rstrip().split('=')
                    os.environ.setdefault(key, value)
