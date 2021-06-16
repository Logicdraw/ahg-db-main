from sqlalchemy import (
	Boolean,
	Column,
	ForeignKey,
	Integer,
	String,
)

from sqlalchemy.orm import relationship

from main.database.base_class import Base

from lib.util_sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)


from sqlalchemy.dialects import postgresql




class UserModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'users'


	id = Column(Integer, primary_key=True, index=True)



	name = Column(String, index=True)


	email = Column(String, unique=True, nullable=False)

	password_hash = Column(String, nullable=False)



	role = Column(String, index=True, nullable=False)


	# roles = (Array)
	# roles = Column(postgresql.ARRAY(String))
	# Maybe ... ?


	is_active = Column(Boolean, server_default='1')


	__mapper_args__ = {
		'eager_defaults': True,
	}




