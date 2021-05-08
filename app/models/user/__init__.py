from sqlalchemy import (
	Boolean,
	Column,
	ForeignKey,
	Integer,
	String,
)

from sqlalchemy.orm import relationship

from app.database.base_class import Base

from lib.util_sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)




class UserModel(Base, ResourceMixin):

	__tablename__ = 'users'


	id = Column(Integer, primary_key=True, index=True)



	name = Column(String, index=True)


	email = Column(String, unique=True, nullable=False)

	password_hash = Column(String, nullable=False)



	role = Column(String, index=True, nullable=False)


	is_active = Column(Boolean, default=True)





