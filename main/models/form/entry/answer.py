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


from sqlalchemy.ext.declarative import AbstractConcreteBase

from sqlalchemy.ext.declarative import declared_attr




# Form Entry Answers


class FormEntryAnswerModel(
	AbstractConcreteBase,
	Base,
):

	id = Column(Integer, primary_key=True, index=True, autoincrement=True)
	

	@declared_attr
	def entry(cls):
		return relationship('FormEntryModel', back_populates='answers', uselist=False,)

	@declared_attr
	def entry_id(cls):
		return Column(Integer, ForeignKey('form_entries.id'))




class FormEntryAnswerInputModel(
	FormEntryAnswerModel,
	ResourceMixin,
):

	__tablename__ = 'form_entry_answer_inputs'


	input_answer = Column(String)

	question = relationship(
		'FormQuestionInputModel',
		back_populates='answers',
		uselist=False,
	)

	question_id = Column(Integer, ForeignKey('form_question_inputs.id'))

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


	textarea_answer = Column(Text)

	question = relationship(
		'FormQuestionTextareaModel',
		back_populates='answers',
		uselist=False,
	)

	question_id = Column(Integer, ForeignKey('form_question_textareas.id'))
	
	__mapper_args__ = {
		'polymorphic_identity': 'form_entry_answer_textareas',
		'concrete': True,
	}



class FormEntryAnswerSelectModel(
	FormEntryAnswerModel,
	ResourceMixin,
):

	__tablename__ = 'form_entry_answer_selects'


	# Selected --

	select_selected = Column(
		mutable_json_type(
			dbtype=JSONB,
			nested=False,
		)
	)


	question = relationship(
		'FormQuestionSelectModel',
		back_populates='answers',
		uselist=False,
	)

	question_id = Column(Integer, ForeignKey('form_question_selects.id'))
	

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

	
	checkbox_checked = Column(Boolean, server_default='0')

	question = relationship(
		'FormQuestionCheckboxModel',
		back_populates='answers',
		uselist=False,
	)

	question_id = Column(Integer, ForeignKey('form_question_checkboxes.id'))

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

	question = relationship(
		'FormQuestionRadioModel',
		back_populates='answers',
		uselist=False,
	)

	question_id = Column(Integer, ForeignKey('form_question_radios.id'))
	
	__mapper_args__ = {
		'polymorphic_identity': 'form_entry_answer_radios',
		'concrete': True,
		'eager_defaults': True,
	}



