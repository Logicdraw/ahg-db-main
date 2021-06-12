from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker


from main.config import settings



echo_on = True

if settings.DEVELOPMENT:
	SQLALCHEMY_URI = settings.PSQL_DEV_URI
elif settings.TESTING:
	SQLALCHEMY_URI = settings.PSQL_TESTING_URI
elif settings.STAGING:
	SQLALCHEMY_URI = settings.PSQL_DEV_URI
elif settings.PRODUCTION:
	SQLALCHEMY_URI = settings.PSQL_PROD_URI
	echo_on = False




engine_psql = create_engine(
	SQLALCHEMY_URI,
	pool_pre_ping=True,
	echo=echo_on,
)



SessionPSQL = sessionmaker(
	engine_psql,
	expire_on_commit=False,
	class_=AsyncSession,
)


