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

from main.models.data.team.season import SeasonModel

from main.schemas.data.team.season import (
	SeasonSchemaCreate,
	SeasonSchemaUpdate,
)




class CRUDSeason(
	CRUDBase[
		SeasonModel,
		SeasonSchemaCreate,
		SeasonSchemaUpdate,
	]):
	
	pass



season_crud = CRUDSeason(SeasonModel)



