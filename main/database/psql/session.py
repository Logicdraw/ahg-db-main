from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker


from main.config import settings



if settings.DEVELOPMENT or settings.STAGING:
	SQLALCHEMY_URI = settings.PSQL_DEV_URI
elif settings.TESTING:
	SQLALCHEMY_URI = settings.PSQL_TESTING_URI
elif settings.PRODUCTION:
	SQLALCHEMY_URI = settings.PSQL_PROD_URI




engine_psql = create_engine(
	SQLALCHEMY_URI,
	pool_pre_ping=True,
)



SessionPSQL = sessionmaker(
	engine_psql,
	expire_on_commit=False,
	class_=AsyncSession,
)


