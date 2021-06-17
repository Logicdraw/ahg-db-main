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

from main.models._base.resource import ResourceBaseModel

from main.schemas._base.resource import (
	ResourceBaseSchemaCreate,
	ResourceBaseSchemaUpdate,
)




class CRUDResourceBase(
	CRUDBase[
		ResourceBaseModel,
		ResourceBaseSchemaCreate,
		ResourceBaseSchemaUpdate,
	]):
	
	pass



resource_base_crud = CRUDResourceBase(ResourceBaseModel)



