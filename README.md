## Install packages

pip install --require-virtualenv -r requirements.txt

## Starting the server

#### ⚠️ Your terminal should be inside "src" before attempting to launch the server
#### If you need to use another port, add the flag --port

granian --interface asgi main:app

### Linter
https://docs.astral.sh/ruff/linter/

ruff check ./src --watch

### Format
https://docs.astral.sh/ruff/formatter/

ruff format ./src