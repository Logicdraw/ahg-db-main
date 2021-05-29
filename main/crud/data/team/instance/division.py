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


from app.crud.base import CRUDBase

from app.models.data.team.instance.division import DivisionInstanceModel

from app.schemas.data.team.instance.division import (
	DivisionInstanceSchemaCreate,
	DivisionInstanceSchemaUpdate,
)




class CRUDDivisionInstance(
	CRUDBase[
		DivisionInstanceModel,
		DivisionInstanceSchemaCreate,
		DivisionInstanceSchemaUpdate,
	]):
	
	pass



division_instance_crud = CRUDDivisionInstance(DivisionInstanceModel)



