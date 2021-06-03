# POLYMORPHIC -- 


from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.form.question import (
	form_question_crud,
)

from main.schemas.form.question import (
	FormQuestionSchemaCreate,
	FormQuestionSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest




@pytest.mark.asyncio
async def test_create_form_question(
	db: AsyncSession,
) -> None:
	# --

	pass



@pytest.mark.asyncio
async def test_create_sync_form_question(
	db: AsyncSession,
) -> None:
	# --

	pass



@pytest.mark.asyncio
async def test_get_form_question(
	db: AsyncSession,
) -> None:
	# --

	pass



@pytest.mark.asyncio
async def test_get_sync_form_question(
	db: AsyncSession,
) -> None:
	# --

	pass



@pytest.mark.asyncio
async def test_update_form_question(
	db: AsyncSession,
) -> None:
	# --

	pass



@pytest.mark.asyncio
async def test_update_sync_form_question(
	db: AsyncSession,
) -> None:
	# --

	pass



@pytest.mark.asyncio
async def test_delete_form_question(
	db: AsyncSession,
) -> None:
	# --

	pass



@pytest.mark.asyncio
async def test_delete_sync_form_question(
	db: AsyncSession,
) -> None:
	# --

	pass







