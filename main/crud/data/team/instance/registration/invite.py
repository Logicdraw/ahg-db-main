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

from main.models.data.team.instance.registration.invite import TeamInstanceRegistrationInviteModel

from main.schemas.data.team.instance.registration.invite import (
	TeamInstanceRegistrationInviteSchemaCreate,
	TeamInstanceRegistrationInviteSchemaUpdate,
)




class CRUDTeamInstanceRegistrationInvite(
	CRUDBase[
		TeamInstanceRegistrationInviteModel,
		TeamInstanceRegistrationInviteSchemaCreate,
		TeamInstanceRegistrationInviteSchemaUpdate,
	]):
	
	pass



team_instance_registration_invite_crud = CRUDTeamInstanceRegistrationInvite(TeamInstanceRegistrationInviteModel)



