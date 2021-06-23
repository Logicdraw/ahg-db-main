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



class SeasonModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'seasons'

	id = Column(Integer, primary_key=True, index=True)


	name = Column(String, nullable=False, index=True)


	season_instances = relationship(
		'SeasonInstanceModel',
		back_populates='seasons_sc',
		lazy='selectin',
	)


	leagues = relationship(
		'LeagueModel',
		back_populates='seasons_sc',
		lazy='selectin',
	)

	conferences = relationship(
		'ConferenceModel',
		back_populates='seasons_sc',
		lazy='selectin',
	)

	divisions = relationship(
		'DivisionModel',
		back_populates='seasons_sc',
		lazy='selectin',
	)

	teams = relationship(
		'TeamModel',
		back_populates='seasons_sc',
		lazy='selectin',
	)


	__mapper_args__ = {
		'eager_defaults': True,
	}



