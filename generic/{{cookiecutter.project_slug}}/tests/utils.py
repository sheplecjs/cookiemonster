import subprocess
import shlex
from pathlib import Path
from typing import Tuple


def log_cli(command: str) -> Tuple[str, str]:
	"""Report status code and stdout for a provided command.

	Args:
	    command (str): the command to capture outputs for

	Returns:
	    tuple[str, str]: status code and stdout for the command
	"""
	output_path = Path("output.log")
	with output_path.open("w") as target:
		status = subprocess.run(
			shlex.split(command), check=True, text=True, stdout=target, stderr=subprocess.STDOUT
		)
	output = output_path.read_text()
	output_path.unlink()
	return status, output
