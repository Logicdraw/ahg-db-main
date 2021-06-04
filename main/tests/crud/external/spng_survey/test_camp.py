# Polymorphic :) !


from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.external.spng_survey.camp import (
	spng_survey_camp_crud,
)

from main.schemas.external.spng_survey.camp import (
	SpngSurveyCampSchemaCreate,
	SpngSurveyCampSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest



@pytest.mark.asyncio
async def test_create_spng_survey_camp(
	db: AsyncSession,
) -> None:
	# --
	
	name = random_lower_string()
	is_active = True
	type = 'camp'

	spng_survey_camp_in = SpngSurveyCampSchemaCreate(
		name=name,
		is_active=is_active,
		type=type,
	)

	spng_survey_camp = await spng_survey_camp_crud.create(
		db=db,
		obj_in=spng_survey_camp_in,
	)

	assert spng_survey_camp.name == name
	assert spng_survey_camp.is_active == is_active
	assert spng_survey_camp.type == type



@pytest.mark.asyncio
async def test_create_sync_spng_survey_camp(
	db: AsyncSession,
) -> None:
	# --

	name = random_lower_string()
	is_active = True
	type = 'camp'

	spng_survey_camp_in = SpngSurveyCampSchemaCreate(
		name=name,
		is_active=is_active,
		type=type,
	)

	spng_survey_camp = await db.run_sync(
		spng_survey_camp_crud.create_sync,
		obj_in=spng_survey_camp_in,
	)

	assert spng_survey_camp.name == name
	assert spng_survey_camp.is_active == is_active
	assert spng_survey_camp.type == type



@pytest.mark.asyncio
async def test_get_spng_survey_camp(
	db: AsyncSession,
) -> None:
	# --

	pass



@pytest.mark.asyncio
async def test_get_sync_spng_survey_camp(
	db: AsyncSession,
) -> None:
	# --

	pass



@pytest.mark.asyncio
async def test_update_spng_survey_camp(
	db: AsyncSession,
) -> None:
	# --

	pass



@pytest.mark.asyncio
async def test_update_sync_spng_survey_camp(
	db: AsyncSession,
) -> None:
	# --

	pass



@pytest.mark.asyncio
async def test_delete_spng_survey_camp(
	db: AsyncSession,
) -> None:
	# --

	pass



@pytest.mark.asyncio
async def test_delete_sync_spng_survey_camp(
	db: AsyncSession,
) -> None:
	# --

	pass





