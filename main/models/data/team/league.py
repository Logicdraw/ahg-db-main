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




class LeagueModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'leagues'

	id = Column(
		Integer,
		primary_key=True,
		index=True,
	)


	name = Column(
		String,
		nullable=False,
		index=True,
	)



	league_instances = relationship(
		'LeagueInstanceModel',
		back_populates='leagues_sc',
		lazy='selectin',
	)

	conferences = relationship(
		'ConferenceModel',
		back_populates='leagues_sc',
		lazy='selectin',
	)

	divisions = relationship(
		'DivisionModel',
		back_populates='leagues_sc',
		lazy='selectin',
	)

	teams = relationship(
		'TeamModel',
		back_populates='leagues_sc',
		lazy='selectin',
	)


	seasons_sc = relationship(
		'SeasonModel',
		back_populates='leagues',
		uselist=False,
	)

	season_id = Column(
		Integer,
		ForeignKey('seasons.id'),
	)


	__mapper_args__ = {
		'eager_defaults': True,
	}




