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



class ConferenceModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'conferences'

	id = Column(
		Integer,
		primary_key=True,
	)


	name = Column(
		String,
		nullable=False,
		index=True,
	)


	conference_instances = relationship(
		'ConferenceInstanceModel',
		back_populates='conferences_sc',
		lazy='selectin',
	)


	teams = relationship(
		'TeamModel',
		back_populates='conferences_sc',
		lazy='selectin',
	)

	divisions = relationship(
		'DivisionModel',
		back_populates='conferences_sc',
		lazy='selectin',
	)


	seasons_sc = relationship(
		'SeasonModel',
		back_populates='conferences',
	)

	season_id = Column(
		Integer,
		ForeignKey('seasons.id'),
	)


	leagues_sc = relationship(
		'LeagueModel',
		back_populates='conferences',
	)

	league_id = Column(
		Integer,
		ForeignKey('leagues.id'),
	)



	__mapper_args__ = {
		'eager_defaults': True,
	}


