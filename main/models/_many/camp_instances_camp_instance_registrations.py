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



class CampInstancesCampInstanceRegistrationsModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'camp_instances_camp_instance_registrations'


	camp_instance_id = Column(
		Integer,
		ForeignKey('camp_instances.id'),
		primary_key=True,
	)

	camp_instance_registration_id = Column(
		Integer,
		ForeignKey('camp_instance_registrations.id'),
		primary_key=True,
	)



	camp_instances_sc = relationship(
		'CampInstanceModel',
		back_populates='camp_instances_camp_instance_registrations',
	)

	camp_instance_registrations_sc = relationship(
		'CampInstanceRegistrationModel',
		back_populates='camp_instances_camp_instance_registrations',
	)


	__mapper_args__ = {
		'eager_defaults': True,
	}





