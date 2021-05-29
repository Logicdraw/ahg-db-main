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



class ConferenceModel(Base, ResourceMixin):

	__tablename__ = 'conferences'

	id = Column(Integer, primary_key=True)


	name = Column(String, nullable=False, index=True)


	instances = relationship(
		'ConferenceInstanceModel',
		back_populates='conference',
		lazy='selectin',
	)


	teams = relationship(
		'TeamModel',
		back_populates='conference',
		lazy='selectin',
	)

	divisions = relationship(
		'DivisionModel',
		back_populates='conference',
		lazy='selectin',
	)


	season = relationship(
		'SeasonModel',
		back_populates='conferences',
		uselist=False,
	)
	season_id = Column(Integer, ForeignKey('seasons.id'))

	league = relationship(
		'LeagueModel',
		back_populates='conferences',
		uselist=False,
	)
	league_id = Column(Integer, ForeignKey('leagues.id'))



