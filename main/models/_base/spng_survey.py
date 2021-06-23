from sqlalchemy import (
	Boolean,
	Column,
	ForeignKey,
	Integer,
	String,
	Date,
	Text,
	Float,
	JSON,
)

from sqlalchemy.orm import relationship


from lib.util_sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)

from main.database.base_class import Base

from sqlalchemy.dialects.postgresql import JSONB

from sqlalchemy_json import mutable_json_type



from main.config import settings



# from sqlalchemy.ext.declarative import AbstractConcreteBase

# from sqlalchemy.ext.declarative import declared_attr



class SpngSurveyBaseModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'spng_surveys'

	id = Column(Integer, primary_key=True, index=True)

	
	survey_id = Column(Integer, index=True)

	name = Column(String, index=True)

	is_active = Column(Boolean, server_default='1')


	type = Column(String(50))


	spng_surveys_spng_survey_questions = relationship(
		'SpngSurveysSpngSurveyQuestionsModel',
		back_populates='spng_surveys_sc',
		lazy='selectin',
	)


	__mapper_args__ = {
		'polymorphic_identity': 'other',
		'polymorphic_on': type,
		'with_polymorphic': '*',
		'eager_defaults': True,
	}




