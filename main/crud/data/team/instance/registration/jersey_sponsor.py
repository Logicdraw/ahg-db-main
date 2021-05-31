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

from main.models.data.team.instance.registration.jersey_sponsor import TeamInstanceRegistrationJerseySponsorModel

from main.schemas.data.team.instance.registration.jersey_sponsor import (
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



