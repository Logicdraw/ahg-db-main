from sqlalchemy import (
	Boolean,
	Column,
	ForeignKey,
	Integer,
	String,
	Date,
	Text,
	Float,
	JSON,
)


from sqlalchemy.orm import relationship

from lib.util_sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)

from main.database.base_class import Base


from sqlalchemy.dialects.postgresql import JSONB

from sqlalchemy_json import mutable_json_type



from main.config import settings


from sqlalchemy.ext.declarative import AbstractConcreteBase



from sqlalchemy.ext.declarative import declared_attr



class ResourceBaseModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'resources'

	id = Column(
		Integer,
		primary_key=True,
		index=True,
		autoincrement=True,
	)

	
	is_live = Column(Boolean, server_default='1')


	name = Column(String)

	slug = Column(String)


	thumbnail_image_url = Column(String)


	type = Column(String(50))


	# Relationship -- one to one
	category_id = Column(
		Integer,
		ForeignKey('resource_categories.id'),
	)
	category = relationship(
		'ResourceCategoryModel',
		uselist=False,
	)


	__mapper_args__ = {
		'polymorphic_identity': 'other',
		'polymorphic_on': type,
		'with_polymorphic': '*',
		'eager_defaults': True,
	}




