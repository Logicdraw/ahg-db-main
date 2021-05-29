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

from app.models.data.team.instance.registration import TeamInstanceRegistrationModel

from app.schemas.data.team.instance.registration import (
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



