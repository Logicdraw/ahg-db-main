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



class ConferenceModel(Base, ResourceMixin):

	__tablename__ = 'conferences'

	id = Column(Integer, primary_key=True)


	name = Column(String, nullable=False, index=True)


	instances = relationship('ConferenceInstanceModel', backref='conference', lazy='dynamic')


	teams = relationship('TeamModel', backref='conference', lazy='dynamic')

	divisions = relationship('DivisionModel', backref='conference', lazy='dynamic')


	season_id = Column(Integer, ForeignKey('seasons.id'))

	league_id = Column(Integer, ForeignKey('leagues.id'))



