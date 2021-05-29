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



class DivisionModel(Base, ResourceMixin):

	__tablename__ = 'divisions'

	id = Column(Integer, primary_key=True)


	name = Column(String, nullable=False, index=True)


	instances = relationship(
		'DivisionInstanceModel',
		back_populates='division',
		lazy='selectin',
	)


	teams = relationship(
		'TeamModel',
		back_populates='division',
		lazy='selectin',
	)


	season = relationship(
		'SeasonModel',
		back_populates='divisions',
		uselist=False,
	)
	season_id = Column(Integer, ForeignKey('seasons.id'))

	league = relationship(
		'LeagueModel',
		back_populates='divisions',
		uselist=False,
	)
	league_id = Column(Integer, ForeignKey('leagues.id'))

	conference = relationship(
		'ConferenceModel',
		back_populates='divisions',
		uselist=False,
	)
	conference_id = Column(Integer, ForeignKey('conferences.id'))





