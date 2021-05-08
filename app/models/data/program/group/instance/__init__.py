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



class ProgramInstanceGroupModel(Base, ResourceMixin):

	__tablename__ = 'program_instance_groups'

	id = Column(Integer, primary_key=True)


	program_instance_id = Column(Integer, ForeignKey('program_instances.id'))

	program_group_id = Column(Integer, ForeignKey('program_groups.id'))


	year_start = Column(Integer)

	year_end = Column(Integer)



