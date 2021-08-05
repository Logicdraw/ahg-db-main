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
	PlayerRegistrationMixin,
	RegistrationFinancialsMixin,
	SpngRegistrationMixin,
	SpngRegistrationFinancialsMixin,
)



class ProgramInstanceRegistrationModel(
	RegistrationBaseModel,
	ResourceMixin,
	SpngRegistrationMixin,
	RegistrationFinancialsMixin,
	SpngRegistrationFinancialsMixin,
	PlayerRegistrationMixin,
):

	__tablename__ = 'program_instance_registrations'


	program_instances_program_instance_registrations = relationship(
		'ProgramInstancesProgramInstanceRegistrationsModel',
		back_populates='program_instance_registrations_sc',
		lazy='selectin',
	)
	

	# Optional :) - nice dropdown on interface --
	program_group_instances_sc = relationship(
		'ProgramGroupInstanceModel',
		back_populates='program_instance_registrations',
	)

	program_group_instance_id = Column(
		Integer,
		ForeignKey('program_group_instances.id'),
	)


	spng_survey_program_instances_sc = relationship(
		'SpngSurveyProgramInstanceModel',
		back_populates='program_instance_registrations',
	)
	
	spng_survey_program_instance_id = Column(
		Integer,
		ForeignKey('spng_survey_program_instances.id'),
	)


	# program_instance_registration_invites_sc = relationship(
	# 	'ProgramInstanceRegistrationInviteModel',
	# 	back_populates='program_instance_registrations_sc',
	# 	uselist=False,
	# )


	# polymorphic identity --

	__mapper_args__ = {
		'polymorphic_identity': 'program_instance',
		'concrete': True,
		'eager_defaults': True,
	}


	


