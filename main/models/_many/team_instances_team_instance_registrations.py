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



class TeamInstancesTeamInstanceRegistrationsModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'team_instances_team_instance_registrations'


	team_instance_id = Column(
		Integer,
		ForeignKey('team_instances.id'),
		primary_key=True,
	)

	team_instance_registration_id = Column(
		Integer,
		ForeignKey('team_instance_registrations.id'),
		primary_key=True,
	)



	team_instances_sc = relationship(
		'TeamInstanceModel',
		back_populates='team_instances_team_instance_registrations',
	)

	team_instance_registrations_sc = relationship(
		'TeamInstanceRegistrationModel',
		back_populates='team_instances_team_instance_registrations',
	)


	__mapper_args__ = {
		'eager_defaults': True,
	}





