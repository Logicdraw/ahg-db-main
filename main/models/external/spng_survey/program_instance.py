from sqlalchemy import (
	Boolean,
	Column,
	ForeignKey,
	Integer,
	String,
)

from sqlalchemy.orm import relationship

from main.database.base_class import Base

from main.utils.sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)

from main.models._base.spng_survey import SpngSurveyBaseModel



from main.config import settings




class SpngSurveyProgramInstanceModel(
	SpngSurveyBaseModel,
	ResourceMixin,
):
	# -- Program
	__tablename__ = 'spng_survey_program_instances'


	id = Column(
		Integer,
		ForeignKey('spng_surveys.id'),
		primary_key=True,
		autoincrement=True,
	)


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
		back_populates='spng_survey_program_instances_sc',
		lazy='selectin',
	)


	__mapper_args__ = {
		'polymorphic_identity': 'program_instance',
		'eager_defaults': True,
	}




