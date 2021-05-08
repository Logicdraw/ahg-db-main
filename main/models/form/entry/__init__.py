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


from main.config import get_settings
settings = get_settings()



# Form Entry


class FormEntryModel(Base, ResourceMixin):

	__tablename__ = 'form_entries'

	id = Column(Integer, primary_key=True, index=True)

	# --


