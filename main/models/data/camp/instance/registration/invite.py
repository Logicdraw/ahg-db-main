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



class CampInstanceRegistrationInviteModel(
	RegistrationInviteBaseModel,
	ResourceMixin,
):

	__tablename__ = 'camp_instance_registration_invites'


	camp_instances_sc = relationship(
		'CampInstanceModel',
		back_populates='camp_instance_registration_invites',
	)

	camp_instance_id = Column(
		Integer,
		ForeignKey('camp_instances.id'),
	)


	camp_instance_registrations_sc = relationship(
		'CampInstanceRegistrationModel',
		back_populates='camp_instance_registration_invites_sc',
	)

	camp_instance_registration_id = Column(
		Integer,
		ForeignKey('camp_instance_registrations.id'),
	)



	# Other options ???/
	__mapper_args__ = {
		'polymorphic_identity': 'camp_instance',
		'concrete': True,
		'eager_defaults': True,
	}




