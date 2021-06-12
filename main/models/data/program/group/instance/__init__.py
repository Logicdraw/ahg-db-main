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



class ProgramGroupInstanceModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'program_group_instances'

	id = Column(Integer, primary_key=True)


	program_instance = relationship(
		'ProgramInstanceModel',
		back_populates='groups',
		uselist=False,
	)
	program_instance_id = Column(Integer, ForeignKey('program_instances.id'))

	program_group = relationship(
		'ProgramGroupModel',
		back_populates='instances',
		uselist=False,
	)
	program_group_id = Column(Integer, ForeignKey('program_groups.id'))



	registrations = relationship(
		'ProgramInstanceRegistrationModel',
		back_populates='program_group_instance',
		lazy='selectin',
	)


	year_start = Column(Integer)

	year_end = Column(Integer)



