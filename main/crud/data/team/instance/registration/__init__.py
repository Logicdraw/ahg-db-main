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

from main.models.data.team.instance.registration import TeamInstanceRegistrationModel

from main.schemas.data.team.instance.registration import (
	TeamInstanceRegistrationSchemaCreate,
	TeamInstanceRegistrationSchemaUpdate,
)




class CRUDTeamInstanceRegistration(
	CRUDBase[
		TeamInstanceRegistrationModel,
		TeamInstanceRegistrationSchemaCreate,
		TeamInstanceRegistrationSchemaUpdate,
	]):
	
	pass



team_instance_registration_crud = CRUDTeamInstanceRegistration(TeamInstanceRegistrationModel)



