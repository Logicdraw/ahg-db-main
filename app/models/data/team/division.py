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



class DivisionModel(Base, ResourceMixin):

	__tablename__ = 'divisions'

	id = Column(Integer, primary_key=True)


	name = Column(String, nullable=False, index=True)


	instances = relationship('DivisionInstanceModel', backref='division', lazy='dynamic')


	teams = relationship('TeamModel', backref='division', lazy='dynamic')


	season_id = Column(Integer, ForeignKey('seasons.id'))

	league_id = Column(Integer, ForeignKey('leagues.id'))

	conference_id = Column(Integer, ForeignKey('conferences.id'))





