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

from sqlalchemy.dialects import postgresql


from sqlalchemy import JSON


from sqlalchemy.dialects.postgresql import JSONB

from sqlalchemy_json import mutable_json_type



from main.config import settings




class SpngSurveyQuestionModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'spng_survey_questions'

	id = Column(Integer, primary_key=True, index=True)


	# Many To Many with SpngSurvey -- |~|
	spng_surveys = relationship(
		'SpngSurveysSpngSurveyQuestionsModel',
		back_populates='spng_survey_question',
		lazy='selectin',
	)


	table_maps = relationship(
		'SpngSurveyQuestionTableMapModel',
		back_populates='spng_survey_question',
		lazy='selectin',
		cascade='all, delete', # Correct > ???
	)






	# Formatting!

	# Date --

	# date options ...


	# -- -- --


	use_answer_text_mappings = Column(Boolean)

	if settings.USE_SQLITE_FOR_TESTING:

		answer_text_mappings = Column(JSON)

	else:

		shared_question_ids = Column(postgresql.ARRAY(Integer))

		answer_text_mappings = Column(
			mutable_json_type(
				dbtype=JSONB,
				nested=False,
			)
		)
		"""
		Example:

		answers = {
			'no': 'False',
			'yes': 'True',
			'no_non': 'False',
			'yes_oui': 'True',
			'non': 'False',
			'out': 'True',
		}
		# Always -- put booleans in capital strings --
		# Pydantic will make the transition to boolean
		# Pydantic - ...
		"""






