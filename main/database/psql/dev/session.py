from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker


from main.config import settings




engine_psql_dev = create_engine(
	settings.PSQL_DEV_URI,
	pool_pre_ping=True,
)



SessionPSQLDev = sessionmaker(
	autocommit=False,
	autoflush=False,
	bind=engine_psql_dev,
)


