from sqlalchemy import (
	Boolean,
	Column,
	ForeignKey,
	Integer,
	String,
)

from sqlalchemy.orm import relationship

from app.database.base_class import Base

from lib.util_sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)


from app.config import get_settings
settings = get_settings()




# Form Entry --

class FormModel(Base, ResourceMixin):

	__tablename__ = 'forms'

	id = Column(Integer, primary_key=True, index=True)


	questions = relationship('FormQuestionModel', backref='form', lazy='dynamic')



