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

from app.models.data.person.player import PlayerModel

from app.schemas.data.person.player import (
	PlayerSchemaCreate,
	PlayerSchemaUpdate,
)




class CRUDPlayer(
	CRUDBase[
		PlayerModel,
		PlayerSchemaCreate,
		PlayerSchemaUpdate,
	]):
	
	pass



player_crud = CRUDPlayer(PlayerModel)



