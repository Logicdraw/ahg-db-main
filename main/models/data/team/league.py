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




class LeagueModel(Base, ResourceMixin):

	__tablename__ = 'leagues'

	id = Column(Integer, primary_key=True, index=True)


	instances = relationship('LeagueInstanceModel', back_populates='league', lazy='selectin')


	conferences = relationship('ConferenceModel', back_populates='league', lazy='selectin')

	divisions = relationship('DivisionModel', back_populates='league', lazy='selectin')

	teams = relationship('TeamModel', back_populates='league', lazy='selectin')


	season = relationship(
		'SeasonModel',
		back_populates='leagues',
		uselist=False,
	)
	season_id = Column(Integer, ForeignKey('seasons.id'))


	name = Column(String, nullable=False, index=True)



	# ...


