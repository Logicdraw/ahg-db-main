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



class FormQuestionModel(
	AbstractConcreteBase,
	Base,
):

	id = Column(Integer, primary_key=True, index=True, autoincrement=True)


	@declared_attr
	def form(cls):
		return relationship('FormModel', back_populates='questions', uselist=False,)

	@declared_attr
	def form_id(cls):
		return Column(Integer, ForeignKey('forms.id'))



	label = Column(String)


	is_active = Column(Boolean, default=True)



class FormQuestionInputModel(
	FormQuestionModel,
	ResourceMixin,
):

	__tablename__ = 'form_question_inputs'


	# max length ... ?
	answers = relationship(
		'FormEntryAnswerInputModel',
		back_populates='question',
		lazy='selectin',
	)

	__mapper_args__ = {
		'polymorphic_identity': 'form_question_inputs',
		'concrete': True, # inline correct
	}



class FormQuestionTextareaModel(
	FormQuestionModel,
	ResourceMixin,
):

	__tablename__ = 'form_question_textareas'


	# max length ... ?
	answers = relationship(
		'FormEntryAnswerTextareaModel',
		back_populates='question',
		lazy='selectin',
	)

	__mapper_args__ = {
		'polymorphic_identity': 'form_question_textareas',
		'concrete': True,
	}




class FormQuestionSelectModel(
	FormQuestionModel,
	ResourceMixin,
):

	__tablename__ = 'form_question_selects'

	
	select_is_multiple = Column(Boolean, default=False)


	select_answers = Column(
		mutable_json_type(
			dbtype=JSONB,
			nested=False,
		)
	)

	answers = relationship(
		'FormEntryAnswerSelectModel',
		back_populates='question',
		lazy='selectin',
	)

	__mapper_args__ = {
		'polymorphic_identity': 'form_question_selects',
		'concrete': True,
	}



class FormQuestionCheckboxModel(
	FormQuestionModel,
	ResourceMixin,
):

	__tablename__ = 'form_question_checkboxes'


	answers = relationship(
		'FormEntryAnswerCheckboxModel',
		back_populates='question',
		lazy='selectin',
	)

	__mapper_args__ = {
		'polymorphic_identity': 'form_question_checkboxes',
		'concrete': True,
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


	answers = relationship(
		'FormEntryAnswerRadioModel',
		back_populates='question',
		lazy='selectin',
	)


	__mapper_args__ = {
		'polymorphic_identity': 'form_question_radios',
		'concrete': True,
	}


