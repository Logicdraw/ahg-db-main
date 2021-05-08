from sqlalchemy import (
	Boolean,
	Column,
	ForeignKey,
	Integer,
	String,
	Text,
	JSON,
)

from sqlalchemy.orm import relationship

from app.database.base_class import Base

from lib.util_sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)




from sqlalchemy.dialects.postgresql import JSONB

from sqlalchemy_json import mutable_json_type


from app.config import get_settings
settings = get_settings()





class FormQuestionModel(Base, ResourceMixin):

	__tablename__ = 'form_questions'

	id = Column(Integer, primary_key=True, index=True)


	form_id = Column(Integer, ForeignKey('forms.id'))


	label = Column(String)

	type = Column(String(50))


	is_active = Column(Boolean, default=True)


	__mapper_args__ = {
		'polymorphic_identity': 'form_questions',
		'polymorphic_on': type,
	}



class FormQuestionInputModel(FormQuestionModel):

	__mapper_args__ = {
		'polymorphic_identity': 'form_question_inputs',
		'polymorphic_load': 'inline',
	}




class FormQuestionTextareaModel(FormQuestionModel):

	__mapper_args__ = {
		'polymorphic_identity': 'form_question_textareas',
		'polymorphic_load': 'inline',
	}




class FormQuestionSelectModel(FormQuestionModel):
	
	select_is_multiple = Column(Boolean, default=False)

	if settings.USE_SQLITE_FOR_TESTING:

		select_answers = Column(JSON)

	else:

		select_answers = Column(
			mutable_json_type(
				dbtype=JSONB,
				nested=False,
			)
		)

	__mapper_args__ = {
		'polymorphic_identity': 'form_question_selects',
		'polymorphic_load': 'inline',
	}



class FormQuestionCheckboxModel(FormQuestionModel):

	__mapper_args__ = {
		'polymorphic_identity': 'form_question_checkboxes',
		'polymorphic_load': 'inline',
	}




class FormQuestionRadioModel(FormQuestionModel):

	if settings.USE_SQLITE_FOR_TESTING:
		
		radio_answers = Column(JSON)

	else:

		radio_answers = Column(
			mutable_json_type(
				dbtype=JSONB,
				nested=False,
			)
		)

	# radio_answers = Column(JSON)

	__mapper_args__ = {
		'polymorphic_identity': 'form_question_radios',
		'polymorphic_load': 'inline',
	}



