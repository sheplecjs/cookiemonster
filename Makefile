.DEFAULT_GOAL := run_dev

RED = \033[0;31m
GREEN = \033[0;32m
YELLOW = \033[1;33m
BLUE = \033[0;34m
NO_COLOR = \033[0m

CONTAINER_ENGINE ?= podman
PROJECT_NAME ?= cookiemonster

run_dev:
		@echo "${YELLOW} Rebuilding dev container:${NO_COLOR}"
		@${CONTAINER_ENGINE} build -t ${PROJECT_NAME} .
		@${CONTAINER_ENGINE} run -it -v ${PWD}:/${PROJECT_NAME} --rm ${PROJECT_NAME} bash