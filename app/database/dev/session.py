from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker


from app.config import get_settings
settings = get_settings()



engine_dev = create_engine(
	settings.SQLALCHEMY_DEV_DATABASE_URI,
	pool_pre_ping=True,
)



SessionDev = sessionmaker(
	autocommit=False,
	autoflush=False,
	bind=engine_dev,
)



