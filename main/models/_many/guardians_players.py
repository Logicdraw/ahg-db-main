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

from lib.util_sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)


from collections import OrderedDict




class GuardiansPlayersModel(Base, ResourceMixin):

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



	role = Column(String)

	is_emergency_contact = Column(Boolean, default=False)



	guardian = relationship(
		'GuardianModel',
		back_populates='players',
		uselist=False,
	)

	player = relationship(
		'PlayerModel',
		back_populates='guardians',
		uselist=False,
	)





