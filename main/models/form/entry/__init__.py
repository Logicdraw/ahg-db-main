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


from main.config import settings



# Form Entry


class FormEntryModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'form_entries'

	id = Column(Integer, primary_key=True, index=True)


	slug = Column(String, unique=True, index=True)

	# --

	forms_sc = relationship(
		'FormModel',
		back_populates='form_entries',
		uselist=False,
	)
	form_id = Column(Integer, ForeignKey('forms.id'))


	# which form ? id ...

	form_entry_answers = relationship(
		'FormEntryAnswerModel',
		back_populates='form_entries_sc',
		lazy='selectin',
	)


	__mapper_args__ = {
		'eager_defaults': True,
	}




