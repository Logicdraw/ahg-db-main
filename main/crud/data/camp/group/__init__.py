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

from app.models.data.camp.group import CampGroupModel

from app.schemas.data.camp.group import (
	CampGroupSchemaCreate,
	CampGroupSchemaUpdate,
)




class CRUDCampGroup(
	CRUDBase[
		CampGroupModel,
		CampGroupSchemaCreate,
		CampGroupSchemaUpdate,
	]):
	
	pass



camp_group_crud = CRUDCampGroup(CampGroupModel)



