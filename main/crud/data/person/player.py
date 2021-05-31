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

from main.models.data.person.player import PlayerModel

from main.schemas.data.person.player import (
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



