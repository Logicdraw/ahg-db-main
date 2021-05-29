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

from app.models.data.camp.group.instance import CampGroupInstanceModel

from app.schemas.data.camp.group.instance import (
	CampGroupInstanceSchemaCreate,
	CampGroupInstanceSchemaUpdate,
)




class CRUDCampGroupInstance(
	CRUDBase[
		CampGroupInstanceModel,
		CampGroupInstanceSchemaCreate,
		CampGroupInstanceSchemaUpdate,
	]):
	
	pass



camp_group_crud = CRUDCampGroupInstance(CampGroupInstanceModel)



