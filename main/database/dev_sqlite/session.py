# This is for setting-up purposes strictly --


from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker


from main.config import get_settings
settings = get_settings()




engine_dev_sqlite = create_engine(
	settings.SQLALCHEMY_DEV_SQLITE_DATABASE_URI,
	connect_args={
		'check_same_thread': False,
	},
)




SessionDevSQLite = sessionmaker(
	autocommit=False,
	autoflush=False,
	bind=engine_dev_sqlite,
)


