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
	SpngRegistrationMixin,
	SpngRegistrationFinancialsMixin,
)



class ProgramInstanceRegistrationModel(
	RegistrationBaseModel,
	ResourceMixin,
	SpngRegistrationMixin,
	SpngRegistrationFinancialsMixin,
	PlayerRegistrationMixin,
):

	__tablename__ = 'program_instance_registrations'


	program_instances_sc = relationship(
		'ProgramInstanceModel',
		back_populates='program_instance_registrations',
		uselist=False,
	)
	program_instance_id = Column(
		Integer,
		ForeignKey('program_instances.id'),
	)
	

	# Optional :) - nice dropdown on interface --
	program_group_instances_sc = relationship(
		'ProgramGroupInstanceModel',
		back_populates='program_instance_registrations',
		uselist=False,
	)
	program_group_instance_id = Column(
		Integer,
		ForeignKey('program_group_instances.id'),
	)


	spng_survey_programs_sc = relationship(
		'SpngSurveyProgramModel',
		back_populates='program_instance_registrations',
		uselist=False,
	)
	spng_survey_program_id = Column(
		Integer,
		ForeignKey('spng_survey_programs.id'),
	)


	# polymorphic identity --

	__mapper_args__ = {
		'polymorphic_identity': 'program_instance',
		'concrete': True,
		'eager_defaults': True,
	}


	


