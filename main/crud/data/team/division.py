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

from app.models.data.team.division import DivisionModel

from app.schemas.data.team.division import (
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



