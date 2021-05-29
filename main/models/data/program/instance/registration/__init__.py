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
	PlayerRegistrationBase,
	SpngRegistrationBase,
	SpngRegistrationFinancialsBase,
)



class ProgramInstanceRegistrationModel(
	RegistrationBaseModel,
	SpngRegistrationBase,
	SpngRegistrationFinancialsBase,
	PlayerRegistrationBase,
):

	__tablename__ = 'program_instance_registrations'


	id = Column(Integer, ForeignKey('registrations.id'), primary_key=True)


	program_instance = relationship(
		'ProgramInstanceModel',
		back_populates='registrations',
		uselist=False,
	)
	program_instance_id = Column(
		Integer,
		ForeignKey('program_instances.id'),
	)
	

	# Optional :) - nice dropdown on interface --
	program_instance_group = relationship(
		'ProgramInstanceGroupModel',
		back_populates='registrations',
		uselist=False,
	)
	program_instance_group_id = Column(
		Integer,
		ForeignKey('program_instance_groups.id'),
	)


	spng_survey_program = relationship(
		'SpngSurveyProgramModel',
		back_populates='registrations',
		uselist=False,
	)
	spng_survey_program_id = Column(
		Integer,
		ForeignKey('spng_survey_programs.id'),
	)


	# polymorphic identity --

	__mapper_args__ = {
		'polymorphic_identity': 'program_instance',
	}




