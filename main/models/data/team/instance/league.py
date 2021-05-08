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



class LeagueInstanceModel(Base, ResourceMixin):

	__tablename__ = 'league_instances'

	id = Column(Integer, primary_key=True)


	year_start = Column(Integer)

	year_end = Column(Integer)


	league_id = Column(Integer, ForeignKey('leagues.id'))


	conferences = relationship('ConferenceInstanceModel', backref='league', lazy='dynamic')

	divisions = relationship('DivisionInstanceModel', backref='league', lazy='dynamic')

	teams = relationship('TeamInstanceModel', backref='league', lazy='dynamic')


	season_instance_id = Column(Integer, ForeignKey('season_instances.id'))



