# This is for setting-up purposes strictly --


from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker


from app.config import get_settings
settings = get_settings()




engine_testing_sqlite = create_engine(
	settings.SQLALCHEMY_TESTING_SQLITE_DATABASE_URI,
	connect_args={
		'check_same_thread': False,
	},
)




SessionTestingSQLite = sessionmaker(
	autocommit=False,
	autoflush=False,
	bind=engine_testing_sqlite,
)


