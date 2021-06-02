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

from main.models._many.program_instances_coaches import ProgramInstancesCoachesModel

from main.schemas._many.program_instances_coaches import (
	ProgramInstancesCoachesSchemaCreate,
	ProgramInstancesCoachesSchemaUpdate,
)



class CRUDProgramInstancesCoaches(
	CRUDBase[
		ProgramInstancesCoachesModel,
		ProgramInstancesCoachesSchemaCreate,
		ProgramInstancesCoachesSchemaUpdate,
	]):

	async def get(
		self,
		db: AsyncSession,
		program_instance_id: int,
		coach_id: int,
	) -> Optional[ProgramInstancesCoachesModel]:
		# --

		result = await db.execute(
			select(ProgramInstancesCoachesModel).\
			filter_by(
				program_instance_id=program_instance_id,
				coach_id=coach_id,
			)
		)

		return result.scalars().first()


	def get_sync(
		self,
		db: AsyncSession,
		program_instance_id: int,
		coach_id: int,
	) -> Optional[ProgramInstancesCoachesModel]:
		# --

		result = db.execute(
			select(ProgramInstancesCoachesModel).\
			filter_by(
				program_instance_id=program_instance_id,
				coach_id=coach_id,
			)
		)

		return result.scalars().first()




program_instances_coaches_crud = CRUDProgramInstancesCoaches(ProgramInstancesCoachesModel)



