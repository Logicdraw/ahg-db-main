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



class ConferenceInstanceModel(Base, ResourceMixin):

	__tablename__ = 'conference_instances'

	id = Column(Integer, primary_key=True)


	year_start = Column(Integer)

	year_end = Column(Integer)


	conference_id = Column(Integer, ForeignKey('conferences.id'))


	teams = relationship('TeamInstanceModel', backref='conference_instance', lazy='dynamic')

	divisions = relationship('DivisionInstanceModel', backref='conference_instance', lazy='dynamic')


	league_instance_id = Column(Integer, ForeignKey('league_instances.id'))

	season_instance_id = Column(Integer, ForeignKey('season_instances.id'))


	

