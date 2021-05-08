from sqlalchemy import (
	Boolean,
	Column,
	ForeignKey,
	Integer,
	String,
)

from sqlalchemy.orm import relationship

from app.database.base_class import Base

from lib.util_sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)




class LeagueModel(Base, ResourceMixin):

	__tablename__ = 'leagues'

	id = Column(Integer, primary_key=True, index=True)


	instances = relationship('LeagueInstanceModel', backref='league', lazy='dynamic')


	conferences = relationship('ConferenceModel', backref='league', lazy='dynamic')

	divisions = relationship('DivisionModel', backref='league', lazy='dynamic')

	teams = relationship('TeamModel', backref='league', lazy='dynamic')


	season_id = Column(Integer, ForeignKey('seasons.id'))


	name = Column(String, nullable=False, index=True)



	# ...


