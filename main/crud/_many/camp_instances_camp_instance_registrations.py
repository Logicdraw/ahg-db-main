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

from main.models._many.camp_instances_camp_instance_registrations import CampInstancesCampInstanceRegistrationsModel

from main.schemas._many.camp_instances_camp_instance_registrations import (
	CampInstancesCampInstanceRegistrationsSchemaCreate,
	CampInstancesCampInstanceRegistrationsSchemaUpdate,
)



class CRUDCampInstancesCampInstanceRegistrations(
	CRUDBase[
		CampInstancesCampInstanceRegistrationsModel,
		CampInstancesCampInstanceRegistrationsSchemaCreate,
		CampInstancesCampInstanceRegistrationsSchemaUpdate,
	]):
	
	pass



camp_instances_camp_instance_registrations_crud = CRUDCampInstancesCampInstanceRegistrations(CampInstancesCampInstanceRegistrationsModel)



