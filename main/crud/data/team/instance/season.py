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

from app.models.data.team.instance.season import SeasonInstanceModel

from app.schemas.data.team.instance.season import (
	SeasonInstanceSchemaCreate,
	SeasonInstanceSchemaUpdate,
)




class CRUDSeasonInstance(
	CRUDBase[
		SeasonInstanceModel,
		SeasonInstanceSchemaCreate,
		SeasonInstanceSchemaUpdate,
	]):
	
	pass



season_instance_crud = CRUDSeasonInstance(SeasonInstanceModel)



