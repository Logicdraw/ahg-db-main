from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker


from main.config import get_settings
settings = get_settings()



if settings.DEVELOPMENT:
	SQLALCHEMY_DATABASE_URI = settings.SQLALCHEMY_DEV_DATABASE_URI
elif settings.TESTING:
	SQLALCHEMY_DATABASE_URI = settings.SQLALCHEMY_TESTING_DATABASE_URI
elif settings.STAGING or settings.PRODUCTION:
	SQLALCHEMY_DATABASE_URI = settings.SQLALCHEMY_PROD_DATABASE_URI



engine = create_engine(
	SQLALCHEMY_DATABASE_URI,
	pool_pre_ping=True,
)



SessionObj = sessionmaker(
	autocommit=False,
	autoflush=False,
	bind=engine,
)


