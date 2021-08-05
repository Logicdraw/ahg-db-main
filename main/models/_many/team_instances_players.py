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



class TeamInstancesPlayersModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'team_instances_players'


	team_instance_id = Column(
		Integer,
		ForeignKey('team_instances.id'),
		primary_key=True,
	)

	player_id = Column(
		Integer,
		ForeignKey('players.id'),
		primary_key=True,
	)


	comment = Column(
		String,
		index=True,
	)


	position = Column(
		String,
	)

	sponsors = Column(
		Text,
	)

	# sponsors Json...?



	team_instances_sc = relationship(
		'TeamInstanceModel',
		back_populates='team_instances_players',
	)
	
	players_sc = relationship(
		'PlayerModel',
		back_populates='team_instances_players',
	)


	__mapper_args__ = {
		'eager_defaults': True,
	}




