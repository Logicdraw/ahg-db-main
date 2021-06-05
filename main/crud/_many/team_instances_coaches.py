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

from main.models._many.team_instances_coaches import TeamInstancesCoachesModel

from main.schemas._many.team_instances_coaches import (
	TeamInstancesCoachesSchemaCreate,
	TeamInstancesCoachesSchemaUpdate,
)



class CRUDTeamInstancesCoaches(
	CRUDBase[
		TeamInstancesCoachesModel,
		TeamInstancesCoachesSchemaCreate,
		TeamInstancesCoachesSchemaUpdate,
	]):
	
	pass


team_instances_coaches_crud = CRUDTeamInstancesCoaches(TeamInstancesCoachesModel)



