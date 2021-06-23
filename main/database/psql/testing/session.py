from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker


from main.config import settings




engine_psql_testing = create_engine(
	settings.PSQL_TESTING_URI,
	pool_pre_ping=True,
	echo=True,
	# echo=False,
)



SessionPSQLTesting = sessionmaker(
	autocommit=False,
	autoflush=False,
	bind=engine_psql_testing,
)


