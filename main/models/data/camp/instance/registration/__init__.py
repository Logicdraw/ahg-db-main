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

from lib.util_sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)



from main.models._base.registration import (
	RegistrationBaseModel,
	SpngRegistrationBase,
	SpngRegistrationFinancialsBase,
	PlayerRegistrationBase,
)


class CampInstanceRegistrationModel(
	RegistrationBaseModel,
	ResourceMixin,
	SpngRegistrationBase,
	SpngRegistrationFinancialsBase,
	PlayerRegistrationBase,
):

	__tablename__ = 'camp_instance_registrations'


	camp_instance_id = Column(
		Integer,
		ForeignKey('camp_instances.id'),
	)

	camp_instances_sc = relationship(
		'CampInstanceModel',
		back_populates='camp_instance_registrations',
		uselist=False,
	)


	# Optional :) - nice dropdown on interface --
	camp_group_instances_sc = relationship(
		'CampGroupInstanceModel',
		back_populates='camp_instance_registrations',
		uselist=False,
	)

	camp_group_instance_id = Column(
		Integer,
		ForeignKey('camp_group_instances.id'),
	)



	spng_survey_camps_sc = relationship(
		'SpngSurveyCampModel',
		back_populates='camp_instance_registrations',
		uselist=False,
	)
	spng_survey_camp_id = Column(
		Integer,
		ForeignKey('spng_survey_camps.id'),
	)


	# polymorphic identity --

	__mapper_args__ = {
		'polymorphic_identity': 'camp_instance',
		'concrete': True,
		'eager_defaults': True,
	}


	# other information

