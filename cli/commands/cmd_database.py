import asyncio


import click


import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)




# PSQL --

from main.database.psql.dev.session import (
	# SessionPSQLDev,
	engine_psql_dev,
)

from main.database.psql.testing.session import (
	# SessionPSQLTesting,
	engine_psql_testing,
)

from main.database.psql.prod.session import (
	# SessionPSQLProd,
	engine_psql_prod,
)


from main.database.psql.helpers import (
	init_psql_db,
	drop_psql_db,
	reset_psql_db,
)


# PSQL ASYNC

from main.database.psql_async.dev.session import (
	# SessionPSQLAsyncDev,
	engine_psql_async_dev,
)

from main.database.psql_async.testing.session import (
	# SessionPSQLAsyncTesting,
	engine_psql_async_testing,
)

from main.database.psql_async.prod.session import (
	# SessionPSQLAsyncProd,
	engine_psql_async_prod,
)


from main.database.psql_async.helpers import (
	init_psql_async_db,
	drop_psql_async_db,
	reset_psql_async_db,
	create_first_superadmin_psql_async_db,
	create_first_admin_psql_async_db,
	create_first_coach_psql_async_db,
	create_first_guardian_psql_async_db,
	create_first_adult_rep_psql_async_db,
)




from main.config import settings




@click.group()
def cli():
	""" Run PostgreSQL related tasks. """
	pass





# Initialize


@click.command()
@click.confirmation_option(prompt='Are you sure you wish to initialize the PSQL TESTING database?')
def init_psql_testing() -> None:
	# Initialize DB

	logger.info('Initializing PSQL TESTING database!')

	init_psql_db(
		engine_psql=engine_psql_testing,
	)


	logger.info('Finished initializing PSQL TESTING database!')

	click.echo(f'DONE')

	return None


@click.command()
@click.confirmation_option(prompt='Are you sure you wish to initialize the PSQL DEV database?')
def init_psql_dev() -> None:
	# Initialize DB

	logger.info('Initializing PSQL DEV database!')


	init_psql_db(
		engine_psql=engine_psql_dev,
	)

	logger.info('Finished initializing PSQL DEV database!')

	click.echo(f'DONE')

	return None


@click.command()
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
@click.confirmation_option(prompt='Are you sure you wish to initialize the PSQL PROD database?')
def init_psql_prod(password) -> None:
	# Initialize DB

	if password != settings.CLI_PASSWORD:
		raise ValueError('Invalid password!')

	logger.info('Initializing PSQL PROD database!')

	init_psql_db(
		engine_psql=engine_psql_prod,
	)

	logger.info('Finished initializing PSQL PROD database!')

	click.echo(f'DONE')

	return None



@click.command()
@click.confirmation_option(prompt='Are you sure you wish to initialize the PSQL (ASYNC) TESTING database?')
def init_psql_async_testing() -> None:
	# Initialize DB

	logger.info('Initializing PSQL (ASYNC) TESTING database!')

	asyncio.run(init_psql_async_db(engine_psql_async_testing))

	logger.info('Finished initializing PSQL (ASYNC) TESTING database!')

	click.echo(f'DONE')

	return None


@click.command()
@click.confirmation_option(prompt='Are you sure you wish to initialize the PSQL (ASYNC) DEV database?')
def init_psql_async_dev() -> None:
	# Initialize DB

	logger.info('Initializing PSQL (ASYNC) DEV database!')

	asyncio.run(init_psql_async_db(engine_psql_async_dev))

	logger.info('Finished initializing PSQL (ASYNC) DEV database!')

	click.echo(f'DONE')

	return None


@click.command()
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
@click.confirmation_option(prompt='Are you sure you wish to initialize the PSQL (ASYNC) PROD database?')
def init_psql_async_prod(password) -> None:
	# Initialize DB

	if password != settings.CLI_PASSWORD:
		raise ValueError('Invalid password!')

	logger.info('Initializing PSQL (ASYNC) PROD database!')

	asyncio.run(init_psql_async_db(engine_psql_async_prod))

	logger.info('Finished initializing PSQL (ASYNC) PROD database!')

	click.echo(f'DONE')

	return None




# Reset



@click.command()
@click.confirmation_option(prompt='Are you sure you wish to reset the PSQL TESTING database?')
def reset_psql_testing() -> None:
	# Reset DB

	logger.info('Resetting PSQL TESTING database!')

	reset_psql_db(
		engine_psql=engine_psql_testing,
	)

	logger.info('Finished resetting PSQL TESTING database!')

	click.echo(f'DONE')

	return None


@click.command()
@click.confirmation_option(prompt='Are you sure you wish to reset the PSQL DEV database?')
def reset_psql_dev() -> None:
	# Reset DB

	logger.info('Resetting PSQL DEV database!')

	reset_psql_db(
		engine_psql=engine_psql_dev,
	)

	logger.info('Finished resetting PSQL DEV database!')

	click.echo(f'DONE')

	return None


@click.command()
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
@click.confirmation_option(prompt='Are you sure you wish to reset the PSQL PROD database?')
def reset_psql_prod(password) -> None:
	# Reset DB

	if password != settings.CLI_PASSWORD:
		raise ValueError('Invalid password!')

	logger.info('Resetting PSQL PROD database!')


	reset_psql_db(
		engine_psql=engine_psql_prod,
	)


	logger.info('Finished resetting PSQL PROD database!')

	click.echo(f'DONE')

	return None



@click.command()
@click.confirmation_option(prompt='Are you sure you wish to reset the PSQL (ASYNC) TESTING database?')
def reset_psql_async_testing() -> None:
	# Reset DB

	logger.info('Resetting PSQL (ASYNC) TESTING database!')

	asyncio.run(reset_psql_async_db(engine_psql_async_testing))

	logger.info('Finished resetting PSQL (ASYNC) TESTING database!')

	click.echo(f'DONE')

	return None


@click.command()
@click.confirmation_option(prompt='Are you sure you wish to reset the PSQL DEV database?')
def reset_psql_async_dev() -> None:
	# Reset DB

	logger.info('Resetting PSQL DEV database!')

	asyncio.run(reset_psql_async_db(engine_psql_async_dev))

	logger.info('Finished resetting PSQL DEV database!')

	click.echo(f'DONE')

	return None


@click.command()
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
@click.confirmation_option(prompt='Are you sure you wish to reset the PSQL (ASYNC) PROD database?')
def reset_psql_async_prod(password) -> None:
	# Reset DB

	if password != settings.CLI_PASSWORD:
		raise ValueError('Invalid password!')

	logger.info('Resetting PSQL (ASYNC) PROD database!')

	asyncio.run(reset_psql_async_db(engine_psql_async_prod))

	logger.info('Finished resetting PSQL (ASYNC) PROD database!')

	click.echo(f'DONE')

	return None



# Drop



@click.command()
@click.confirmation_option(prompt='Are you sure you wish to drop the TESTING database?')
def drop_psql_testing() -> None:
	# Drop DB

	logger.info('Dropping PSQL TESTING database!')


	drop_psql_db(
		engine_psql=engine_psql_testing,
	)

	logger.info('Finished dropping PSQL TESTING database!')

	click.echo(f'DONE')

	return None


@click.command()
@click.confirmation_option(prompt='Are you sure you wish to drop the PSQL DEV database?')
def drop_psql_dev() -> None:
	# Drop DB

	logger.info('Dropping PSQL DEV database!')


	drop_psql_db(
		engine_psql=engine_psql_dev,
	)


	logger.info('Finished dropping PSQL DEV database!')

	click.echo(f'DONE')

	return None



@click.command()
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
@click.confirmation_option(prompt='Are you sure you wish to drop the PSQL PROD database?')
def drop_psql_prod(password) -> None:
	# Drop DB


	if password != settings.CLI_PASSWORD:
		raise ValueError('Invalid password!')

	logger.info('Dropping PSQL PROD database!')

	drop_psql_db(
		engine_psql=engine_psql_prod,
	)

	logger.info('Finished dropping PSQL PROD database!')

	click.echo(f'DONE')

	return None




@click.command()
@click.confirmation_option(prompt='Are you sure you wish to drop the PSQL ASNYC TESTING database?')
def drop_psql_async_testing() -> None:
	# Drop DB

	logger.info('Dropping PSQL (ASYNC) TESTING database!')

	asyncio.run(drop_psql_async_db(engine_psql_async_testing))

	logger.info('Finished dropping PSQL (ASYNC) TESTING database!')

	click.echo(f'DONE')

	return None


@click.command()
@click.confirmation_option(prompt='Are you sure you wish to drop the PSQL (ASYNC) DEV database?')
def drop_psql_async_dev() -> None:
	# Drop DB

	logger.info('Dropping PSQL (ASYNC) DEV database!')

	asyncio.run(drop_psql_async_db(engine_psql_async_dev))

	logger.info('Finished dropping PSQL (ASYNC) DEV database!')

	click.echo(f'DONE')

	return None



@click.command()
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
@click.confirmation_option(prompt='Are you sure you wish to drop the PSQL (ASYNC) PROD database?')
def drop_psql_async_prod(password) -> None:
	# Drop DB

	if password != settings.CLI_PASSWORD:
		raise ValueError('Invalid password!')

	logger.info('Dropping PSQL (ASYNC) PROD database!')

	asyncio.run(drop_psql_async_db(engine_psql_async_prod))

	logger.info('Finished dropping PSQL (ASYNC) PROD database!')

	click.echo(f'DONE')

	return None




@click.command()
@click.confirmation_option(prompt='Are you sure you wish to create the first superadmin for PSQL (ASYNC) TESTING database?')
def create_first_superadmin_psql_async_testing() -> None:
	# --

	logger.info('Creating first superadmin PSQL (ASYNC) TESTING database!')

	asyncio.run(create_first_superadmin_psql_async_db(engine_psql_async_testing))

	logger.info('Finished Creating first superadmin PSQL (ASYNC) TESTING database!')

	click.echo(f'DONE')

	return None


@click.command()
@click.confirmation_option(prompt='Are you sure you wish to create the first superadmin for PSQL (ASYNC) DEV database?')
def create_first_superadmin_psql_async_dev() -> None:
	# --

	logger.info('Creating first superadmin PSQL (ASYNC) DEV database!')

	asyncio.run(create_first_superadmin_psql_async_db(engine_psql_async_dev))

	logger.info('Finished Creating first superadmin PSQL (ASYNC) DEV database!')

	click.echo(f'DONE')

	return None


@click.command()
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
@click.confirmation_option(prompt='Are you sure you wish to create the first superadmin for PSQL (ASYNC) PROD database?')
def create_first_superadmin_psql_async_prod(password) -> None:
	# --

	if password != settings.CLI_PASSWORD:
		raise ValueError('Invalid password!')

	logger.info('Creating first superadmin PSQL (ASYNC) PROD database!')

	asyncio.run(create_first_superadmin_psql_async_db(engine_psql_async_prod))

	logger.info('Finished Creating first superadmin PSQL (ASYNC) PROD database!')

	click.echo(f'DONE')

	return None



@click.command()
@click.confirmation_option(prompt='Are you sure you wish to create the first admin for PSQL (ASYNC) TESTING database?')
def create_first_admin_psql_async_testing() -> None:
	# --

	logger.info('Creating first admin PSQL (ASYNC) TESTING database!')

	asyncio.run(create_first_admin_psql_async_db(engine_psql_async_testing))

	logger.info('Finished Creating first admin PSQL (ASYNC) TESTING database!')

	click.echo(f'DONE')

	return None


@click.command()
@click.confirmation_option(prompt='Are you sure you wish to create the first admin for PSQL (ASYNC) DEV database?')
def create_first_admin_psql_async_dev() -> None:
	# --

	logger.info('Creating first admin PSQL (ASYNC) DEV database!')

	asyncio.run(create_first_admin_psql_async_db(engine_psql_async_dev))

	logger.info('Finished Creating first admin PSQL (ASYNC) DEV database!')

	click.echo(f'DONE')

	return None


@click.command()
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
@click.confirmation_option(prompt='Are you sure you wish to create the first admin for PSQL (ASYNC) PROD database?')
def create_first_admin_psql_async_prod(password) -> None:
	# --

	if password != settings.CLI_PASSWORD:
		raise ValueError('Invalid password!')

	logger.info('Creating first admin PSQL (ASYNC) PROD database!')

	asyncio.run(create_first_admin_psql_async_db(engine_psql_async_prod))

	logger.info('Finished Creating first admin PSQL (ASYNC) PROD database!')

	click.echo(f'DONE')

	return None



@click.command()
@click.confirmation_option(prompt='Are you sure you wish to create the first coach for PSQL (ASYNC) TESTING database?')
def create_first_coach_psql_async_testing() -> None:
	# --

	logger.info('Creating first coach PSQL (ASYNC) TESTING database!')

	asyncio.run(create_first_coach_psql_async_db(engine_psql_async_testing))

	logger.info('Finished Creating first coach PSQL (ASYNC) TESTING database!')

	click.echo(f'DONE')

	return None


@click.command()
@click.confirmation_option(prompt='Are you sure you wish to create the first coach for PSQL (ASYNC) DEV database?')
def create_first_coach_psql_async_dev() -> None:
	# --

	logger.info('Creating first coach PSQL (ASYNC) DEV database!')

	asyncio.run(create_first_coach_psql_async_db(engine_psql_async_dev))

	logger.info('Finished Creating first coach PSQL (ASYNC) DEV database!')

	click.echo(f'DONE')

	return None


@click.command()
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
@click.confirmation_option(prompt='Are you sure you wish to create the first coach for PSQL (ASYNC) PROD database?')
def create_first_coach_psql_async_prod(password) -> None:
	# --

	if password != settings.CLI_PASSWORD:
		raise ValueError('Invalid password!')

	logger.info('Creating first coach PSQL (ASYNC) PROD database!')

	asyncio.run(create_first_coach_psql_async_db(engine_psql_async_prod))

	logger.info('Finished Creating first coach PSQL (ASYNC) PROD database!')

	click.echo(f'DONE')

	return None



@click.command()
@click.confirmation_option(prompt='Are you sure you wish to create the first guardian for PSQL (ASYNC) TESTING database?')
def create_first_guardian_psql_async_testing() -> None:
	# --

	logger.info('Creating first guardian PSQL (ASYNC) TESTING database!')

	asyncio.run(create_first_guardian_psql_async_db(engine_psql_async_testing))

	logger.info('Finished Creating first guardian PSQL (ASYNC) TESTING database!')

	click.echo(f'DONE')

	return None


@click.command()
@click.confirmation_option(prompt='Are you sure you wish to create the first guardian for PSQL (ASYNC) DEV database?')
def create_first_guardian_psql_async_dev() -> None:
	# --

	logger.info('Creating first guardian PSQL (ASYNC) DEV database!')

	asyncio.run(create_first_guardian_psql_async_db(engine_psql_async_dev))

	logger.info('Finished Creating first guardian PSQL (ASYNC) DEV database!')

	click.echo(f'DONE')

	return None


@click.command()
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
@click.confirmation_option(prompt='Are you sure you wish to create the first guardian for PSQL (ASYNC) PROD database?')
def create_first_guardian_psql_async_prod(password) -> None:
	# --

	if password != settings.CLI_PASSWORD:
		raise ValueError('Invalid password!')

	logger.info('Creating first guardian PSQL (ASYNC) PROD database!')

	asyncio.run(create_first_guardian_psql_async_db(engine_psql_async_prod))

	logger.info('Finished Creating first guardian PSQL (ASYNC) PROD database!')

	click.echo(f'DONE')

	return None




@click.command()
@click.confirmation_option(prompt='Are you sure you wish to create the first adult_rep for PSQL (ASYNC) TESTING database?')
def create_first_adult_rep_psql_async_testing() -> None:
	# --

	logger.info('Creating first adult_rep PSQL (ASYNC) TESTING database!')

	asyncio.run(create_first_adult_rep_psql_async_db(engine_psql_async_testing))

	logger.info('Finished Creating first adult_rep PSQL (ASYNC) TESTING database!')

	click.echo(f'DONE')

	return None


@click.command()
@click.confirmation_option(prompt='Are you sure you wish to create the first adult_rep for PSQL (ASYNC) DEV database?')
def create_first_adult_rep_psql_async_dev() -> None:
	# --

	logger.info('Creating first adult_rep PSQL (ASYNC) DEV database!')

	asyncio.run(create_first_adult_rep_psql_async_db(engine_psql_async_dev))

	logger.info('Finished Creating first adult_rep PSQL (ASYNC) DEV database!')

	click.echo(f'DONE')

	return None


@click.command()
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
@click.confirmation_option(prompt='Are you sure you wish to create the first adult_rep for PSQL (ASYNC) PROD database?')
def create_first_adult_rep_psql_async_prod(password) -> None:
	# --

	if password != settings.CLI_PASSWORD:
		raise ValueError('Invalid password!')

	logger.info('Creating first adult_rep PSQL (ASYNC) PROD database!')

	asyncio.run(create_first_adult_rep_psql_async_db(engine_psql_async_prod))

	logger.info('Finished Creating first adult_rep PSQL (ASYNC) PROD database!')

	click.echo(f'DONE')

	return None




cli.add_command(init_psql_testing)
cli.add_command(init_psql_dev)
cli.add_command(init_psql_prod)
cli.add_command(init_psql_async_testing)
cli.add_command(init_psql_async_dev)
cli.add_command(init_psql_async_prod)


cli.add_command(reset_psql_testing)
cli.add_command(reset_psql_dev)
cli.add_command(reset_psql_prod)
cli.add_command(reset_psql_async_testing)
cli.add_command(reset_psql_async_dev)
cli.add_command(reset_psql_async_prod)


cli.add_command(drop_psql_testing)
cli.add_command(drop_psql_dev)
cli.add_command(drop_psql_prod)
cli.add_command(drop_psql_async_testing)
cli.add_command(drop_psql_async_dev)
cli.add_command(drop_psql_async_prod)


cli.add_command(create_first_superadmin_psql_async_testing)
cli.add_command(create_first_superadmin_psql_async_dev)
cli.add_command(create_first_superadmin_psql_async_prod)


cli.add_command(create_first_admin_psql_async_testing)
cli.add_command(create_first_admin_psql_async_dev)
cli.add_command(create_first_admin_psql_async_prod)


cli.add_command(create_first_coach_psql_async_testing)
cli.add_command(create_first_coach_psql_async_dev)
cli.add_command(create_first_coach_psql_async_prod)


cli.add_command(create_first_guardian_psql_async_testing)
cli.add_command(create_first_guardian_psql_async_dev)
cli.add_command(create_first_guardian_psql_async_prod)


cli.add_command(create_first_adult_rep_psql_async_testing)
cli.add_command(create_first_adult_rep_psql_async_dev)
cli.add_command(create_first_adult_rep_psql_async_prod)


# In use:
# -------

# ahg-db-main-cli database init-psql-testing
# ahg-db-main-cli database init-psql-dev
# ahg-db-main-cli database init-psql-prod
# ahg-db-main-cli database init-psql-async-testing
# ahg-db-main-cli database init-psql-async-dev
# ahg-db-main-cli database init-psql-async-prod

# ahg-db-main-cli database reset-psql-testing
# ahg-db-main-cli database reset-psql-dev
# ahg-db-main-cli database reset-psql-prod
# ahg-db-main-cli database reset-psql-async-testing
# ahg-db-main-cli database reset-psql-async-dev
# ahg-db-main-cli database reset-psql-async-prod

# ahg-db-main-cli database drop-psql-testing
# ahg-db-main-cli database drop-psql-dev
# ahg-db-main-cli database drop-psql-prod
# ahg-db-main-cli database drop-psql-async-testing
# ahg-db-main-cli database drop-psql-async-dev
# ahg-db-main-cli database drop-psql-async-prod

# ahg-db-main-cli database create-first-superadmin-psql-async-testing
# ahg-db-main-cli database create-first-superadmin-psql-async-dev
# ahg-db-main-cli database create-first-superadmin-psql-async-prod

# ahg-db-main-cli database create-first-admin-psql-async-testing
# ahg-db-main-cli database create-first-admin-psql-async-dev
# ahg-db-main-cli database create-first-admin-psql-async-prod

# ahg-db-main-cli database create-first-coach-psql-async-testing
# ahg-db-main-cli database create-first-coach-psql-async-dev
# ahg-db-main-cli database create-first-coach-psql-async-prod

# ahg-db-main-cli database create-first-guardian-psql-async-testing
# ahg-db-main-cli database create-first-guardian-psql-async-dev
# ahg-db-main-cli database create-first-guardian-psql-async-prod

# ahg-db-main-cli database create-first-adult-rep-psql-async-testing
# ahg-db-main-cli database create-first-adult-rep-psql-async-dev
# ahg-db-main-cli database create-first-adult-rep-psql-async-prod



