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

from main.utils.sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)


from collections import OrderedDict



class ProgramInstancesProgramInstanceRegistrationsModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'program_instances_program_instance_registrations'


	program_instance_id = Column(
		Integer,
		ForeignKey('program_instances.id'),
		primary_key=True,
	)

	program_instance_registration_id = Column(
		Integer,
		ForeignKey('program_instance_registrations.id'),
		primary_key=True,
	)



	program_instances_sc = relationship(
		'ProgramInstanceModel',
		back_populates='program_instances_program_instance_registrations',
	)

	program_instance_registrations_sc = relationship(
		'ProgramInstanceRegistrationModel',
		back_populates='program_instances_program_instance_registrations',
	)


	__mapper_args__ = {
		'eager_defaults': True,
	}





