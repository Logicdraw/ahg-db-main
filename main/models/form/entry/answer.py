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




# Form Entry Answers


class FormEntryAnswerModel(
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
	def form_entries_sc(cls):
		return relationship(
			'FormEntryModel',
			back_populates='form_entry_answers',
			uselist=False,
		)

	@declared_attr
	def form_entry_id(cls):
		return Column(
			Integer,
			ForeignKey('form_entries.id'),
		)


	__mapper_args__ = {
		'eager_defaults': True,
	}



class FormEntryAnswerInputModel(
	FormEntryAnswerModel,
	ResourceMixin,
):

	__tablename__ = 'form_entry_answer_inputs'


	input_answer = Column(
		String,
	)

	form_question_inputs_sc = relationship(
		'FormQuestionInputModel',
		back_populates='form_entry_answer_inputs',
		uselist=False,
	)

	form_question_input_id = Column(
		Integer,
		ForeignKey('form_question_inputs.id'),
	)

	__mapper_args__ = {
		'polymorphic_identity': 'form_entry_answer_inputs',
		'concrete': True,
		'eager_defaults': True,
	}



class FormEntryAnswerTextareaModel(
	FormEntryAnswerModel,
	ResourceMixin,
):

	__tablename__ = 'form_entry_answer_textareas'


	textarea_answer = Column(
		Text,
	)

	form_question_textareas_sc = relationship(
		'FormQuestionTextareaModel',
		back_populates='form_entry_answer_textareas',
		uselist=False,
	)

	form_question_textarea_id = Column(
		Integer,
		ForeignKey('form_question_textareas.id'),
	)
	
	__mapper_args__ = {
		'polymorphic_identity': 'form_entry_answer_textareas',
		'concrete': True,
		'eager_defaults': True,
	}



class FormEntryAnswerSelectModel(
	FormEntryAnswerModel,
	ResourceMixin,
):

	__tablename__ = 'form_entry_answer_selects'


	# Selected --

	# what does this even look like???
	select_selected = Column(
		mutable_json_type(
			dbtype=JSONB,
			nested=False,
		)
	)


	form_question_selects_sc = relationship(
		'FormQuestionSelectModel',
		back_populates='form_entry_answer_selects',
		uselist=False,
	)

	form_question_select_id = Column(
		Integer,
		ForeignKey('form_question_selects.id'),
	)
	

	__mapper_args__ = {
		'polymorphic_identity': 'form_entry_answer_selects',
		'concrete': True,
		'eager_defaults': True,
	}



class FormEntryAnswerCheckboxModel(
	FormEntryAnswerModel,
	ResourceMixin,
):

	__tablename__ = 'form_entry_answer_checkboxes'

	
	checkbox_checked = Column(
		Boolean,
		server_default='0',
	)

	form_question_checkboxes_sc = relationship(
		'FormQuestionCheckboxModel',
		back_populates='form_entry_answer_checkboxes',
		uselist=False,
	)

	form_question_checkbox_id = Column(
		Integer,
		ForeignKey('form_question_checkboxes.id'),
	)

	__mapper_args__ = {
		'polymorphic_identity': 'form_entry_answer_checkboxes',
		'concrete': True,
		'eager_defaults': True,
	}



class FormEntryAnswerRadioModel(
	FormEntryAnswerModel,
	ResourceMixin,
):

	__tablename__ = 'form_entry_answer_radios'


	radio_selected = Column(
		mutable_json_type(
			dbtype=JSONB,
			nested=False,
		)
	)

	form_question_radios_sc = relationship(
		'FormQuestionRadioModel',
		back_populates='form_entry_answer_radios',
		uselist=False,
	)

	form_question_radio_id = Column(
		Integer,
		ForeignKey('form_question_radios.id'),
	)
	
	
	__mapper_args__ = {
		'polymorphic_identity': 'form_entry_answer_radios',
		'concrete': True,
		'eager_defaults': True,
	}



