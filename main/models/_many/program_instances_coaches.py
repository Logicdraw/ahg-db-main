from sqlalchemy import (
	Boolean,
	Column,
	ForeignKey,
	Integer,
	String,
	Text,
	Enum,
)

from sqlalchemy.orm import relationship

from main.database.base_class import Base

from lib.util_sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)


from collections import OrderedDict




class ProgramInstancesCoachesModel(Base, ResourceMixin):

	__tablename__ = 'program_instances_coaches'

	program_instance_id = Column(Integer, ForeignKey('program_instances.id'), primary_key=True)
	coach_id = Column(Integer, ForeignKey('coaches.id'), primary_key=True)


	role = Column(String)


	program_instance = relationship('ProgramInstanceModel', back_populates='coaches')
	coach = relationship('CoachModel', back_populates='program_instances')

