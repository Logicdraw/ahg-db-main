# This is for setting-up purposes strictly --


from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker


from main.config import settings




engine_sqlite_dev = create_engine(
	settings.SQLITE_DEV_URI,
	connect_args={
		'check_same_thread': False,
	},
	echo=True,
)



SessionSQLiteDev = sessionmaker(
	autocommit=False,
	autoflush=False,
	bind=engine_sqlite_dev,
)


