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




class SpngSurveyCampInstanceModel(
	SpngSurveyBaseModel,
	ResourceMixin,
):
	# -- Camp
	__tablename__ = 'spng_survey_camp_instances'


	id = Column(
		Integer,
		ForeignKey('spng_surveys.id'),
		primary_key=True,
		autoincrement=True,
	)


	# default_camp_instance = relationship(
	# 	'CampInstanceModel',
	# 	uselist=False,
	# )
	# default_camp_instance_id = Column(
	# 	Integer,
	# 	ForeignKey('camp_instances.id'),
	# )


	# registrations --
	camp_instance_registrations = relationship(
		'CampInstanceRegistrationModel',
		back_populates='spng_survey_camp_instances_sc',
		lazy='selectin',
	)


	__mapper_args__ = {
		'polymorphic_identity': 'camp_instance',
		'eager_defaults': True,
	}



