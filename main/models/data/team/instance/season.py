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



class SeasonInstanceModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'season_instances'

	id = Column(Integer, primary_key=True)


	year_start = Column(Integer)

	year_end = Column(Integer)
	

	seasons_sc = relationship(
		'SeasonModel',
		back_populates='season_instances',
		uselist=False,
	)

	season_id = Column(
		Integer,
		ForeignKey('seasons.id'),
	)

	
	league_instances = relationship(
		'LeagueInstanceModel',
		back_populates='season_instances_sc',
		lazy='selectin',
	)

	conference_instances = relationship(
		'ConferenceInstanceModel',
		back_populates='season_instances_sc',
		lazy='selectin',
	)

	division_instances = relationship(
		'DivisionInstanceModel',
		back_populates='season_instances_sc',
		lazy='selectin',
	)

	team_instances = relationship(
		'TeamInstanceModel',
		back_populates='season_instances_sc',
		lazy='selectin',
	)


	__mapper_args__ = {
		'eager_defaults': True,
	}





