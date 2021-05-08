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



# Gamesheet --

class GSMetaModel(Base, ResourceMixin):

	__tablename__ = 'gs_meta'

	id = Column(Integer, primary_key=True, index=True)

	access_token_encoded = Column(String)


