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

from app.models.data.external.spng_survey_camp import SpngSurveyCampModel

from app.schemas.data.external.spng_survey_camp import (
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



