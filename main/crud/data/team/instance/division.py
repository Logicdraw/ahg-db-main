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

from main.models.data.team.instance.division import DivisionInstanceModel

from main.schemas.data.team.instance.division import (
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



