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



class DivisionModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'divisions'

	id = Column(
		Integer,
		primary_key=True,
	)


	name = Column(
		String,
		nullable=False,
		index=True,
	)


	division_instances = relationship(
		'DivisionInstanceModel',
		back_populates='divisions_sc',
		lazy='selectin',
	)


	teams = relationship(
		'TeamModel',
		back_populates='divisions_sc',
		lazy='selectin',
	)


	seasons_sc = relationship(
		'SeasonModel',
		back_populates='divisions',
		uselist=False,
	)
	
	season_id = Column(
		Integer, 
		ForeignKey('seasons.id'),
	)


	leagues_sc = relationship(
		'LeagueModel',
		back_populates='divisions',
	)

	league_id = Column(
		Integer,
		ForeignKey('leagues.id'),
	)


	conferences_sc = relationship(
		'ConferenceModel',
		back_populates='divisions',
	)

	conference_id = Column(
		Integer,
		ForeignKey('conferences.id'),
	)


	__mapper_args__ = {
		'eager_defaults': True,
	}



