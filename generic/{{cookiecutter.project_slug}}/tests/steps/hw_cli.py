from tests.utils import log_cli


@when('we run command "{command}"')  # noqa: F821
def step_impl(context, command):
	context.status, context.output = log_cli(command)


@then('output has "{expected_output}"')  # noqa: F821
def step_impl(context, expected_output):  # noqa: F811
	assert context.status.returncode == 0
	assert expected_output in context.output
