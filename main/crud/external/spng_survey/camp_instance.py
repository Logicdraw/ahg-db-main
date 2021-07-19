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

from main.models.external.spng_survey.camp_instance import SpngSurveyCampInstanceModel

from main.schemas.external.spng_survey.camp_instance import (
	SpngSurveyCampInstanceSchemaCreate,
	SpngSurveyCampInstanceSchemaUpdate,
)



class CRUDSpngSurveyCampInstance(
	CRUDBase[
		SpngSurveyCampInstanceModel,
		SpngSurveyCampInstanceSchemaCreate,
		SpngSurveyCampInstanceSchemaUpdate,
	]):
	pass






spng_survey_camp_instance_crud = CRUDSpngSurveyCampInstance(SpngSurveyCampInstanceModel)



