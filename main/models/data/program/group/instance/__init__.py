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

from main.utils.sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)



class ProgramGroupInstanceModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'program_group_instances'

	id = Column(
		Integer,
		primary_key=True,
	)


	program_instances_sc = relationship(
		'ProgramInstanceModel',
		back_populates='program_group_instances',
		uselist=False,
	)

	program_instance_id = Column(
		Integer,
		ForeignKey('program_instances.id'),
	)

	program_groups_sc = relationship(
		'ProgramGroupModel',
		back_populates='program_group_instances',
		uselist=False,
	)

	program_group_id = Column(
		Integer,
		ForeignKey('program_groups.id'),
	)



	program_instance_registrations = relationship(
		'ProgramInstanceRegistrationModel',
		back_populates='program_group_instances_sc',
		lazy='selectin',
	)


	year_start = Column(
		Integer,
	)

	year_end = Column(
		Integer,
	)


	__mapper_args__ = {
		'eager_defaults': True,
	}


	
