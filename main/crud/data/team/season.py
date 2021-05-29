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

from app.models.data.team.season import SeasonModel

from app.schemas.data.team.season import (
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



