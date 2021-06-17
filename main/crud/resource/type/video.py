from typing import (
	Any,
	Dict,
	Optional,
	Union,
	List,
)


from sqlalchemy.ext.asyncio import AsyncSession


from sqlalchemy import (
	func,
	or_,
)


from main.crud.base import CRUDBase

from main.models.resource.type.video import ResourceVideoModel

from main.schemas.resource.type.video import (
	ResourceVideoSchemaCreate,
	ResourceVideoSchemaUpdate,
)




class CRUDResourceVideo(
	CRUDBase[
		ResourceVideoModel,
		ResourceVideoSchemaCreate,
		ResourceVideoSchemaUpdate,
	]):
	
	pass



resource_video_crud = CRUDResourceVideo(ResourceVideoModel)



