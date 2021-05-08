from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context


import os
import sys


from dotenv import load_dotenv




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
from app.database.base import Base
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
db_urls = {
	'dev_sqlite': 'sqlite:///{}'.format(os.path.join(base_dir, '_dev_.db')),
	'testing_sqlite': 'sqlite:///{}'.format(os.path.join(base_dir, '_testing_.db')),
	'dev': os.environ['SQLALCHEMY_DEV_DATABASE_URI'],
	'testing': os.environ['SQLALCHEMY_TESTING_DATABASE_URI'],
	'prod': os.environ['SQLALCHEMY_PROD_DATABASE_URI'],
}


try:
	db_url = db_urls[cmd_kwargs['db']]
	# Set -- DB URL in .ini in main section (under [alembic])
	config.set_main_option("sqlalchemy.url", db_url)
except ValueError:
	raise Exception(
		'Invalid database given! '
		'Must be one of: {}.'.format(','.join(db_urls.keys()))
	)




def run_migrations_offline():
	"""Run migrations in 'offline' mode.

	This configures the context with just a URL
	and not an Engine, though an Engine is acceptable
	here as well.  By skipping the Engine creation
	we don't even need a DBAPI to be available.

	Calls to context.execute() here emit the given string to the
	script output.

	"""
	url = config.get_main_option("sqlalchemy.url")
	context.configure(
		url=url,
		target_metadata=target_metadata,
		literal_binds=True,
		dialect_opts={'paramstyle': 'named'},
		# render_as_batch=True, # SQLite --
	)

	with context.begin_transaction():
		context.run_migrations()


def run_migrations_online():
	"""Run migrations in 'online' mode.

	In this scenario we need to create an Engine
	and associate a connection with the context.

	"""

	connectable = engine_from_config(
		config.get_section(config.config_ini_section),
		prefix="sqlalchemy.",
		poolclass=pool.NullPool,
	)
	with connectable.connect() as connection:
		context.configure(
			connection=connection,
			target_metadata=target_metadata,
		)

		with context.begin_transaction():
			context.run_migrations()


if context.is_offline_mode():
	run_migrations_offline()
else:
	run_migrations_online()



