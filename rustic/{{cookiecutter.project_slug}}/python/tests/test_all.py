import pytest
import {{cookiecutter.project_slug}}


def test_sum_as_string():
    assert {{cookiecutter.project_slug}}.sum_as_string(1, 1) == "2"
