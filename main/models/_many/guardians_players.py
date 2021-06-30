from sqlalchemy import (
	Boolean,
	Column,
	ForeignKey,
	Integer,
	String,
	Text,
	Enum,
)

from sqlalchemy.orm import relationship

from main.database.base_class import Base

from main.utils.sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)


from collections import OrderedDict




class GuardiansPlayersModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'guardians_players'


	guardian_id = Column(
		Integer,
		ForeignKey('guardians.id'),
		primary_key=True,
	)

	player_id = Column(
		Integer,
		ForeignKey('players.id'),
		primary_key=True,
	)



	role = Column(
		String,
	)

	is_emergency_contact = Column(
		Boolean,
		server_default='0',
	)



	guardians_sc = relationship(
		'GuardianModel',
		back_populates='guardians_players',
		uselist=False,
	)

	players_sc = relationship(
		'PlayerModel',
		back_populates='guardians_players',
		uselist=False,
	)


	__mapper_args__ = {
		'eager_defaults': True,
	}





