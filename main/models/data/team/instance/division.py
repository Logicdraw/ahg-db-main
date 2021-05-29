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



class DivisionInstanceModel(Base, ResourceMixin):

	__tablename__ = 'division_instances'

	id = Column(Integer, primary_key=True)


	year_start = Column(Integer)

	year_end = Column(Integer)


	division = relationship(
		'DivisionModel',
		back_populates='instances',
		uselist=False,
	)
	division_id = Column(Integer, ForeignKey('divisions.id'))


	teams = relationship(
		'TeamInstanceModel',
		back_populates='division',
		lazy='selectin',
	)


	season_instance = relationship(
		'SeasonInstanceModel',
		back_populates='divisions',
		uselist=False,
	)
	season_instance_id = Column(Integer, ForeignKey('season_instances.id'))

	league_instance = relationship(
		'LeagueInstanceModel',
		back_populates='divisions',
		uselist=False,
	)
	league_instance_id = Column(Integer, ForeignKey('league_instances.id'))

	conference_instance = relationship(
		'ConferenceInstanceModel',
		back_populates='divisions',
		uselist=False,
	)
	conference_instance_id = Column(Integer, ForeignKey('conference_instances.id'))




