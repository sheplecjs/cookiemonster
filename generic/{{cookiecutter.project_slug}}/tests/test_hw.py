import hello_world
from hypothesis import given, strategies, example
from tests.utils import log_cli
import pytest


@pytest.mark.unit
def test_hw() -> None:
	"""Check that cli behavior works as expected without a value arg."""
	status, out = log_cli("python src/hello_world.py")
	assert status.returncode == 0
	assert "Hello, World!" in out


@pytest.mark.unit
def test_hw_value() -> None:
	"""Check that cli behavior works as expected with a value arg."""
	status, out = log_cli("python src/hello_world.py --value Alice")
	assert status.returncode == 0
	assert "Hello, Alice!" in out


@pytest.mark.property
@given(value=strategies.text(max_size=50))
@example(value="Bob")
def test_hw_values(value: str) -> None:
	assert hello_world.main(value) == f"Hello, {value}!"
