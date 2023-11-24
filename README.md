# Cookiemonster

## Description

This is an isolated cookiecutter environment for generating pre-configured directories for projects. To operate, run as a dev container. 

## Structure

```bash
.
├── Dockerfile
├── Makefile
├── README.md
├── generic
│   ├── cookiecutter.json
│   └── {{cookiecutter.project_slug}}
│       ├── Dockerfile
│       ├── LICENSE
│       ├── Makefile
│       ├── README.md
│       ├── pyproject.toml
│       └── requirements.txt
└── requirements.txt
```
