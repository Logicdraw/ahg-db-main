from typing import (
	Any,
	Dict,
	List,
	Optional,
	Union,
)


from pydantic import (
	AnyHttpUrl,
	BaseSettings,
	EmailStr,
	HttpUrl,
	PostgresDsn,
	validator,
)


import os


from functools import lru_cache


import psycopg2




if 'VERCEL' in os.environ:
	in_prod = (os.environ['VERCEL_ENV'] == 'production')
	in_staging = (os.environ['VERCEL_ENV'] == 'preview')
	in_server = True
else:
	in_prod = in_staging = in_server = False



in_dev = (not in_server)




base_dir = os.path.abspath(
			os.path.dirname(
				os.path.dirname(__file__) ))




class Settings(BaseSettings):

	PROJECT_NAME: str = 'ahg-serv-database'



	TESTING: bool = False

	DEVELOPMENT: bool = False

	STAGING: bool = False

	PRODUCTION: bool = False



	USE_SQLITE_FOR_TESTING: bool = False



	if in_dev:

		DEVELOPMENT: bool = True


		SERVER_NAME: str = '127.0.0.1:8000'

		SERVER_HOST: str = f'http://{SERVER_NAME}'


		SECRET_KEY: str

		AUTH_SECRET_KEY: str


		USE_SQLITE_FOR_TESTING: bool = False


		SQLALCHEMY_TESTING_DATABASE_URI: str
		
		SQLALCHEMY_DEV_DATABASE_URI: str

		SQLALCHEMY_PROD_DATABASE_URI: str


		SQLALCHEMY_DATABASE_URI: str

		SQLALCHEMY_DATABASE_URI_TESTING: str


		SQLALCHEMY_DEV_SQLITE_DATABASE_URI: str = 'sqlite:///' + os.path.join(base_dir, '_dev_.db')

		SQLALCHEMY_TESTING_SQLITE_DATABASE_URI: str = 'sqlite:///' + os.path.join(base_dir, '_testing_.db')


		@validator(
			'SQLALCHEMY_DATABASE_URI',
			'SQLALCHEMY_DATABASE_URI_TESTING',
			pre=True,
		)
		def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
			if not isinstance(v, str):
				raise ValueError('Not a valid string!')
			return v



		FIRST_SUPERADMIN_NAME: str

		FIRST_SUPERADMIN_EMAIL: str
		
		FIRST_SUPERADMIN_PASSWORD: str


		CLI_PASSWORD: str



	if in_server:

		SERVER_NAME: str = os.environ['VERCEL_URL']

		SERVER_HOST: str = f'https://{SERVER_NAME}'


		SECRET_KEY: str = os.environ['SECRET_KEY']
		
		AUTH_SECRET_KEY: str = os.environ['AUTH_SECRET_KEY']



		FIRST_SUPERADMIN_NAME: str = os.environ['FIRST_SUPERADMIN_NAME']

		FIRST_SUPERADMIN_EMAIL: str = os.environ['FIRST_SUPERADMIN_EMAIL']

		FIRST_SUPERADMIN_PASSWORD: str = os.environ['FIRST_SUPERADMIN_PASSWORD']


		
		SENTRY_DSN: Optional[HttpUrl] = os.environ['SENTRY_DSN']

		@validator(
			'SENTRY_DSN',
			pre=True,
		)
		def sentry_dsn_can_be_blank(cls, v: str) -> Optional[str]:
			if len(v) == 0:
				return None
			return v



		SQLALCHEMY_DATABASE_URI: str = os.environ['DATABASE_URL']

		@validator(
			'SQLALCHEMY_DATABASE_URI',
			pre=True,
		)
		def assemble_db_connection(
			cls,
			v: Optional[str],
			values: Dict[str, Any],
		) -> Any:
			if not isinstance(v, str):
				raise ValueError('Not a valid string!')
			return v



	if in_staging:
		
		STAGING: bool = True


	if in_prod:
		
		PRODUCTION: bool = True




	class Config:
		case_sensitive = True

		env_file = '.env'




@lru_cache()
def get_settings():
	return Settings()




