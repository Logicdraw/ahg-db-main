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



class SeasonModel(Base, ResourceMixin):

	__tablename__ = 'seasons'

	id = Column(Integer, primary_key=True, index=True)


	name = Column(String, nullable=False, index=True)


	instances = relationship('SeasonInstanceModel', backref='season', lazy='dynamic')


	leagues = relationship('LeagueModel', backref='season', lazy='dynamic')

	conferences = relationship('ConferenceModel', backref='season', lazy='dynamic')

	divisions = relationship('DivisionModel', backref='season', lazy='dynamic')

	teams = relationship('TeamModel', backref='season', lazy='dynamic')




