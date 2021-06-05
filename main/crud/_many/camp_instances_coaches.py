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

from main.models._many.camp_instances_coaches import CampInstancesCoachesModel

from main.schemas._many.camp_instances_coaches import (
	CampInstancesCoachesSchemaCreate,
	CampInstancesCoachesSchemaUpdate,
)



class CRUDCampInstancesCoaches(
	CRUDBase[
		CampInstancesCoachesModel,
		CampInstancesCoachesSchemaCreate,
		CampInstancesCoachesSchemaUpdate,
	]):




camp_instances_coaches_crud = CRUDCampInstancesCoaches(CampInstancesCoachesModel)



