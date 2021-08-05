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

from main.models._many.team_instances_team_instance_registrations import TeamInstancesTeamInstanceRegistrationsModel

from main.schemas._many.team_instances_team_instance_registrations import (
	TeamInstancesTeamInstanceRegistrationsSchemaCreate,
	TeamInstancesTeamInstanceRegistrationsSchemaUpdate,
)



class CRUDTeamInstancesTeamInstanceRegistrations(
	CRUDBase[
		TeamInstancesTeamInstanceRegistrationsModel,
		TeamInstancesTeamInstanceRegistrationsSchemaCreate,
		TeamInstancesTeamInstanceRegistrationsSchemaUpdate,
	]):
	
	pass



team_instances_team_instance_registrations_crud = CRUDTeamInstancesTeamInstanceRegistrations(TeamInstancesTeamInstanceRegistrationsModel)



