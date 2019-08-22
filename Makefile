# Constants

PROJECT := extract-py

# Targets
# ----------
.PHONY: help
help:  # Show this help.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

poetry.lock: pyproject.toml
	poetry config "settings.virtualenvs.in-project" true
	poetry install

.PHONY: install
install: poetry.lock  # Create virtual environment
	@:

.PHONY: run
run: install  # Run development server for the Flask application.
	FLASK_APP=extract/ FLASK_ENV=development poetry run flask run

.PHONY: shell
shell: install  # Run development shell for the Flask application.
	FLASK_APP=extract FLASK_ENV=development poetry run flask shell

.PHONY: init
init: install  # Create migrations directory.
	FLASK_APP=extract FLASK_ENV=development poetry run flask db init

.PHONY: migrate
migrate: install    # Make a database migration.
    FLASK_APP=extract FLASK_ENV=development poetry run flask db migrate

.PHONY: upgrade
upgrade: install  # Upgrade database to a later version.
	FLASK_APP=extract FLASK_ENV=development poetry run flask db upgrade