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




# Form Entry Answers


class FormEntryAnswerModel(Base, ResourceMixin):

	__tablename__ = 'form_entry_answers'

	id = Column(Integer, primary_key=True, index=True)


	entry_id = Column(Integer, ForeignKey('form_entries.id'))

	question_id = Column(Integer, ForeignKey('form_questions.id'))


	type = Column(String(50))


	__mapper_args__ = {
		'polymorphic_identity': 'form_entry_answers',
		'polymorphic_on': type,
	}





class FormEntryAnswerInputModel(FormEntryAnswerModel):

	input_answer = Column(String)

	__mapper_args__ = {
		'polymorphic_identity': 'form_entry_answer_inputs',
		'polymorphic_load': 'inline',
	}



class FormEntryAnswerTextareaModel(FormEntryAnswerModel):

	textarea_answer = Column(Text)
	
	__mapper_args__ = {
		'polymorphic_identity': 'form_entry_answer_textareas',
		'polymorphic_load': 'inline',
	}



class FormEntryAnswerSelectModel(FormEntryAnswerModel):

	# Selected --

	if settings.USE_SQLITE_FOR_TESTING:

		select_selected = Column(JSON)

	else:

		select_selected = Column(
			mutable_json_type(
				dbtype=JSONB,
				nested=False,
			)
		)

	# select_selected = Column(JSON)

	__mapper_args__ = {
		'polymorphic_identity': 'form_entry_answer_selects',
		'polymorphic_load': 'inline',
	}



class FormEntryAnswerCheckboxModel(FormEntryAnswerModel):
	
	checkbox_checked = Column(Boolean, default=False)

	__mapper_args__ = {
		'polymorphic_identity': 'form_entry_answer_checkboxes',
		'polymorphic_load': 'inline',
	}



class FormEntryAnswerRadioModel(FormEntryAnswerModel):

	if settings.USE_SQLITE_FOR_TESTING:

		radio_selected = Column(JSON)

	else:

		radio_selected = Column(
			mutable_json_type(
				dbtype=JSONB,
				nested=False,
			)
		)

	# radio_selected = Column(JSON)
	
	__mapper_args__ = {
		'polymorphic_identity': 'form_entry_answer_radios',
		'polymorphic_load': 'inline',
	}






