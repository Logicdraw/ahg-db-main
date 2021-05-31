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

from main.models.data.camp.instance import CampInstanceModel

from main.schemas.data.camp.instance import (
	CampInstanceSchemaCreate,
	CampInstanceSchemaUpdate,
)




class CRUDCampInstance(
	CRUDBase[
		CampInstanceModel,
		CampInstanceSchemaCreate,
		CampInstanceSchemaUpdate,
	]):
	
	pass



camp_instance_crud = CRUDCampInstance(CampInstanceModel)



