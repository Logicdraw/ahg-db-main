# POLYMORPHIC -- 


from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.form.question import (
	form_question_input_crud,
	form_question_textarea_crud,
	form_question_select_crud,
	form_question_checkbox_crud,
	form_question_radio_crud,
)

from main.schemas.form.question import (
	FormQuestionInputSchemaCreate,
	FormQuestionInputSchemaUpdate,
	FormQuestionTextareaSchemaCreate,
	FormQuestionTextareaSchemaUpdate,
	FormQuestionSelectSchemaCreate,
	FormQuestionSelectSchemaUpdate,
	FormQuestionCheckboxSchemaCreate,
	FormQuestionCheckboxSchemaUpdate,
	FormQuestionRadioSchemaCreate,
	FormQuestionRadioSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest





# Input --



@pytest.mark.asyncio
async def test_create_form_question_input(
	db: AsyncSession,
) -> None:
	# --
	
	label = random_lower_string()
	is_active = True

	form_question_input_in = FormQuestionInputSchemaCreate(
		label=label,
		is_active=is_active,
	)

	form_question_input = await form_question_input_crud.create(
		db=db,
		obj_in=form_question_input_in,
	)

	assert form_question_input.label == label
	assert form_question_input.is_active == is_active



@pytest.mark.asyncio
async def test_create_sync_form_question_input(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True

	form_question_input_in = FormQuestionInputSchemaCreate(
		label=label,
		is_active=is_active,
	)

	form_question_input = await db.run_sync(
		form_question_input_crud.create_sync,
		obj_in=form_question_input_in,
	)

	assert form_question_input.label == label
	assert form_question_input.is_active == is_active



@pytest.mark.asyncio
async def test_get_form_question_input(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True

	form_question_input_in = FormQuestionInputSchemaCreate(
		label=label,
		is_active=is_active,
	)

	form_question_input = await form_question_input_crud.create(
		db=db,
		obj_in=form_question_input_in,
	)

	form_question_input_2 = await form_question_input_crud.get(
		db=db,
		id=form_question_input.id,
	)

	assert form_question_input_2
	assert jsonable_encoder(form_question_input_2) == jsonable_encoder(form_question_input)



@pytest.mark.asyncio
async def test_get_sync_form_question_input(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True

	form_question_input_in = FormQuestionInputSchemaCreate(
		label=label,
		is_active=is_active,
	)

	form_question_input = await db.run_sync(
		form_question_input_crud.create_sync,
		obj_in=form_question_input_in,
	)

	form_question_input_2 = await db.run_sync(
		form_question_input_crud.get_sync,
		id=form_question_input.id,
	)

	assert form_question_input_2
	assert jsonable_encoder(form_question_input_2) == jsonable_encoder(form_question_input)



@pytest.mark.asyncio
async def test_update_form_question_input(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True

	form_question_input_in = FormQuestionInputSchemaCreate(
		label=label,
		is_active=is_active,
	)

	form_question_input = await form_question_input_crud.create(
		db=db,
		obj_in=form_question_input_in,
	)


	new_label = random_lower_string()
	
	form_question_input_in_update = FormQuestionInputSchemaUpdate(
		label=new_label,
	)

	form_question_input_2 = await form_question_input_crud.update(
		db=db,
		db_obj=form_question_input,
		obj_in=form_question_input_in_update,
	)

	assert form_question_input_2
	assert form_question_input_2.label == new_label



@pytest.mark.asyncio
async def test_update_sync_form_question_input(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True

	form_question_input_in = FormQuestionInputSchemaCreate(
		label=label,
		is_active=is_active,
	)

	form_question_input = await db.run_sync(
		form_question_input_crud.create_sync,
		obj_in=form_question_input_in,
	)


	new_label = random_lower_string()
	
	form_question_input_in_update = FormQuestionInputSchemaUpdate(
		label=new_label,
	)

	form_question_input_2 = await db.run_sync(
		form_question_input_crud.update_sync,
		db_obj=form_question_input,
		obj_in=form_question_input_in_update,
	)

	assert form_question_input_2
	assert form_question_input_2.label == new_label



@pytest.mark.asyncio
async def test_delete_form_question_input(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True

	form_question_input_in = FormQuestionInputSchemaCreate(
		label=label,
		is_active=is_active,
	)

	form_question_input = await form_question_input_crud.create(
		db=db,
		obj_in=form_question_input_in,
	)

	form_question_input_2 = await form_question_input_crud.delete(
		db=db,
		id=form_question_input.id,
	)

	form_question_input_3 = await form_question_input_crud.get(
		db=db,
		id=form_question_input.id,
	)


	assert form_question_input_3 is None
	assert form_question_input_2.id == form_question_input.id



@pytest.mark.asyncio
async def test_delete_sync_form_question_input(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True

	form_question_input_in = FormQuestionInputSchemaCreate(
		label=label,
		is_active=is_active,
	)

	form_question_input = await db.run_sync(
		form_question_input_crud.create_sync,
		obj_in=form_question_input_in,
	)

	form_question_input_2 = await db.run_sync(
		form_question_input_crud.delete_sync,
		id=form_question_input.id,
	)

	form_question_input_3 = await db.run_sync(
		form_question_input_crud.get_sync,
		id=form_question_input.id,
	)


	assert form_question_input_3 is None
	assert form_question_input_2.id == form_question_input.id




# Textarea --



@pytest.mark.asyncio
async def test_create_form_question_textarea(
	db: AsyncSession,
) -> None:
	# --
	
	label = random_lower_string()
	is_active = True

	form_question_textarea_in = FormQuestionTextareaSchemaCreate(
		label=label,
		is_active=is_active,
	)

	form_question_textarea = await form_question_textarea_crud.create(
		db=db,
		obj_in=form_question_textarea_in,
	)

	assert form_question_textarea.label == label
	assert form_question_textarea.is_active == is_active



@pytest.mark.asyncio
async def test_create_sync_form_question_textarea(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True

	form_question_textarea_in = FormQuestionTextareaSchemaCreate(
		label=label,
		is_active=is_active,
	)

	form_question_textarea = await db.run_sync(
		form_question_textarea_crud.create_sync,
		obj_in=form_question_textarea_in,
	)

	assert form_question_textarea.label == label
	assert form_question_textarea.is_active == is_active



@pytest.mark.asyncio
async def test_get_form_question_textarea(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True

	form_question_textarea_in = FormQuestionTextareaSchemaCreate(
		label=label,
		is_active=is_active,
	)

	form_question_textarea = await form_question_textarea_crud.create(
		db=db,
		obj_in=form_question_textarea_in,
	)

	form_question_textarea_2 = await form_question_textarea_crud.get(
		db=db,
		id=form_question_textarea.id,
	)

	assert form_question_textarea_2
	assert jsonable_encoder(form_question_textarea_2) == jsonable_encoder(form_question_textarea)



@pytest.mark.asyncio
async def test_get_sync_form_question_textarea(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True

	form_question_textarea_in = FormQuestionTextareaSchemaCreate(
		label=label,
		is_active=is_active,
	)

	form_question_textarea = await db.run_sync(
		form_question_textarea_crud.create_sync,
		obj_in=form_question_textarea_in,
	)

	form_question_textarea_2 = await db.run_sync(
		form_question_textarea_crud.get_sync,
		id=form_question_textarea.id,
	)

	assert form_question_textarea_2
	assert jsonable_encoder(form_question_textarea_2) == jsonable_encoder(form_question_textarea)



@pytest.mark.asyncio
async def test_update_form_question_textarea(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True

	form_question_textarea_in = FormQuestionTextareaSchemaCreate(
		label=label,
		is_active=is_active,
	)

	form_question_textarea = await form_question_textarea_crud.create(
		db=db,
		obj_in=form_question_textarea_in,
	)


	new_label = random_lower_string()
	
	form_question_textarea_in_update = FormQuestionTextareaSchemaUpdate(
		label=new_label,
	)

	form_question_textarea_2 = await form_question_textarea_crud.update(
		db=db,
		db_obj=form_question_textarea,
		obj_in=form_question_textarea_in_update,
	)

	assert form_question_textarea_2
	assert form_question_textarea_2.label == new_label



@pytest.mark.asyncio
async def test_update_sync_form_question_textarea(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True

	form_question_textarea_in = FormQuestionTextareaSchemaCreate(
		label=label,
		is_active=is_active,
	)

	form_question_textarea = await db.run_sync(
		form_question_textarea_crud.create_sync,
		obj_in=form_question_textarea_in,
	)


	new_label = random_lower_string()
	
	form_question_textarea_in_update = FormQuestionTextareaSchemaUpdate(
		label=new_label,
	)

	form_question_textarea_2 = await db.run_sync(
		form_question_textarea_crud.update_sync,
		db_obj=form_question_textarea,
		obj_in=form_question_textarea_in_update,
	)

	assert form_question_textarea_2
	assert form_question_textarea_2.label == new_label



@pytest.mark.asyncio
async def test_delete_form_question_textarea(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True

	form_question_textarea_in = FormQuestionTextareaSchemaCreate(
		label=label,
		is_active=is_active,
	)

	form_question_textarea = await form_question_textarea_crud.create(
		db=db,
		obj_in=form_question_textarea_in,
	)

	form_question_textarea_2 = await form_question_textarea_crud.delete(
		db=db,
		id=form_question_textarea.id,
	)

	form_question_textarea_3 = await form_question_textarea_crud.get(
		db=db,
		id=form_question_textarea.id,
	)


	assert form_question_textarea_3 is None
	assert form_question_textarea_2.id == form_question_textarea.id



@pytest.mark.asyncio
async def test_delete_sync_form_question_textarea(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True

	form_question_textarea_in = FormQuestionTextareaSchemaCreate(
		label=label,
		is_active=is_active,
	)

	form_question_textarea = await db.run_sync(
		form_question_textarea_crud.create_sync,
		obj_in=form_question_textarea_in,
	)

	form_question_textarea_2 = await db.run_sync(
		form_question_textarea_crud.delete_sync,
		id=form_question_textarea.id,
	)

	form_question_textarea_3 = await db.run_sync(
		form_question_textarea_crud.get_sync,
		id=form_question_textarea.id,
	)


	assert form_question_textarea_3 is None
	assert form_question_textarea_2.id == form_question_textarea.id




# Select --



@pytest.mark.asyncio
async def test_create_form_question_select(
	db: AsyncSession,
) -> None:
	# --
	
	label = random_lower_string()
	is_active = True
	select_is_multiple = True
	select_answers = {
		'a': 'abc',
	}

	form_question_select_in = FormQuestionSelectSchemaCreate(
		label=label,
		is_active=is_active,
		select_is_multiple=select_is_multiple,
		select_answers=select_answers,
	)

	form_question_select = await form_question_select_crud.create(
		db=db,
		obj_in=form_question_select_in,
	)

	assert form_question_select.label == label
	assert form_question_select.is_active == is_active



@pytest.mark.asyncio
async def test_create_sync_form_question_select(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True
	select_is_multiple = True
	select_answers = {
		'a': 'abc',
	}

	form_question_select_in = FormQuestionSelectSchemaCreate(
		label=label,
		is_active=is_active,
		select_is_multiple=select_is_multiple,
		select_answers=select_answers,
	)

	form_question_select = await db.run_sync(
		form_question_select_crud.create_sync,
		obj_in=form_question_select_in,
	)

	assert form_question_select.label == label
	assert form_question_select.is_active == is_active



@pytest.mark.asyncio
async def test_get_form_question_select(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True
	select_is_multiple = True
	select_answers = {
		'a': 'abc',
	}

	form_question_select_in = FormQuestionSelectSchemaCreate(
		label=label,
		is_active=is_active,
		select_is_multiple=select_is_multiple,
		select_answers=select_answers,
	)

	form_question_select = await form_question_select_crud.create(
		db=db,
		obj_in=form_question_select_in,
	)

	form_question_select_2 = await form_question_select_crud.get(
		db=db,
		id=form_question_select.id,
	)

	assert form_question_select_2
	assert jsonable_encoder(form_question_select_2) == jsonable_encoder(form_question_select)



@pytest.mark.asyncio
async def test_get_sync_form_question_select(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True
	select_is_multiple = True
	select_answers = {
		'a': 'abc',
	}

	form_question_select_in = FormQuestionSelectSchemaCreate(
		label=label,
		is_active=is_active,
		select_is_multiple=select_is_multiple,
		select_answers=select_answers,
	)

	form_question_select = await db.run_sync(
		form_question_select_crud.create_sync,
		obj_in=form_question_select_in,
	)

	form_question_select_2 = await db.run_sync(
		form_question_select_crud.get_sync,
		id=form_question_select.id,
	)

	assert form_question_select_2
	assert jsonable_encoder(form_question_select_2) == jsonable_encoder(form_question_select)



@pytest.mark.asyncio
async def test_update_form_question_select(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True
	select_is_multiple = True
	select_answers = {
		'a': 'abc',
	}

	form_question_select_in = FormQuestionSelectSchemaCreate(
		label=label,
		is_active=is_active,
		select_is_multiple=select_is_multiple,
		select_answers=select_answers,
	)

	form_question_select = await form_question_select_crud.create(
		db=db,
		obj_in=form_question_select_in,
	)


	new_label = random_lower_string()
	
	form_question_select_in_update = FormQuestionSelectSchemaUpdate(
		label=new_label,
	)

	form_question_select_2 = await form_question_select_crud.update(
		db=db,
		db_obj=form_question_select,
		obj_in=form_question_select_in_update,
	)

	assert form_question_select_2
	assert form_question_select_2.label == new_label



@pytest.mark.asyncio
async def test_update_sync_form_question_select(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True
	select_is_multiple = True
	select_answers = {
		'a': 'abc',
	}

	form_question_select_in = FormQuestionSelectSchemaCreate(
		label=label,
		is_active=is_active,
		select_is_multiple=select_is_multiple,
		select_answers=select_answers,
	)

	form_question_select = await db.run_sync(
		form_question_select_crud.create_sync,
		obj_in=form_question_select_in,
	)


	new_label = random_lower_string()
	
	form_question_select_in_update = FormQuestionSelectSchemaUpdate(
		label=new_label,
	)

	form_question_select_2 = await db.run_sync(
		form_question_select_crud.update_sync,
		db_obj=form_question_select,
		obj_in=form_question_select_in_update,
	)

	assert form_question_select_2
	assert form_question_select_2.label == new_label



@pytest.mark.asyncio
async def test_delete_form_question_select(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True
	select_is_multiple = True
	select_answers = {
		'a': 'abc',
	}

	form_question_select_in = FormQuestionSelectSchemaCreate(
		label=label,
		is_active=is_active,
		select_is_multiple=select_is_multiple,
		select_answers=select_answers,
	)

	form_question_select = await form_question_select_crud.create(
		db=db,
		obj_in=form_question_select_in,
	)

	form_question_select_2 = await form_question_select_crud.delete(
		db=db,
		id=form_question_select.id,
	)

	form_question_select_3 = await form_question_select_crud.get(
		db=db,
		id=form_question_select.id,
	)


	assert form_question_select_3 is None
	assert form_question_select_2.id == form_question_select.id



@pytest.mark.asyncio
async def test_delete_sync_form_question_select(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True
	select_is_multiple = True
	select_answers = {
		'a': 'abc',
	}

	form_question_select_in = FormQuestionSelectSchemaCreate(
		label=label,
		is_active=is_active,
		select_is_multiple=select_is_multiple,
		select_answers=select_answers,
	)

	form_question_select = await db.run_sync(
		form_question_select_crud.create_sync,
		obj_in=form_question_select_in,
	)

	form_question_select_2 = await db.run_sync(
		form_question_select_crud.delete_sync,
		id=form_question_select.id,
	)

	form_question_select_3 = await db.run_sync(
		form_question_select_crud.get_sync,
		id=form_question_select.id,
	)


	assert form_question_select_3 is None
	assert form_question_select_2.id == form_question_select.id




# Checkbox --



@pytest.mark.asyncio
async def test_create_form_question_checkbox(
	db: AsyncSession,
) -> None:
	# --
	
	label = random_lower_string()
	is_active = True

	form_question_checkbox_in = FormQuestionCheckboxSchemaCreate(
		label=label,
		is_active=is_active,
	)

	form_question_checkbox = await form_question_checkbox_crud.create(
		db=db,
		obj_in=form_question_checkbox_in,
	)

	assert form_question_checkbox.label == label
	assert form_question_checkbox.is_active == is_active



@pytest.mark.asyncio
async def test_create_sync_form_question_checkbox(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True

	form_question_checkbox_in = FormQuestionCheckboxSchemaCreate(
		label=label,
		is_active=is_active,
	)

	form_question_checkbox = await db.run_sync(
		form_question_checkbox_crud.create_sync,
		obj_in=form_question_checkbox_in,
	)

	assert form_question_checkbox.label == label
	assert form_question_checkbox.is_active == is_active



@pytest.mark.asyncio
async def test_get_form_question_checkbox(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True

	form_question_checkbox_in = FormQuestionCheckboxSchemaCreate(
		label=label,
		is_active=is_active,
	)

	form_question_checkbox = await form_question_checkbox_crud.create(
		db=db,
		obj_in=form_question_checkbox_in,
	)

	form_question_checkbox_2 = await form_question_checkbox_crud.get(
		db=db,
		id=form_question_checkbox.id,
	)

	assert form_question_checkbox_2
	assert jsonable_encoder(form_question_checkbox_2) == jsonable_encoder(form_question_checkbox)



@pytest.mark.asyncio
async def test_get_sync_form_question_checkbox(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True

	form_question_checkbox_in = FormQuestionCheckboxSchemaCreate(
		label=label,
		is_active=is_active,
	)

	form_question_checkbox = await db.run_sync(
		form_question_checkbox_crud.create_sync,
		obj_in=form_question_checkbox_in,
	)

	form_question_checkbox_2 = await db.run_sync(
		form_question_checkbox_crud.get_sync,
		id=form_question_checkbox.id,
	)

	assert form_question_checkbox_2
	assert jsonable_encoder(form_question_checkbox_2) == jsonable_encoder(form_question_checkbox)



@pytest.mark.asyncio
async def test_update_form_question_checkbox(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True

	form_question_checkbox_in = FormQuestionCheckboxSchemaCreate(
		label=label,
		is_active=is_active,
	)

	form_question_checkbox = await form_question_checkbox_crud.create(
		db=db,
		obj_in=form_question_checkbox_in,
	)


	new_label = random_lower_string()
	
	form_question_checkbox_in_update = FormQuestionCheckboxSchemaUpdate(
		label=new_label,
	)

	form_question_checkbox_2 = await form_question_checkbox_crud.update(
		db=db,
		db_obj=form_question_checkbox,
		obj_in=form_question_checkbox_in_update,
	)

	assert form_question_checkbox_2
	assert form_question_checkbox_2.label == new_label



@pytest.mark.asyncio
async def test_update_sync_form_question_checkbox(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True

	form_question_checkbox_in = FormQuestionCheckboxSchemaCreate(
		label=label,
		is_active=is_active,
	)

	form_question_checkbox = await db.run_sync(
		form_question_checkbox_crud.create_sync,
		obj_in=form_question_checkbox_in,
	)


	new_label = random_lower_string()
	
	form_question_checkbox_in_update = FormQuestionCheckboxSchemaUpdate(
		label=new_label,
	)

	form_question_checkbox_2 = await db.run_sync(
		form_question_checkbox_crud.update_sync,
		db_obj=form_question_checkbox,
		obj_in=form_question_checkbox_in_update,
	)

	assert form_question_checkbox_2
	assert form_question_checkbox_2.label == new_label



@pytest.mark.asyncio
async def test_delete_form_question_checkbox(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True

	form_question_checkbox_in = FormQuestionCheckboxSchemaCreate(
		label=label,
		is_active=is_active,
	)

	form_question_checkbox = await form_question_checkbox_crud.create(
		db=db,
		obj_in=form_question_checkbox_in,
	)

	form_question_checkbox_2 = await form_question_checkbox_crud.delete(
		db=db,
		id=form_question_checkbox.id,
	)

	form_question_checkbox_3 = await form_question_checkbox_crud.get(
		db=db,
		id=form_question_checkbox.id,
	)


	assert form_question_checkbox_3 is None
	assert form_question_checkbox_2.id == form_question_checkbox.id



@pytest.mark.asyncio
async def test_delete_sync_form_question_checkbox(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True

	form_question_checkbox_in = FormQuestionCheckboxSchemaCreate(
		label=label,
		is_active=is_active,
	)

	form_question_checkbox = await db.run_sync(
		form_question_checkbox_crud.create_sync,
		obj_in=form_question_checkbox_in,
	)

	form_question_checkbox_2 = await db.run_sync(
		form_question_checkbox_crud.delete_sync,
		id=form_question_checkbox.id,
	)

	form_question_checkbox_3 = await db.run_sync(
		form_question_checkbox_crud.get_sync,
		id=form_question_checkbox.id,
	)


	assert form_question_checkbox_3 is None
	assert form_question_checkbox_2.id == form_question_checkbox.id




# Radio --


@pytest.mark.asyncio
async def test_create_form_question_radio(
	db: AsyncSession,
) -> None:
	# --
	
	label = random_lower_string()
	is_active = True
	radio_answers = {
		'a': 'abc',
	}

	form_question_radio_in = FormQuestionRadioSchemaCreate(
		label=label,
		is_active=is_active,
		radio_answers=radio_answers,
	)

	form_question_radio = await form_question_radio_crud.create(
		db=db,
		obj_in=form_question_radio_in,
	)

	assert form_question_radio.label == label
	assert form_question_radio.is_active == is_active



@pytest.mark.asyncio
async def test_create_sync_form_question_radio(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True
	radio_answers = {
		'a': 'abc',
	}

	form_question_radio_in = FormQuestionRadioSchemaCreate(
		label=label,
		is_active=is_active,
		radio_answers=radio_answers,
	)

	form_question_radio = await db.run_sync(
		form_question_radio_crud.create_sync,
		obj_in=form_question_radio_in,
	)

	assert form_question_radio.label == label
	assert form_question_radio.is_active == is_active



@pytest.mark.asyncio
async def test_get_form_question_radio(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True
	radio_answers = {
		'a': 'abc',
	}

	form_question_radio_in = FormQuestionRadioSchemaCreate(
		label=label,
		is_active=is_active,
		radio_answers=radio_answers,
	)

	form_question_radio = await form_question_radio_crud.create(
		db=db,
		obj_in=form_question_radio_in,
	)

	form_question_radio_2 = await form_question_radio_crud.get(
		db=db,
		id=form_question_radio.id,
	)

	assert form_question_radio_2
	assert jsonable_encoder(form_question_radio_2) == jsonable_encoder(form_question_radio)



@pytest.mark.asyncio
async def test_get_sync_form_question_radio(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True
	radio_answers = {
		'a': 'abc',
	}

	form_question_radio_in = FormQuestionRadioSchemaCreate(
		label=label,
		is_active=is_active,
		radio_answers=radio_answers,
	)

	form_question_radio = await db.run_sync(
		form_question_radio_crud.create_sync,
		obj_in=form_question_radio_in,
	)

	form_question_radio_2 = await db.run_sync(
		form_question_radio_crud.get_sync,
		id=form_question_radio.id,
	)

	assert form_question_radio_2
	assert jsonable_encoder(form_question_radio_2) == jsonable_encoder(form_question_radio)



@pytest.mark.asyncio
async def test_update_form_question_radio(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True
	radio_answers = {
		'a': 'abc',
	}

	form_question_radio_in = FormQuestionRadioSchemaCreate(
		label=label,
		is_active=is_active,
		radio_answers=radio_answers,
	)

	form_question_radio = await form_question_radio_crud.create(
		db=db,
		obj_in=form_question_radio_in,
	)


	new_label = random_lower_string()
	
	form_question_radio_in_update = FormQuestionRadioSchemaUpdate(
		label=new_label,
	)

	form_question_radio_2 = await form_question_radio_crud.update(
		db=db,
		db_obj=form_question_radio,
		obj_in=form_question_radio_in_update,
	)

	assert form_question_radio_2
	assert form_question_radio_2.label == new_label



@pytest.mark.asyncio
async def test_update_sync_form_question_radio(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True
	radio_answers = {
		'a': 'abc',
	}

	form_question_radio_in = FormQuestionRadioSchemaCreate(
		label=label,
		is_active=is_active,
		radio_answers=radio_answers,
	)

	form_question_radio = await db.run_sync(
		form_question_radio_crud.create_sync,
		obj_in=form_question_radio_in,
	)


	new_label = random_lower_string()
	
	form_question_radio_in_update = FormQuestionRadioSchemaUpdate(
		label=new_label,
	)

	form_question_radio_2 = await db.run_sync(
		form_question_radio_crud.update_sync,
		db_obj=form_question_radio,
		obj_in=form_question_radio_in_update,
	)

	assert form_question_radio_2
	assert form_question_radio_2.label == new_label



@pytest.mark.asyncio
async def test_delete_form_question_radio(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True
	radio_answers = {
		'a': 'abc',
	}

	form_question_radio_in = FormQuestionRadioSchemaCreate(
		label=label,
		is_active=is_active,
		radio_answers=radio_answers,
	)

	form_question_radio = await form_question_radio_crud.create(
		db=db,
		obj_in=form_question_radio_in,
	)

	form_question_radio_2 = await form_question_radio_crud.delete(
		db=db,
		id=form_question_radio.id,
	)

	form_question_radio_3 = await form_question_radio_crud.get(
		db=db,
		id=form_question_radio.id,
	)


	assert form_question_radio_3 is None
	assert form_question_radio_2.id == form_question_radio.id



@pytest.mark.asyncio
async def test_delete_sync_form_question_radio(
	db: AsyncSession,
) -> None:
	# --

	label = random_lower_string()
	is_active = True
	radio_answers = {
		'a': 'abc',
	}

	form_question_radio_in = FormQuestionRadioSchemaCreate(
		label=label,
		is_active=is_active,
		radio_answers=radio_answers,
	)

	form_question_radio = await db.run_sync(
		form_question_radio_crud.create_sync,
		obj_in=form_question_radio_in,
	)

	form_question_radio_2 = await db.run_sync(
		form_question_radio_crud.delete_sync,
		id=form_question_radio.id,
	)

	form_question_radio_3 = await db.run_sync(
		form_question_radio_crud.get_sync,
		id=form_question_radio.id,
	)


	assert form_question_radio_3 is None
	assert form_question_radio_2.id == form_question_radio.id









