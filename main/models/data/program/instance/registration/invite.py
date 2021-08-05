from sqlalchemy import (
	Boolean,
	Column,
	ForeignKey,
	Integer,
	String,
	Float,
)

from sqlalchemy.orm import relationship

from main.database.base_class import Base

from main.utils.sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)


from main.models._base.registration_invite import (
	RegistrationInviteBaseModel,
)



class ProgramInstanceRegistrationInviteModel(
	RegistrationInviteBaseModel,
	ResourceMixin,
):

	__tablename__ = 'program_instance_registration_invites'


	program_instances_sc = relationship(
		'ProgramInstanceModel',
		back_populates='program_instance_registration_invites',
	)

	program_instance_id = Column(
		Integer,
		ForeignKey('program_instances.id'),
	)


	program_instance_registrations_sc = relationship(
		'ProgramInstanceRegistrationModel',
		back_populates='program_instance_registration_invites',
	)

	program_instance_registration_id = Column(
		Integer,
		ForeignKey('program_instance_registrations.id'),
	)



	# Other options ???/
	__mapper_args__ = {
		'polymorphic_identity': 'program_instance',
		'concrete': True,
		'eager_defaults': True,
	}




