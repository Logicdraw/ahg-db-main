from sqlalchemy import (
	Boolean,
	Column,
	ForeignKey,
	Integer,
	String,
)

from sqlalchemy.orm import relationship

from main.database.base_class import Base

from lib.util_sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)

from main.models._base.spng_survey import SpngSurveyBaseModel



from main.config import settings




class SpngSurveyProgramModel(
	SpngSurveyBaseModel,
	ResourceMixin,
):
	# -- Program
	__tablename__ = 'spng_survey_programs'


	id = Column(Integer, ForeignKey('spng_surveys.id'), primary_key=True)


	# default_program_instance = relationship(
	# 	'ProgramInstanceModel',
	# 	uselist=False,
	# )
	# default_program_instance_id = Column(
	# 	Integer,
	# 	ForeignKey('program_instances.id'),
	# )


	# registrations --
	program_instance_registrations = relationship(
		'ProgramInstanceRegistrationModel',
		back_populates='spng_survey_programs_sc',
		lazy='selectin',
	)


	__mapper_args__ = {
		'polymorphic_identity': 'program',
		'eager_defaults': True,
	}




