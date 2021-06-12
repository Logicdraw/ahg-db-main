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




class SpngSurveyCampModel(
	SpngSurveyBaseModel,
	ResourceMixin,
):
	# -- Camp
	__tablename__ = 'spng_survey_camps'


	id = Column(Integer, ForeignKey('spng_surveys.id'), primary_key=True)


	default_camp_instance = relationship(
		'CampInstanceModel',
		uselist=False,
	)
	default_camp_instance_id = Column(
		Integer,
		ForeignKey('camp_instances.id'),
	)


	# registrations --
	registrations = relationship(
		'CampInstanceRegistrationModel',
		back_populates='spng_survey_camp',
		lazy='selectin',
	)


	__mapper_args__ = {
		'polymorphic_identity': 'camp',
		'eager_defaults': True,
	}



