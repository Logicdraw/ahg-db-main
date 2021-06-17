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

from main.models.resource.category import ResourceCategoryModel

from main.schemas.resource.category import (
	ResourceCategorySchemaCreate,
	ResourceCategorySchemaUpdate,
)




class CRUDResourceCategory(
	CRUDBase[
		ResourceCategoryModel,
		ResourceCategorySchemaCreate,
		ResourceCategorySchemaUpdate,
	]):
	
	pass



resource_category_crud = CRUDResourceCategory(ResourceCategoryModel)



