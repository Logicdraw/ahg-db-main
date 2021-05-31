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

from main.models.data.team.division import DivisionModel

from main.schemas.data.team.division import (
	DivisionSchemaCreate,
	DivisionSchemaUpdate,
)




class CRUDDivision(
	CRUDBase[
		DivisionModel,
		DivisionSchemaCreate,
		DivisionSchemaUpdate,
	]):
	
	pass



division_crud = CRUDDivision(DivisionModel)



