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

from main.models._many.team_instances_adult_reps import TeamInstancesAdultRepsModel

from main.schemas._many.team_instances_adult_reps import (
	TeamInstancesAdultRepsSchemaCreate,
	TeamInstancesAdultRepsSchemaUpdate,
)



class CRUDTeamInstancesAdultReps(
	CRUDBase[
		TeamInstancesAdultRepsModel,
		TeamInstancesAdultRepsSchemaCreate,
		TeamInstancesAdultRepsSchemaUpdate,
	]):
	
	pass


team_instances_adult_reps_crud = CRUDTeamInstancesAdultReps(TeamInstancesAdultRepsModel)



