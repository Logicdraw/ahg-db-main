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



class TeamInstanceRegistrationInviteModel(
	RegistrationInviteBaseModel,
	ResourceMixin,
):

	__tablename__ = 'team_instance_registration_invites'


	team_instances_sc = relationship(
		'TeamInstanceModel',
		back_populates='team_instance_registration_invites',
	)

	team_instance_id = Column(
		Integer,
		ForeignKey('team_instances.id'),
	)


	team_instance_registrations_sc = relationship(
		'TeamInstanceRegistrationModel',
		back_populates='team_instance_registration_invites_sc',
	)

	team_instance_registration_id = Column(
		Integer,
		ForeignKey('team_instance_registrations.id'),
	)



	# Other options ???/
	__mapper_args__ = {
		'polymorphic_identity': 'team_instance',
		'concrete': True,
		'eager_defaults': True,
	}




