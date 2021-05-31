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



class ConferenceInstanceModel(Base, ResourceMixin):

	__tablename__ = 'conference_instances'

	id = Column(Integer, primary_key=True)


	year_start = Column(Integer)

	year_end = Column(Integer)


	conference = relationship(
		'ConferenceModel',
		back_populates='instances',
		uselist=False,
	)
	conference_id = Column(
		Integer,
		ForeignKey('conferences.id'),
	)


	team_instances = relationship(
		'TeamInstanceModel',
		back_populates='conference_instance',
		lazy='selectin',
	)

	division_instances = relationship(
		'DivisionInstanceModel',
		back_populates='conference_instance',
		lazy='selectin',
	)


	league_instance = relationship(
		'LeagueInstanceModel',
		back_populates='conference_instances',
		uselist=False,
	)
	league_instance_id = Column(
		Integer,
		ForeignKey('league_instances.id'),
	)

	season_instance = relationship(
		'SeasonInstanceModel',
		back_populates='conference_instances',
		uselist=False,
	)
	season_instance_id = Column(
		Integer,
		ForeignKey('season_instances.id'),
	)


	

