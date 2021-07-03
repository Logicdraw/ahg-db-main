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

from main.utils.sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)

from sqlalchemy import JSON



from sqlalchemy.dialects.postgresql import JSONB

from sqlalchemy_json import mutable_json_type


from main.config import settings



from sqlalchemy.ext.declarative import AbstractConcreteBase


from sqlalchemy.ext.declarative import declared_attr



class FormQuestionModel(
	AbstractConcreteBase,
	Base,
):

	id = Column(
		Integer,
		primary_key=True,
		index=True,
		autoincrement=True,
	)


	@declared_attr
	def forms_sc(cls):
		return relationship(
			'FormModel',
			back_populates='form_questions',
			uselist=False,
		)

	@declared_attr
	def form_id(cls):
		return Column(
			Integer,
			ForeignKey('forms.id'),
		)



	label = Column(
		String,
	)

	is_active = Column(
		Boolean,
		server_default='1',
	)


	__mapper_args__ = {
		'eager_defaults': True,
	}




class FormQuestionInputModel(
	FormQuestionModel,
	ResourceMixin,
):

	__tablename__ = 'form_question_inputs'


	# max length ... ?
	form_entry_answer_inputs = relationship(
		'FormEntryAnswerInputModel',
		back_populates='form_question_inputs_sc',
		lazy='selectin',
	)

	__mapper_args__ = {
		'polymorphic_identity': 'form_question_inputs',
		'concrete': True, # inline correct
		'eager_defaults': True,
	}



class FormQuestionTextareaModel(
	FormQuestionModel,
	ResourceMixin,
):

	__tablename__ = 'form_question_textareas'


	# max length ... ?
	form_entry_answer_textareas = relationship(
		'FormEntryAnswerTextareaModel',
		back_populates='form_question_textareas_sc',
		lazy='selectin',
	)

	__mapper_args__ = {
		'polymorphic_identity': 'form_question_textareas',
		'concrete': True,
		'eager_defaults': True,
	}




class FormQuestionSelectModel(
	FormQuestionModel,
	ResourceMixin,
):

	__tablename__ = 'form_question_selects'

	
	select_is_multiple = Column(
		Boolean,
		server_default='0',
	)


	select_answers = Column(
		mutable_json_type(
			dbtype=JSONB,
			nested=False,
		)
	)

	form_entry_answer_selects = relationship(
		'FormEntryAnswerSelectModel',
		back_populates='form_question_selects_sc',
		lazy='selectin',
	)

	__mapper_args__ = {
		'polymorphic_identity': 'form_question_selects',
		'concrete': True,
		'eager_defaults': True,
	}



class FormQuestionCheckboxModel(
	FormQuestionModel,
	ResourceMixin,
):

	__tablename__ = 'form_question_checkboxes'


	form_entry_answer_checkboxes = relationship(
		'FormEntryAnswerCheckboxModel',
		back_populates='form_question_checkboxes_sc',
		lazy='selectin',
	)

	__mapper_args__ = {
		'polymorphic_identity': 'form_question_checkboxes',
		'concrete': True,
		'eager_defaults': True,
	}




class FormQuestionRadioModel(
	FormQuestionModel,
	ResourceMixin,
):

	__tablename__ = 'form_question_radios'


	radio_answers = Column(
		mutable_json_type(
			dbtype=JSONB,
			nested=False,
		)
	)


	form_entry_answer_radios = relationship(
		'FormEntryAnswerRadioModel',
		back_populates='form_question_radios_sc',
		lazy='selectin',
	)


	__mapper_args__ = {
		'polymorphic_identity': 'form_question_radios',
		'concrete': True,
		'eager_defaults': True,
	}


