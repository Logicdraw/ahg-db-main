from sqlalchemy import (
	Boolean,
	Column,
	ForeignKey,
	Integer,
	String,
	Date,
)

from sqlalchemy.orm import relationship

from main.database.base_class import Base

from lib.util_sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)



class CampGroupInstanceModel(Base, ResourceMixin):

	__tablename__ = 'camp_group_instances'

	id = Column(Integer, primary_key=True)


	camp_instance = relationship(
		'CampInstanceModel',
		back_populates='groups',
		uselist=False,
	)
	camp_instance_id = Column(Integer, ForeignKey('camp_instances.id'))


	camp_group = relationship(
		'CampGroupModel',
		back_populates='instances',
		uselist=False,
	)
	camp_group_id = Column(Integer, ForeignKey('camp_groups.id'))


	year_start = Column(Integer)

	year_end = Column(Integer)



