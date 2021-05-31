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




# Form Entry Answers


class FormEntryAnswerModel(Base, ResourceMixin):

	__tablename__ = 'form_entry_answers'

	id = Column(Integer, primary_key=True, index=True)


	entry = relationship(
		'FormEntryModel',
		back_populates='answers',
		uselist=False,
	)
	entry_id = Column(Integer, ForeignKey('form_entries.id'))

	question = relationship(
		'FormQuestionModel',
		back_populates='answers',
		uselist=False,
	)
	question_id = Column(Integer, ForeignKey('form_questions.id'))


	type = Column(String(50))


	__mapper_args__ = {
		'polymorphic_identity': 'form_entry_answers',
		'polymorphic_on': type,
		'with_polymorphic': '*',
	}





class FormEntryAnswerInputModel(FormEntryAnswerModel):

	__tablename__ = 'form_entry_answer_inputs'

	id = Column(Integer, ForeignKey('form_entry_answers.id'), primary_key=True)

	input_answer = Column(String)

	__mapper_args__ = {
		'polymorphic_identity': 'form_entry_answer_inputs',
		'polymorphic_load': 'inline',
	}



class FormEntryAnswerTextareaModel(FormEntryAnswerModel):

	__tablename__ = 'form_entry_answer_textareas'

	id = Column(Integer, ForeignKey('form_entry_answers.id'), primary_key=True)

	textarea_answer = Column(Text)
	
	__mapper_args__ = {
		'polymorphic_identity': 'form_entry_answer_textareas',
		'polymorphic_load': 'inline',
	}



class FormEntryAnswerSelectModel(FormEntryAnswerModel):

	__tablename__ = 'form_entry_answer_selects'

	id = Column(Integer, ForeignKey('form_entry_answers.id'), primary_key=True)

	# Selected --

	select_selected = Column(
		mutable_json_type(
			dbtype=JSONB,
			nested=False,
		)
	)

	__mapper_args__ = {
		'polymorphic_identity': 'form_entry_answer_selects',
		'polymorphic_load': 'inline',
	}



class FormEntryAnswerCheckboxModel(FormEntryAnswerModel):

	__tablename__ = 'form_entry_answer_checkboxes'

	id = Column(Integer, ForeignKey('form_entry_answers.id'), primary_key=True)
	
	checkbox_checked = Column(Boolean, default=False)

	__mapper_args__ = {
		'polymorphic_identity': 'form_entry_answer_checkboxes',
		'polymorphic_load': 'inline',
	}



class FormEntryAnswerRadioModel(FormEntryAnswerModel):

	__tablename__ = 'form_entry_answer_radios'

	id = Column(Integer, ForeignKey('form_entry_answers.id'), primary_key=True)


	radio_selected = Column(
		mutable_json_type(
			dbtype=JSONB,
			nested=False,
		)
	)
	
	__mapper_args__ = {
		'polymorphic_identity': 'form_entry_answer_radios',
		'polymorphic_load': 'inline',
	}






