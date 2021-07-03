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

from main.models._base.resource import (
	ResourceBaseModel,
)



from main.config import settings




class ResourceVideoModel(
	ResourceBaseModel,
	ResourceMixin,
):

	__tablename__ = 'resource_videos'


	id = Column(
		Integer,
		ForeignKey('resources.id'),
		primary_key=True,
		autoincrement=True,
	)


	video_url = Column(
		String,
	)


	__mapper_args__ = {
		'polymorphic_identity': 'video',
		'eager_defaults': True,
	}



