# QRCode and Barcode Reader

Pre Reqs

sudo apt-get install zbar-tools

poetry config virtualenvs.in-project true

Activate env

```sh
# activate venv
poetry shell
# dev dependencies
poetry add pytest mypy pyright flake8 autopep8 pylint tox isort black flake8-bandit flake8-docstrings flake8-bugbear jupyter autoflake  --group dev
# organize imports and format code
poetry run autoflake --expand-star-imports --remove-all-unused-imports --remove-duplicate-keys --remove-unused-variables --recursive --in-place .  && poetry run isort . && poetry run black .
# test
poetry run coverage run -m pytest && poetry run coverage report -m






```