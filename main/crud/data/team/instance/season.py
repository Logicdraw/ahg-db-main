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

from main.models.data.team.instance.season import SeasonInstanceModel

from main.schemas.data.team.instance.season import (
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



