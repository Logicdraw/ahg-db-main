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

from sqlalchemy.dialects import postgresql


from main.config import settings




class SpngSurveyQuestionTableMapModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'spng_survey_question_table_maps'

	id = Column(Integer, primary_key=True, index=True)


	db_table_name = Column(String, index=True, nullable=False)
	# e.g. players

	db_table_column_name = Column(String, index=True, nullable=False)



	# relationships -- 


	spng_survey_questions_sc = relationship(
		'SpngSurveyQuestionModel',
		back_populates='spng_survey_question_table_maps',
		uselist=False,
	)

	# ForeignKey --
	spng_survey_question_id = Column(
		Integer,
		ForeignKey('spng_survey_questions.id'),
	)


	__mapper_args__ = {
		'eager_defaults': True,
	}

	# https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fthumbs.gfycat.com%2FBigheartedRealBobcat-size_restricted.gif&f=1&nofb=1
	# array


	# rel -- 
	# rel_holder -- ok !


	# relationships, columns, tables -- etc..



