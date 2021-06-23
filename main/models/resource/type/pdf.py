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

from main.models._base.resource import (
	ResourceBaseModel,
)



from main.config import settings




class ResourcePDFModel(
	ResourceBaseModel,
	ResourceMixin,
):

	__tablename__ = 'resource_pdfs'


	id = Column(
		Integer,
		ForeignKey('resources.id'),
		primary_key=True,
		autoincrement=True,
	)


	pdf_url = Column(String)


	__mapper_args__ = {
		'polymorphic_identity': 'pdf',
		'eager_defaults': True,
	}



