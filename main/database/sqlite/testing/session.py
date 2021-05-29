# This is for setting-up purposes strictly --


from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker


from main.config import settings




engine_sqlite_testing = create_engine(
	settings.SQLITE_TESTING_URI,
	connect_args={
		'check_same_thread': False,
	},
)



SessionSQLiteTesting = sessionmaker(
	autocommit=False,
	autoflush=False,
	bind=engine_sqlite_testing,
)

