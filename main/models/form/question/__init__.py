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

from main.database.base_class import Base

from lib.util_sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)

from sqlalchemy import JSON



from sqlalchemy.dialects.postgresql import JSONB

from sqlalchemy_json import mutable_json_type


from main.config import settings





class FormQuestionModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'form_questions'

	id = Column(Integer, primary_key=True, index=True)


	form = relationship(
		'FormModel',
		back_populates='questions',
		uselist=False,
	)
	form_id = Column(Integer, ForeignKey('forms.id'))


	answers = relationship(
		'FormEntryAnswerModel',
		back_populates='question',
		lazy='selectin',
	)


	label = Column(String)

	type = Column(String(50))


	is_active = Column(Boolean, default=True)


	__mapper_args__ = {
		'polymorphic_identity': 'form_questions',
		'polymorphic_on': type,
		'with_polymorphic': '*',
	}



class FormQuestionInputModel(FormQuestionModel):

	__tablename__ = 'form_question_inputs'

	id = Column(Integer, ForeignKey('form_questions.id'), primary_key=True)

	# max length ... ?

	__mapper_args__ = {
		'polymorphic_identity': 'form_question_inputs',
		'polymorphic_load': 'inline', # inline correct
	}



class FormQuestionTextareaModel(FormQuestionModel):

	__tablename__ = 'form_question_textareas'

	id = Column(Integer, ForeignKey('form_questions.id'), primary_key=True)

	# max length ... ?

	__mapper_args__ = {
		'polymorphic_identity': 'form_question_textareas',
		'polymorphic_load': 'inline',
	}




class FormQuestionSelectModel(FormQuestionModel):

	__tablename__ = 'form_question_selects'

	id = Column(Integer, ForeignKey('form_questions.id'), primary_key=True)
	
	select_is_multiple = Column(Boolean, default=False)


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

	__tablename__ = 'form_question_checkboxes'

	id = Column(Integer, ForeignKey('form_questions.id'), primary_key=True)

	__mapper_args__ = {
		'polymorphic_identity': 'form_question_checkboxes',
		'polymorphic_load': 'inline',
	}




class FormQuestionRadioModel(FormQuestionModel):

	__tablename__ = 'form_question_radios'

	id = Column(Integer, ForeignKey('form_questions.id'), primary_key=True)


	radio_answers = Column(
		mutable_json_type(
			dbtype=JSONB,
			nested=False,
		)
	)


	__mapper_args__ = {
		'polymorphic_identity': 'form_question_radios',
		'polymorphic_load': 'inline',
	}



