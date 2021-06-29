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
	# column_property,
)

from main.database.base_class import Base

from lib.util_sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)


from sqlalchemy.ext.hybrid import (
	hybrid_property,
	hybrid_method,
)





class PlayerModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'players'

	id = Column(Integer, primary_key=True)


	# Relationships

	registrations = relationship(
		'RegistrationBaseModel',
		back_populates='players_sc',
		lazy='selectin',
		cascade='delete',
	)


	# Change!! -- column property ... ?

	# team_instance_registrations = relationship(
	# 	'TeamInstanceRegistrationModel',
	# 	back_populates='player',
	# 	lazy='selectin',
	# 	cascade='delete',
	# )

	# program_instance_registrations = relationship(
	# 	'ProgramInstanceRegistrationModel',
	# 	back_populates='player',
	# 	lazy='selectin',
	# 	cascade='delete',
	# )

	# camp_instance_registrations = relationship(
	# 	'CampInstanceRegistrationModel',
	# 	back_populates='player',
	# 	lazy='selectin',
	# 	cascade='delete',
	# )


	# Many - to - Many

	guardians_players = relationship(
		'GuardiansPlayersModel',
		back_populates='players_sc',
		lazy='selectin',
	)

	# Many - to - Many

	team_instances_players = relationship(
		'TeamInstancesPlayersModel',
		back_populates='players_sc',
		lazy='selectin',
	)



	first_name = Column(String, index=True)

	last_name = Column(String, index=True)


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



	spng_persona_id = Column(Integer, unique=True)
	

	# updated? -- updated_on > created_on ...?


	# Parents



	__mapper_args__ = {
		'eager_defaults': True,
	}



	@hybrid_property
	def full_name(self):
		return f'{self.first_name} {self.last_name}'

	



