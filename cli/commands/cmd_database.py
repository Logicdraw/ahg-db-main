import click


import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



from main.database.helpers import (
	init_db,
	reset_db,
	drop_db,
)


from main.database.dev_sqlite.session import (
	SessionDevSQLite,
	engine_dev_sqlite,
)

from main.database.testing_sqlite.session import (
	SessionTestingSQLite,
	engine_testing_sqlite,
)

from main.database.dev.session import (
	SessionDev,
	engine_dev,
)

from main.database.testing.session import (
	SessionTesting,
	engine_testing,
)

from main.database.prod.session import (
	SessionProd,
	engine_prod,
)






@click.group()
def cli():
	""" Run PostgreSQL related tasks. """
	pass





# Initialize


@click.command()
@click.confirmation_option(prompt='Are you sure you wish to initialize the DEV SQLITE database?')
def init_dev_sqlite() -> None:
	# Initialize DB

	logger.info('Initializing DEV SQLITE database!')

	# settings.USE_SQLITE_FOR_TESTING = True

	db = SessionDevSQLite()
	try:
		init_db(
			db=db,
			engine=engine_dev_sqlite,
		)
	except:
		db.rollback()
		raise
	finally:
		db.close()

	logger.info('Finished initializing DEV SQLITE database!')

	click.echo(f'DONE')

	return None



@click.command()
@click.confirmation_option(prompt='Are you sure you wish to initialize the TESTING SQLITE database?')
def init_testing_sqlite() -> None:
	# Initialize DB

	logger.info('Initializing TESTING SQLITE database!')

	# settings.USE_SQLITE_FOR_TESTING = True

	db = SessionTestingSQLite()
	try:
		init_db(
			db=db,
			engine=engine_testing_sqlite,
		)
	except:
		db.rollback()
		raise
	finally:
		db.close()

	logger.info('Finished initializing TESTING SQLITE database!')

	click.echo(f'DONE')

	return None



@click.command()
@click.confirmation_option(prompt='Are you sure you wish to initialize the TESTING database?')
def init_testing() -> None:
	# Initialize DB

	logger.info('Initializing TESTING database!')

	db = SessionTesting()
	try:
		init_db(
			db=db,
			engine=engine_testing,
		)
	except:
		db.rollback()
		raise
	finally:
		db.close()

	logger.info('Finished initializing TESTING database!')

	click.echo(f'DONE')

	return None


@click.command()
@click.confirmation_option(prompt='Are you sure you wish to initialize the DEV database?')
def init_dev() -> None:
	# Initialize DB

	logger.info('Initializing DEV database!')

	db = SessionDev()
	try:
		init_db(
			db=db,
			engine=engine_dev,
		)
	except:
		db.rollback()
		raise
	finally:
		db.close()

	logger.info('Finished initializing DEV database!')

	click.echo(f'DONE')

	return None


@click.command()
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
@click.confirmation_option(prompt='Are you sure you wish to initialize the TESTING database?')
def init_prod(password) -> None:
	# Initialize DB

	if password != settings.CLI_PASSWORD:
		raise ValueError('Invalid password!')

	logger.info('Initializing PROD database!')

	db = SessionProd()
	try:
		init_db(
			db=db,
			engine=engine_prod,
		)
	except:
		db.rollback()
		raise
	finally:
		db.close()

	logger.info('Finished initializing PRODUCTION database!')

	click.echo(f'DONE')

	return None




# Reset


@click.command()
@click.confirmation_option(prompt='Are you sure you wish to reset the DEV SQLITE database?')
def reset_dev_sqlite() -> None:
	# Reset DB

	logger.info('Resetting DEV SQLITE database!')

	# settings.USE_SQLITE_FOR_TESTING = True

	db = SessionDevSQLite()
	try:
		reset_db(
			db=db,
			engine=engine_dev_sqlite,
		)
	except:
		db.rollback()
		raise
	finally:
		db.close()

	logger.info('Finished resetting DEV SQLITE database!')

	click.echo(f'DONE')

	return None



@click.command()
@click.confirmation_option(prompt='Are you sure you wish to reset the TESTING SQLITE database?')
def reset_testing_sqlite() -> None:
	# Reset DB

	logger.info('Resetting TESTING SQLITE database!')

	# settings.USE_SQLITE_FOR_TESTING = True

	db = SessionDevSQLite()
	try:
		reset_db(
			db=db,
			engine=engine_testing_sqlite,
		)
	except:
		db.rollback()
		raise
	finally:
		db.close()

	logger.info('Finished resetting TESTING SQLITE database!')

	click.echo(f'DONE')

	return None




@click.command()
@click.confirmation_option(prompt='Are you sure you wish to reset the TESTING database?')
def reset_testing() -> None:
	# Reset DB

	logger.info('Resetting TESTING database!')

	db = SessionTesting()
	try:
		reset_db(
			db=db,
			engine=engine_testing,
		)
	except:
		db.rollback()
		raise
	finally:
		db.close()

	logger.info('Finished resetting TESTING database!')

	click.echo(f'DONE')

	return None


@click.command()
@click.confirmation_option(prompt='Are you sure you wish to reset the DEV database?')
def reset_dev() -> None:
	# Reset DB

	logger.info('resetting DEV database!')

	db = SessionDev()
	try:
		reset_db(
			db=db,
			engine=engine_dev,
		)
	except:
		db.rollback()
		raise
	finally:
		db.close()

	logger.info('Finished resetting DEV database!')

	click.echo(f'DONE')

	return None


@click.command()
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
@click.confirmation_option(prompt='Are you sure you wish to reset the PROD database?')
def reset_prod(password) -> None:
	# Reset DB

	if password != settings.CLI_PASSWORD:
		raise ValueError('Invalid password!')

	logger.info('Resetting PROD database!')

	db = SessionProd()
	try:
		reset_db(
			db=db,
			engine=engine_prod,
		)
	except:
		db.rollback()
		raise
	finally:
		db.close()

	logger.info('Finished resetting PROD database!')

	click.echo(f'DONE')

	return None



# Drop


@click.command()
@click.confirmation_option(prompt='Are you sure you wish to drop the DEV SQLITE database?')
def drop_dev_sqlite() -> None:
	# Drop DB

	logger.info('Dropping DEV SQLITE database!')

	# settings.USE_SQLITE_FOR_TESTING = True

	db = SessionDevSQLite()
	try:
		drop_db(
			db=db,
			engine=engine_dev_sqlite,
		)
	except:
		db.rollback()
		raise
	finally:
		db.close()

	logger.info('Finished dropping DEV SQLITE database!')

	click.echo(f'DONE')

	return None


@click.command()
@click.confirmation_option(prompt='Are you sure you wish to drop the DEV database?')
def drop_testing_sqlite() -> None:
	# Drop DB

	logger.info('dropping TESTING SQLITE database!')

	# settings.USE_SQLITE_FOR_TESTING = True

	db = SessionDev()
	try:
		drop_db(
			db=db,
			engine=engine_testing_sqlite,
		)
	except:
		db.rollback()
		raise
	finally:
		db.close()

	logger.info('Finished dropping TESTING SQLITE database!')

	click.echo(f'DONE')

	return None



@click.command()
@click.confirmation_option(prompt='Are you sure you wish to drop the TESTING database?')
def drop_testing() -> None:
	# Drop DB

	logger.info('Dropping TESTING database!')

	db = SessionTesting()
	try:
		drop_db(
			db=db,
			engine=engine_testing,
		)
	except:
		db.rollback()
		raise
	finally:
		db.close()

	logger.info('Finished dropping TESTING database!')

	click.echo(f'DONE')

	return None


@click.command()
@click.confirmation_option(prompt='Are you sure you wish to drop the DEV database?')
def drop_dev() -> None:
	# Drop DB

	logger.info('dropping DEV database!')

	db = SessionDev()
	try:
		drop_db(
			db=db,
			engine=engine_dev,
		)
	except:
		db.rollback()
		raise
	finally:
		db.close()

	logger.info('Finished dropping DEV database!')

	click.echo(f'DONE')

	return None



@click.command()
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
@click.confirmation_option(prompt='Are you sure you wish to drop the PROD database?')
def drop_prod(password) -> None:
	# Drop DB


	if password != settings.CLI_PASSWORD:
		raise ValueError('Invalid password!')

	logger.info('Dropping PROD database!')

	db = SessionProd()
	try:
		drop_db(
			db=db,
			engine=engine_prod,
		)
	except:
		db.rollback()
		raise
	finally:
		db.close()

	logger.info('Finished dropping PROD database!')

	click.echo(f'DONE')

	return None





cli.add_command(init_dev_sqlite)
cli.add_command(init_testing_sqlite)
cli.add_command(init_testing)
cli.add_command(init_dev)
cli.add_command(init_prod)


cli.add_command(reset_dev_sqlite)
cli.add_command(reset_testing_sqlite)
cli.add_command(reset_testing)
cli.add_command(reset_dev)
cli.add_command(reset_prod)


cli.add_command(drop_dev_sqlite)
cli.add_command(drop_testing_sqlite)
cli.add_command(drop_testing)
cli.add_command(drop_dev)
cli.add_command(drop_prod)






# In use:
# -------

# ahg-db-cli database init-dev-sqlite
# ahg-db-cli database init-testing-sqlite
# ahg-db-cli database init-testing
# ahg-db-cli database init-dev
# ahg-db-cli database init-prod

# ahg-db-cli database reset-dev-sqlite
# ahg-db-cli database reset-testing-sqlite
# ahg-db-cli database reset-testing
# ahg-db-cli database reset-dev
# ahg-db-cli database reset-prod

# ahg-db-cli database drop-dev-sqlite
# ahg-db-cli database drop-testing-sqlite
# ahg-db-cli database drop-testing
# ahg-db-cli database drop-dev
# ahg-db-cli database drop-prod






