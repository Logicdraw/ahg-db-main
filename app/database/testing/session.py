from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker


from app.config import get_settings
settings = get_settings()



engine_testing = create_engine(
	settings.SQLALCHEMY_TESTING_DATABASE_URI,
	pool_pre_ping=True,
)


SessionTesting = sessionmaker(
	autocommit=False,
	autoflush=False,
	bind=engine_testing,
)




