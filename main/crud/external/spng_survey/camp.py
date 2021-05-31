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

from main.models.external.spng_survey.camp import SpngSurveyCampModel

from main.schemas.external.spng_survey.camp import (
	SpngSurveyCampSchemaCreate,
	SpngSurveyCampSchemaUpdate,
)



class CRUDSpngSurveyCamp(
	CRUDBase[
		SpngSurveyCampModel,
		SpngSurveyCampSchemaCreate,
		SpngSurveyCampSchemaUpdate,
	]):
	pass






spng_survey_camp_crud = CRUDSpngSurveyCamp(SpngSurveyCampModel)



