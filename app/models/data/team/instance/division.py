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



class DivisionInstanceModel(Base, ResourceMixin):

	__tablename__ = 'division_instances'

	id = Column(Integer, primary_key=True)


	year_start = Column(Integer)

	year_end = Column(Integer)


	division_id = Column(Integer, ForeignKey('divisions.id'))


	teams = relationship('TeamInstanceModel', backref='division', lazy='dynamic')


	season_instance_id = Column(Integer, ForeignKey('season_instances.id'))

	league_instance_id = Column(Integer, ForeignKey('league_instances.id'))

	conference_instance_id = Column(Integer, ForeignKey('conference_instances.id'))



