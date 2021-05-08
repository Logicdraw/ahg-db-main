from sqlalchemy import (
	Boolean,
	Column,
	ForeignKey,
	Integer,
	String,
	Date,
)

from sqlalchemy.orm import relationship

from app.database.base_class import Base

from lib.util_sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)



class CampInstanceGroupModel(Base, ResourceMixin):

	__tablename__ = 'camp_instance_groups'

	id = Column(Integer, primary_key=True)


	camp_instance_id = Column(Integer, ForeignKey('camp_instances.id'))

	camp_group_id = Column(Integer, ForeignKey('camp_groups.id'))


	year_start = Column(Integer)

	year_end = Column(Integer)



