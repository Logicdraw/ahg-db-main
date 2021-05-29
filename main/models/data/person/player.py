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




class PlayerModel(Base, ResourceMixin):

	__tablename__ = 'players'

	id = Column(Integer, primary_key=True)


	# Relationships

	registrations = relationship(
		'RegistrationBaseModel',
		back_populates='player',
		lazy='selectin',
		cascade='all, delete',
	)

	team_instance_registrations = relationship(
		'TeamInstanceRegistrationModel',
		back_populates='player',
		lazy='selectin',
		cascade='all, delete',
	)

	program_instance_registrations = relationship(
		'ProgramInstanceRegistrationModel',
		back_populates='player',
		lazy='selectin',
		cascade='all, delete',
	)

	camp_instance_registrations = relationship(
		'CampInstanceRegistrationModel',
		back_populates='player',
		lazy='selectin',
		cascade='all, delete',
	)


	# Many - to - Many

	guardians = relationship(
		'GuardiansPlayersModel',
		back_populates='player',
		lazy='selectin',
	)

	# Many - to - Many

	team_instances = relationship(
		'TeamInstancesPlayersModel',
		back_populates='player',
		lazy='selectin',
	)



	first_name = Column(String, index=True)

	last_name = Column(String, index=True)

	full_name = column_property(first_name + ' ' + last_name)


	date_of_birth = Column(Date, index=True)


	medicare_number = Column(String)


	street_address_1 = Column(String)

	street_address_2 = Column(String)

	postal_code = Column(String)

	city = Column(String)

	province = Column(String)

	country = Column(String)



	gender = Column(String)

	language = Column(String)



	se_persona_id = Column(Integer, unique=True)
	

	# updated? -- updated_on > created_on ...?


	# Parents




