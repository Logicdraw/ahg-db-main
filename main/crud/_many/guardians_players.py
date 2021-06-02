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

	async def get(
		self,
		db: AsyncSession,
		player_id: int,
		guardian_id: int,
	) -> Optional[GuardiansPlayersModel]:
		# --

		result = await db.execute(
			select(GuardiansPlayersModel).\
			filter_by(
				guardian_id=guardian_id,
				player_id=player_id,
			)
		)

		return result.scalars().first()


	def get_sync(
		self,
		db: AsyncSession,
		player_id: int,
		guardian_id: int,
	) -> Optional[GuardiansPlayersModel]:
		# --

		result = db.execute(
			select(GuardiansPlayersModel).\
			filter_by(
				guardian_id=guardian_id,
				player_id=player_id,
			)
		)

		return result.scalars().first()




guardians_players_crud = CRUDGuardiansPlayers(GuardiansPlayersModel)



