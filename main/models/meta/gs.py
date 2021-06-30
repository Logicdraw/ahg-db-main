from sqlalchemy import (
	Boolean,
	Column,
	ForeignKey,
	Integer,
	String,
)

from sqlalchemy.orm import relationship

from main.database.base_class import Base

from main.utils.sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)


from main.config import settings



# Gamesheet --

class GSMetaModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'gs_meta'

	id = Column(Integer, primary_key=True, index=True)


	access_token_encoded = Column(String)


	__mapper_args__ = {
		'eager_defaults': True,
	}
	
