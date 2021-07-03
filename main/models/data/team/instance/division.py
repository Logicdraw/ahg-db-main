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



class DivisionInstanceModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'division_instances'

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


	divisions_sc = relationship(
		'DivisionModel',
		back_populates='division_instances',
		uselist=False,
	)

	division_id = Column(
		Integer,
		ForeignKey('divisions.id'),
	)


	team_instances = relationship(
		'TeamInstanceModel',
		back_populates='division_instances_sc',
		lazy='selectin',
	)


	season_instances_sc = relationship(
		'SeasonInstanceModel',
		back_populates='division_instances',
		uselist=False,
	)

	season_instance_id = Column(
		Integer,
		ForeignKey('season_instances.id'),
	)


	league_instances_sc = relationship(
		'LeagueInstanceModel',
		back_populates='division_instances',
		uselist=False,
	)

	league_instance_id = Column(
		Integer,
		ForeignKey('league_instances.id'),
	)


	conference_instances_sc = relationship(
		'ConferenceInstanceModel',
		back_populates='division_instances',
		uselist=False,
	)
	
	conference_instance_id = Column(
		Integer,
		ForeignKey('conference_instances.id'),
	)


	__mapper_args__ = {
		'eager_defaults': True,
	}

