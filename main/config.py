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
	RedisDsn,
	validator,
	SecretStr,
)


import os



base_dir = os.path.abspath(
			os.path.dirname(
				os.path.dirname(__file__) ))




class Settings(BaseSettings):

	PROJECT_NAME: str = 'ahg-db-main'



	# DB --


	PSQL_DEV_DB: str
	PSQL_DEV_HOST: str
	PSQL_DEV_USER: str
	PSQL_DEV_PASSWORD: SecretStr

	PSQL_DEV_URI: Optional[PostgresDsn] = None

	@validator(
		'PSQL_DEV_URI',
		pre=True,
	)
	def assemble_psql_dev_db_connection(
		cls,
		v: Optional[str],
		values: Dict[str, Any],
	) -> Any:
		if isinstance(v, str):
			return v
		password: SecretStr = values.get('PSQL_DEV_PASSWORD', SecretStr(''))
		return '{scheme}://{user}:{password}@{host}/{db}'.format(
			scheme='postgresql',
			user=values.get('PSQL_DEV_USER'),
			password=password.get_secret_value(),
			host=values.get('PSQL_DEV_HOST'),
			db=values.get('PSQL_DEV_DB'),
		)

	PSQL_ASYNC_DEV_URI: Optional[str] = None

	@validator(
		'PSQL_ASYNC_DEV_URI',
		pre=True,
	)
	def assemble_psql_async_dev_db_connection(
		cls,
		v: Optional[str],
		values: Dict[str, Any],
	) -> Any:
		if isinstance(v, str):
			return v
		password: SecretStr = values.get('PSQL_DEV_PASSWORD', SecretStr(''))
		return '{scheme}://{user}:{password}@{host}/{db}'.format(
			scheme='postgresql+asyncpg',
			user=values.get('PSQL_DEV_USER'),
			password=password.get_secret_value(),
			host=values.get('PSQL_DEV_HOST'),
			db=values.get('PSQL_DEV_DB'),
		)



	PSQL_TESTING_DB: str
	PSQL_TESTING_HOST: str
	PSQL_TESTING_USER: str
	PSQL_TESTING_PASSWORD: SecretStr

	PSQL_TESTING_URI: Optional[PostgresDsn] = None

	@validator(
		'PSQL_TESTING_URI',
		pre=True,
	)
	def assemble_psql_testing_db_connection(
		cls,
		v: Optional[str],
		values: Dict[str, Any],
	) -> Any:
		if isinstance(v, str):
			return v
		password: SecretStr = values.get('PSQL_TESTING_PASSWORD', SecretStr(''))
		return '{scheme}://{user}:{password}@{host}/{db}'.format(
			scheme='postgresql',
			user=values.get('PSQL_TESTING_USER'),
			password=password.get_secret_value(),
			host=values.get('PSQL_TESTING_HOST'),
			db=values.get('PSQL_TESTING_DB'),
		)

	PSQL_ASYNC_TESTING_URI: Optional[str] = None

	@validator(
		'PSQL_ASYNC_TESTING_URI',
		pre=True,
	)
	def assemble_psql_async_testing_db_connection(
		cls,
		v: Optional[str],
		values: Dict[str, Any],
	) -> Any:
		if isinstance(v, str):
			return v
		password: SecretStr = values.get('PSQL_TESTING_PASSWORD', SecretStr(''))
		return '{scheme}://{user}:{password}@{host}/{db}'.format(
			scheme='postgresql+asyncpg',
			user=values.get('PSQL_TESTING_USER'),
			password=password.get_secret_value(),
			host=values.get('PSQL_TESTING_HOST'),
			db=values.get('PSQL_TESTING_DB'),
		)



	PSQL_PROD_DB: str
	PSQL_PROD_HOST: str
	PSQL_PROD_USER: str
	PSQL_PROD_PASSWORD: SecretStr

	PSQL_PROD_URI: Optional[PostgresDsn] = None

	@validator(
		'PSQL_PROD_URI',
		pre=True,
	)
	def assemble_psql_prod_db_connection(
		cls,
		v: Optional[str],
		values: Dict[str, Any],
	) -> Any:
		if isinstance(v, str):
			return v
		password: SecretStr = values.get('PSQL_PROD_PASSWORD', SecretStr(''))
		return '{scheme}://{user}:{password}@{host}/{db}'.format(
			scheme='postgresql',
			user=values.get('PSQL_PROD_USER'),
			password=password.get_secret_value(),
			host=values.get('PSQL_PROD_HOST'),
			db=values.get('PSQL_PROD_DB'),
		)


	PSQL_ASYNC_PROD_URI: Optional[str] = None

	@validator(
		'PSQL_ASYNC_PROD_URI',
		pre=True,
	)
	def assemble_psql_async_prod_db_connection(
		cls,
		v: Optional[str],
		values: Dict[str, Any],
	) -> Any:
		if isinstance(v, str):
			return v
		password: SecretStr = values.get('PSQL_PROD_PASSWORD', SecretStr(''))
		return '{scheme}://{user}:{password}@{host}/{db}'.format(
			scheme='postgresql+asyncpg',
			user=values.get('PSQL_PROD_USER'),
			password=password.get_secret_value(),
			host=values.get('PSQL_PROD_HOST'),
			db=values.get('PSQL_PROD_DB'),
		)




	CLI_PASSWORD: str


	SECRET_KEY: SecretStr



	USER_ROLES = [
		'superadmin',
		'admin',
		'coach',
		'guardian',
		'adult_rep',
	]



	FIRST_SUPERADMIN_NAME: str
	FIRST_SUPERADMIN_EMAIL: str
	FIRST_SUPERADMIN_PASSWORD: SecretStr

	FIRST_ADMIN_NAME: str
	FIRST_ADMIN_EMAIL: str
	FIRST_ADMIN_PASSWORD: SecretStr

	FIRST_COACH_NAME: str
	FIRST_COACH_EMAIL: str
	FIRST_COACH_PASSWORD: SecretStr

	FIRST_GUARDIAN_NAME: str
	FIRST_GUARDIAN_EMAIL: str
	FIRST_GUARDIAN_PASSWORD: SecretStr

	FIRST_ADULT_REP_NAME: str
	FIRST_ADULT_REP_EMAIL: str
	FIRST_ADULT_REP_PASSWORD: SecretStr





	class Config:
		case_sensitive = True

		env_file = '.env'






settings = Settings()





