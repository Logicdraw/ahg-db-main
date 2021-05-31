from sqlalchemy import (
	Boolean,
	Column,
	ForeignKey,
	Integer,
	String,
	Text,
	Enum,
)

from sqlalchemy.orm import relationship

from main.database.base_class import Base

from lib.util_sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)


from collections import OrderedDict



class SpngSurveysSpngSurveyQuestionsModel(Base, ResourceMixin):

	__tablename__ = 'spng_surveys_spng_survey_questions'

	spng_survey_id = Column(Integer, ForeignKey('spng_surveys.id'), primary_key=True)
	spng_survey_question_id = Column(Integer, ForeignKey('spng_survey_questions.id'), primary_key=True)


	# Extra Data --
	included_in_db = Column(Boolean, default=True)


	spng_survey = relationship(
		'SpngSurveyBaseModel',
		back_populates='spng_survey_questions',
	)
	spng_survey_question = relationship(
		'SpngSurveyQuestionModel',
		back_populates='spng_surveys'
	)




