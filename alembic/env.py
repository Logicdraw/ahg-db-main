from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context


import os
import sys


from dotenv import load_dotenv


from main.config import settings


import asyncio

from sqlalchemy.ext.asyncio import AsyncEngine




# This is so we can load our Database URIs from our .env file :) --

base_dir = os.path.dirname(
			os.path.dirname(
				os.path.abspath(__file__) ))

load_dotenv(os.path.join(base_dir, '.env'))

# Why is this needed again? --
sys.path.append(base_dir)




# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
from main.database.base import Base
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.




# To specify which database :) --
# Example: alembic -x db=dev upgrade head


cmd_kwargs = context.get_x_argument(as_dictionary=True)

if 'db' not in cmd_kwargs:
	raise Exception('We couldn\'t find `db` in the CLI arguments. '
					'Please verify `alembic` was run with `-x db=<db_name>` '
					'(e.g. `alembic -x db=dev upgrade head`)')



# Our DB URLS :) --
db_uris = {
	# SQLITE --
	'sqlite_dev': settings.SQLITE_DEV_URI,
	'sqlite_testing': settings.SQLITE_TESTING_URI,
	# PSQL --
	# 'psql_dev': settings.PSQL_DEV_URI,
	# 'psql_testing': settings.PSQL_TESTING_URI,
	# 'psql_prod': settings.PSQL_PROD_URI,
	# PSQL Async
	'psql_async_dev': settings.PSQL_ASYNC_DEV_URI,
	'psql_async_testing': settings.PSQL_ASYNC_TESTING_URI,
	'psql_async_prod': settings.PSQL_ASYNC_PROD_URI,
}


try:
	db_uri = db_uris[cmd_kwargs['db']]
	# Set -- DB URL in .ini in main section (under [alembic])
	config.set_main_option('sqlalchemy.url', db_uri)
except ValueError:
	raise Exception(
		'Invalid database given! '
		'Must be one of: {}.'.format(','.join(db_uris.keys()))
	)




# https://gist.github.com/nathancahill/aeec99f6a3423c5ada77
# exclude spatial_ref_sys --

def exclude_tables_from_config(config_):
	tables_ = config_.get('tables', None)
	if tables_ is not None:
		tables = tables_.split(",")
	return tables


exclude_tables = exclude_tables_from_config(config.get_section('alembic:exclude'))


def include_object(object, name, type_, reflected, compare_to):
	return not (type_ == 'table' and name in exclude_tables)




def do_run_migrations(connection):
    context.configure(
    	connection=connection,
    	target_metadata=target_metadata,
    	include_object=include_object,
    )

    with context.begin_transaction():
        context.run_migrations()



def run_migrations_offline():
	"""Run migrations in 'offline' mode.

	This configures the context with just a URL
	and not an Engine, though an Engine is acceptable
	here as well.  By skipping the Engine creation
	we don't even need a DBAPI to be available.

	Calls to context.execute() here emit the given string to the
	script output.

	"""
	url = config.get_main_option('sqlalchemy.url')
	context.configure(
		url=url,
		target_metadata=target_metadata,
		literal_binds=True,
		dialect_opts={'paramstyle': 'named'},
		# render_as_batch=True, # SQLite --
	)

	with context.begin_transaction():
		context.run_migrations()


async def run_migrations_online():
	"""Run migrations in 'online' mode.

	In this scenario we need to create an Engine
	and associate a connection with the context.

	"""

	connectable = AsyncEngine(
		engine_from_config(
			config.get_section(config.config_ini_section),
			prefix="sqlalchemy.",
			poolclass=pool.NullPool,
			future=True,
		)
	)
	async with connectable.connect() as connection:
		await connection.run_sync(do_run_migrations)



if context.is_offline_mode():
	run_migrations_offline()
else:
	asyncio.run(run_migrations_online())



