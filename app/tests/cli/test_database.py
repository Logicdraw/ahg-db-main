import click

from click.testing import CliRunner


# from cli.commands.cmd_database import (
# 	init_dev,
# 	init_testing,
# 	reset_dev,
# 	reset_testing,
# 	drop_dev,
# 	drop_testing,
# )


import pytest


# import mock



# def test_init_dev():
# 	# initialize dev

# 	runner = CliRunner()

# 	result = runner.invoke(init_dev, input="y\n")

# 	assert result.exit_code == 0
# 	assert not result.exception
# 	assert result.output == 'DONE'

# 	result = runner.invoke(init_dev, input="\n")

# 	assert result.exit_code == 0
# 	assert not result.exception
# 	assert result.output == 'DONE'

# 	with pytest.raises(click.Abort) as err_info:
# 		result = runner.invoke(init_dev, input="n\n")



# def test_init_testing():
# 	# initialize testing

# 	runner = CliRunner()

# 	result = runner.invoke(init_testing, input="y\n")

# 	assert result.exit_code == 0
# 	assert not result.exception
# 	assert result.output == 'DONE'

# 	result = runner.invoke(init_testing, input="\n")

# 	assert result.exit_code == 0
# 	assert not result.exception
# 	assert result.output == 'DONE'

# 	with pytest.raises(click.Abort) as err_info:
# 		result = runner.invoke(init_testing, input="n\n")



# def test_reset_dev():
# 	# reset dev

# 	runner = CliRunner()

# 	result = runner.invoke(reset_dev, input="y\n")

# 	assert result.exit_code == 0
# 	assert not result.exception
# 	assert result.output == 'DONE'

# 	result = runner.invoke(reset_dev, input="\n")

# 	assert result.exit_code == 0
# 	assert not result.exception
# 	assert result.output == 'DONE'

# 	with pytest.raises(click.Abort) as err_info:
# 		result = runner.invoke(reset_dev, input="n\n")



# def test_reset_testing():
# 	# reset testing

# 	runner = CliRunner()

# 	result = runner.invoke(reset_testing, input="y\n")

# 	assert result.exit_code == 0
# 	assert not result.exception
# 	assert result.output == 'DONE'

# 	result = runner.invoke(reset_testing, input="\n")

# 	assert result.exit_code == 0
# 	assert not result.exception
# 	assert result.output == 'DONE'

# 	with pytest.raises(click.Abort) as err_info:
# 		result = runner.invoke(reset_testing, input="n\n")




# def test_drop_dev():
# 	# drop dev

# 	runner = CliRunner()

# 	result = runner.invoke(drop_dev, input="y\n")

# 	assert result.exit_code == 0
# 	assert not result.exception
# 	assert result.output == 'DONE'

# 	result = runner.invoke(drop_dev, input="\n")

# 	assert result.exit_code == 0
# 	assert not result.exception
# 	assert result.output == 'DONE'

# 	with pytest.raises(click.Abort) as err_info:
# 		result = runner.invoke(drop_dev, input="n\n")



# def test_drop_testing():
# 	# drop testing

# 	runner = CliRunner()
	
# 	result = runner.invoke(drop_testing, input="y\n")

# 	assert result.exit_code == 0
# 	assert not result.exception
# 	assert result.output == 'DONE'

# 	result = runner.invoke(drop_testing, input="\n")

# 	assert result.exit_code == 0
# 	assert not result.exception
# 	assert result.output == 'DONE'

# 	with pytest.raises(click.Abort) as err_info:
# 		result = runner.invoke(drop_testing, input="n\n")


