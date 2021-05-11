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




base_dir = os.path.abspath(
			os.path.dirname(
				os.path.dirname(__file__) ))




class Settings(BaseSettings):

	PROJECT_NAME: str = 'ahg-db'


	USE_SQLITE_FOR_TESTING: bool = False


	SQLALCHEMY_TESTING_DATABASE_URI: str
	
	SQLALCHEMY_DEV_DATABASE_URI: str

	SQLALCHEMY_PROD_DATABASE_URI: str


	SQLALCHEMY_DEV_SQLITE_DATABASE_URI: str = 'sqlite:///' + os.path.join(base_dir, '_dev_.db')

	SQLALCHEMY_TESTING_SQLITE_DATABASE_URI: str = 'sqlite:///' + os.path.join(base_dir, '_testing_.db')



	@validator(
		'SQLALCHEMY_TESTING_DATABASE_URI',
		'SQLALCHEMY_DEV_DATABASE_URI',
		'SQLALCHEMY_PROD_DATABASE_URI',
		'SQLALCHEMY_DEV_SQLITE_DATABASE_URI',
		'SQLALCHEMY_TESTING_SQLITE_DATABASE_URI',
		pre=True,
	)
	def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
		if not isinstance(v, str):
			raise ValueError('Not a valid string!')
		return v


	CLI_PASSWORD: str



	class Config:
		case_sensitive = True

		env_file = '.env'




@lru_cache()
def get_settings():
	return Settings()




