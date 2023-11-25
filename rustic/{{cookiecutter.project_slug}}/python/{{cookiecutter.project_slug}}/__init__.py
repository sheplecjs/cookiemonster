from .{{cookiecutter.project_slug}} import *


__doc__ = {{cookiecutter.project_slug}}.__doc__
if hasattr({{cookiecutter.project_slug}}, "__all__"):
    __all__ = {{cookiecutter.project_slug}}.__all__
