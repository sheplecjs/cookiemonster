.DEFAULT_GOAL := help

RED = \033[0;31m
GREEN = \033[0;32m
YELLOW = \033[1;33m
BLUE = \033[0;34m
NO_COLOR = \033[0m

PROJECT_NAME ?= {{ cookiecutter.project_slug }}

## Run all code quality rules
all: lint format

## Lint all files with ruff
lint:
	@pre-commit run --all-files ruff

## Format all files with ruff
format:
	@pre-commit run --all-files ruff-format

## Start jupyterlab server
lab:
	@jupyter lab --allow-root

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