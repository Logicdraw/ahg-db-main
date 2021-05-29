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



class SeasonModel(Base, ResourceMixin):

	__tablename__ = 'seasons'

	id = Column(Integer, primary_key=True, index=True)


	name = Column(String, nullable=False, index=True)


	instances = relationship(
		'SeasonInstanceModel',
		back_populates='season',
		lazy='selectin',
	)


	leagues = relationship(
		'LeagueModel',
		back_populates='season',
		lazy='selectin',
	)

	conferences = relationship(
		'ConferenceModel',
		back_populates='season',
		lazy='selectin',
	)

	divisions = relationship(
		'DivisionModel',
		back_populates='season',
		lazy='selectin',
	)

	teams = relationship(
		'TeamModel',
		back_populates='season',
		lazy='selectin',
	)




