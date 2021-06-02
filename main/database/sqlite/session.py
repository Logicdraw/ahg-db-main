# Create Sqlite Session--

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker


from main.config import settings



if settings.DEVELOPMENT:
	SQLALCHEMY_URI = settings.SQLITE_DEV_URI
elif settings.TESTING:
	SQLALCHEMY_URI = settings.SQLITE_TESTING_URI



engine_sqlite = create_engine(
	SQLALCHEMY_URI,
	connect_args={
		"check_same_thread": False
	},
	echo=True,
)


