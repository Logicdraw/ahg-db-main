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
	SpngRegistrationBase,
	SpngRegistrationFinancialsBase,
	PlayerRegistrationBase,
):

	__tablename__ = 'camp_instance_registrations'

	id = Column(Integer, ForeignKey('registrations.id'), primary_key=True)


	camp_instance_id = Column(Integer, ForeignKey('camp_instances.id'))
	camp_instance = relationship(
		'CampInstanceModel',
		back_populates='registrations',
		uselist=False,
	)


	# Optional :) - nice dropdown on interface --
	camp_group_instance = relationship(
		'CampGroupInstanceModel',
		back_populates='registrations',
		uselist=False,
	)
	camp_group_instance_id = Column(Integer, ForeignKey('camp_group_instances.id'))



	spng_survey_camp = relationship(
		'SpngSurveyCampModel',
		back_populates='registrations',
		uselist=False,
	)
	spng_survey_camp_id = Column(
		Integer,
		ForeignKey('spng_survey_camps.id'),
	)


	# polymorphic identity --

	__mapper_args__ = {
		'polymorphic_identity': 'camp_instance',
	}


	# other information

