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

from app.models.data.team.instance.registration.jersey_sponsor import TeamInstanceRegistrationJerseySponsorModel

from app.schemas.data.team.instance.registration.jersey_sponsor import (
	TeamInstanceRegistrationJerseySponsorSchemaCreate,
	TeamInstanceRegistrationJerseySponsorSchemaUpdate,
)




class CRUDTeamInstanceRegistrationJerseySponsor(
	CRUDBase[
		TeamInstanceRegistrationJerseySponsorModel,
		TeamInstanceRegistrationJerseySponsorSchemaCreate,
		TeamInstanceRegistrationJerseySponsorSchemaUpdate,
	]):
	
	pass



team_instance_registration_jersey_sponsor_crud = CRUDTeamInstanceRegistrationJerseySponsor(TeamInstanceRegistrationJerseySponsorModel)



