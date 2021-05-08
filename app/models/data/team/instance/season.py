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



class SeasonInstanceModel(Base, ResourceMixin):

	__tablename__ = 'season_instances'

	id = Column(Integer, primary_key=True)


	year_start = Column(Integer)

	year_end = Column(Integer)
	

	season_id = Column(Integer, ForeignKey('seasons.id'))

	
	leagues = relationship('LeagueInstanceModel', backref='season', lazy='dynamic')

	conferences = relationship('ConferenceInstanceModel', backref='season', lazy='dynamic')

	divisions = relationship('DivisionInstanceModel', backref='season', lazy='dynamic')

	teams = relationship('TeamInstanceModel', backref='season', lazy='dynamic')



