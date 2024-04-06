.DEFAULT_GOAL := help

PROJECT_NAME ?= {{ cookiecutter.project_slug }}

## Run all code quality rules
all: lint format

## Lint all files with ruff
lint:
	@pre-commit run --all-files ruff

## Format all files with ruff
format:
	@pre-commit run --all-files ruff-format

{% if cookiecutter.project_base_deps == "django/psycopg" -%}
## Create DB migrations
makemigrations:
	@python manage.py makemigrations

## Create DB migrations and migrate
migrate: makemigrations
	@python manage.py migrate

## Run dev server
runserver:
	@python manage.py runserver
{%- endif %}

## Update deps txt files
update_deps:
	@pip-compile --extra test -o requirements.txt
	@pip-compile --all-extras -o requirements-dev.txt

test:
	@tox

## This help screen
help:
	@printf "Available targets:\n\n"
	@awk '/^[a-zA-Z\-\_0-9%:\\]+/ { \
		helpMessage = match(lastLine, /^## (.*)/); \
		if (helpMessage) { \
		helpCommand = $$1; \
		helpMessage = substr(lastLine, RSTART + 3, RLENGTH); \
	gsub("\\\\", "", helpCommand); \
	gsub(":+$$", "", helpCommand); \
		printf "  \x1b[32;01m%-35s\x1b[0m %s\n", helpCommand, helpMessage; \
		} \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST) | sort -u
	@printf "\n"