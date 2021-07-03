from sqlalchemy import (
	Boolean,
	Column,
	ForeignKey,
	Integer,
	String,
	Enum,
	Date,
)

from sqlalchemy.orm import (
	relationship,
	column_property,
)

from main.database.base_class import Base

from main.utils.sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)



class ResourceCategoryModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'resource_categories'

	id = Column(
		Integer,
		primary_key=True,
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


	resources = relationship(
		'ResourceBaseModel',
		back_populates='resource_categories_sc',
		lazy='selectin',
	)


	__mapper_args__ = {
		'eager_defaults': True,
	}


