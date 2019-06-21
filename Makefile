# Constants

PROJECT := extract-py

# Targets
# ----------

.PHONY: install
install: poetry.lock  # Create virtual environment
	@:

PHONY: run
run: install  # Run development server for the Flask application.
	FLASK_APP=extract-py/app.py FLASK_ENV=development poetry run flask run

PHONY: shell
shell: install  # Run development shell for the Flask application.
	FLASK_APP=extract-py/app.py FLASK_ENV=development poetry run flask shell