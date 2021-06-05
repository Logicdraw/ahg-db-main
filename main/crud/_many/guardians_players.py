from typing import (
	Any,
	Dict,
	Optional,
	Union,
	List,
)


from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession



from main.crud.base import CRUDBase

from main.models._many.guardians_players import GuardiansPlayersModel

from main.schemas._many.guardians_players import (
	GuardiansPlayersSchemaCreate,
	GuardiansPlayersSchemaUpdate,
)



class CRUDGuardiansPlayers(
	CRUDBase[
		GuardiansPlayersModel,
		GuardiansPlayersSchemaCreate,
		GuardiansPlayersSchemaUpdate,
	]):

	pass


guardians_players_crud = CRUDGuardiansPlayers(GuardiansPlayersModel)



