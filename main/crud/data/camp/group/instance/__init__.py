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

from main.models.data.camp.group.instance import CampGroupInstanceModel

from main.schemas.data.camp.group.instance import (
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



camp_group_instance_crud = CRUDCampGroupInstance(CampGroupInstanceModel)



