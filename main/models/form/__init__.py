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




# Form Entry --

class FormModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'forms'

	id = Column(Integer, primary_key=True, index=True)


	title = Column(String(500), index=True, nullable=False)

	description = Column(String, nullable=True)


	has_deadline = Column(Boolean, server_default='0')

	deadline_on = Column(AwareDateTime())



	questions = relationship(
		'FormQuestionModel',
		back_populates='form',
		lazy='selectin',
	)


	entries = relationship(
		'FormEntryModel',
		back_populates='form',
		lazy='selectin',
	)


