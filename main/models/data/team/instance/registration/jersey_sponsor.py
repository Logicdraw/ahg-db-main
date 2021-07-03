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



class TeamInstanceRegistrationJerseySponsorModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'team_instance_registration_jersey_sponsors'

	id = Column(
		Integer,
		primary_key=True,
	)



	team_instance_registrations_sc = relationship(
		'TeamInstanceRegistrationModel',
		back_populates='team_instance_registration_jersey_sponsors',
		uselist=False,
	)

	team_instance_registration_id = Column(
		Integer,
		ForeignKey('team_instance_registrations.id'),
	)



	name = Column(
		String,
		index=True,
	)

	amount = Column(
		Float,
	)


	# Other options ???/
	__mapper_args__ = {
		'eager_defaults': True,
	}




