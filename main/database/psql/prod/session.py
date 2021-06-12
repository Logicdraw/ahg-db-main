from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker


from main.config import settings




engine_psql_prod = create_engine(
	settings.PSQL_PROD_URI,
	pool_pre_ping=True,
	echo=False,
)



SessionPSQLProd = sessionmaker(
	autocommit=False,
	autoflush=False,
	bind=engine_psql_prod,
)


