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

from main.utils.sqlalchemy import (
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

	
	is_live = Column(
		Boolean,
		server_default='1',
	)


	name = Column(
		String,
	)

	slug = Column(
		String,
	)


	thumbnail_image_url = Column(
		String,
	)


	type = Column(
		String(50),
	)


	# Relationship -- one to one
	
	resource_category_id = Column(
		Integer,
		ForeignKey('resource_categories.id'),
	)

	resource_categories_sc = relationship(
		'ResourceCategoryModel',
		back_populates='resources',
	)


	__mapper_args__ = {
		'polymorphic_identity': 'other',
		'polymorphic_on': type,
		'with_polymorphic': '*',
		'eager_defaults': True,
	}




