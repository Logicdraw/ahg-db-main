from sqlalchemy import (
	Boolean,
	Column,
	ForeignKey,
	Integer,
	String,
	Enum,
	Date,
)

from sqlalchemy.orm import (
	relationship,
	column_property,
)

from main.database.base_class import Base

from lib.util_sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)




class GuardianModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'guardians'

	id = Column(Integer, primary_key=True)


	# Relationships

	players = relationship(
		'GuardiansPlayersModel',
		back_populates='guardian',
		lazy='selectin',
	)


	full_name = Column(String, index=True)


	mobile_phone = Column(String)

	home_phone = Column(String)

	work_phone = Column(String)


	# Email -- will be unique identifier of guardian!
	email = Column(String, unique=True)



	user = relationship(
		'UserModel',
		uselist=False,
	)
	user_id = Column(Integer, ForeignKey('users.id'))


	__mapper_args__ = {
		'eager_defaults': True,
	}




