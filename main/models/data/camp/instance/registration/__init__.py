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



from main.models._base.registration import (
	RegistrationBaseModel,
	SpngRegistrationMixin,
	RegistrationFinancialsMixin,
	SpngRegistrationFinancialsMixin,
	PlayerRegistrationMixin,
)


class CampInstanceRegistrationModel(
	RegistrationBaseModel,
	ResourceMixin,
	SpngRegistrationMixin,
	RegistrationFinancialsMixin,
	SpngRegistrationFinancialsMixin,
	PlayerRegistrationMixin,
):

	__tablename__ = 'camp_instance_registrations'


	camp_instances_camp_instance_registrations = relationship(
		'CampInstancesCampInstanceRegistrationsModel',
		back_populates='camp_instance_registrations_sc',
		lazy='selectin',
	)


	# Optional :) - nice dropdown on interface --
	camp_group_instances_sc = relationship(
		'CampGroupInstanceModel',
		back_populates='camp_instance_registrations',
	)

	camp_group_instance_id = Column(
		Integer,
		ForeignKey('camp_group_instances.id'),
	)



	spng_survey_camp_instances_sc = relationship(
		'SpngSurveyCampInstanceModel',
		back_populates='camp_instance_registrations',
	)
	
	spng_survey_camp_instance_id = Column(
		Integer,
		ForeignKey('spng_survey_camp_instances.id'),
	)



	# camp_instance_registration_invites_sc = relationship(
	# 	'CampInstanceRegistrationInviteModel',
	# 	back_populates='camp_instance_registrations_sc',
	# 	uselist=False,
	# )


	# polymorphic identity --

	__mapper_args__ = {
		'polymorphic_identity': 'camp_instance',
		'concrete': True,
		'eager_defaults': True,
	}


	# other information

