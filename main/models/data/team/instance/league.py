from sqlalchemy import (
	Boolean,
	Column,
	ForeignKey,
	Integer,
	String,
)

from sqlalchemy.orm import relationship

from main.database.base_class import Base

from main.utils.sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)



class LeagueInstanceModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'league_instances'

	id = Column(
		Integer,
		primary_key=True,
	)


	year_start = Column(
		Integer,
	)

	year_end = Column(
		Integer,
	)


	leagues_sc = relationship(
		'LeagueModel',
		back_populates='league_instances',
	)

	league_id = Column(
		Integer,
		ForeignKey('leagues.id'),
	)


	conference_instances = relationship(
		'ConferenceInstanceModel',
		back_populates='league_instances_sc',
		lazy='selectin',
	)

	division_instances = relationship(
		'DivisionInstanceModel',
		back_populates='league_instances_sc',
		lazy='selectin',
	)

	team_instances = relationship(
		'TeamInstanceModel',
		back_populates='league_instances_sc',
		lazy='selectin',
	)


	season_instances_sc = relationship(
		'SeasonInstanceModel',
		back_populates='league_instances',
	)
	
	season_instance_id = Column(
		Integer,
		ForeignKey('season_instances.id'),
	)



	__mapper_args__ = {
		'eager_defaults': True,
	}


