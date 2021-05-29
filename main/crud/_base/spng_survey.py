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

from app.models._base.spng_survey import SpngSurveyBaseModel

from app.schemas._base.spng_survey import (
	SpngSurveyBaseSchemaCreate,
	SpngSurveyBaseSchemaUpdate,
)




class CRUDSpngSurveyBase(
	CRUDBase[
		SpngSurveyBaseModel,
		SpngSurveyBaseSchemaCreate,
		SpngSurveyBaseSchemaUpdate,
	]):
	
	pass



spng_survey_base_crud = CRUDSpngSurveyBase(SpngSurveyBaseModel)



