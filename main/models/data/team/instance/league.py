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



class LeagueInstanceModel(Base, ResourceMixin):

	__tablename__ = 'league_instances'

	id = Column(Integer, primary_key=True)


	year_start = Column(Integer)

	year_end = Column(Integer)


	league = relationship(
		'LeagueModel',
		back_populates='instances',
		uselist=False,
	)
	league_id = Column(Integer, ForeignKey('leagues.id'))


	conferences = relationship(
		'ConferenceInstanceModel',
		back_populates='league',
		lazy='selectin',
	)

	divisions = relationship(
		'DivisionInstanceModel',
		back_populates='league',
		lazy='selectin',
	)

	teams = relationship(
		'TeamInstanceModel',
		back_populates='league',
		lazy='selectin',
	)


	season_instance = relationship(
		'SeasonInstanceModel',
		back_populates='leagues',
		uselist=False,
	)
	season_instance_id = Column(
		Integer,
		ForeignKey('season_instances.id'),
	)




