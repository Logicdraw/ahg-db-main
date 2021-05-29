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

from app.models._many.program_instances_coaches import ProgramInstancesCoachesModel

from app.schemas._many.program_instances_coaches import (
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




program_instances_coaches_crud = CRUDProgramInstancesCoaches(ProgramInstancesCoachesModel)



