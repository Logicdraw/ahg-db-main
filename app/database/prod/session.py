from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker


from app.config import get_settings
settings = get_settings()



engine_prod = create_engine(
	settings.SQLALCHEMY_PROD_DATABASE_URI,
	pool_pre_ping=True,
)



SessionProd = sessionmaker(
	autocommit=False,
	autoflush=False,
	bind=engine_prod,
)


