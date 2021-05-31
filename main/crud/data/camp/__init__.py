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

from main.models.data.camp import CampModel

from main.schemas.data.camp import (
	CampSchemaCreate,
	CampSchemaUpdate,
)




class CRUDCamp(
	CRUDBase[
		CampModel,
		CampSchemaCreate,
		CampSchemaUpdate,
	]):
	
	pass



camp_crud = CRUDCamp(CampModel)



