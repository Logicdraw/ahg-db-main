# POLYMORPHIC -- 


from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.form.entry.answer import (
	form_entry_answer_input_crud,
	form_entry_answer_textarea_crud,
	form_entry_answer_select_crud,
	form_entry_answer_checkbox_crud,
	form_entry_answer_radio_crud,
)

from main.schemas.form.entry.answer import (
	FormEntryAnswerInputSchemaCreate,
	FormEntryAnswerInputSchemaUpdate,
	FormEntryAnswerTextareaSchemaCreate,
	FormEntryAnswerTextareaSchemaUpdate,
	FormEntryAnswerSelectSchemaCreate,
	FormEntryAnswerSelectSchemaUpdate,
	FormEntryAnswerCheckboxSchemaCreate,
	FormEntryAnswerCheckboxSchemaUpdate,
	FormEntryAnswerRadioSchemaCreate,
	FormEntryAnswerRadioSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest



# crud, async + sync all !!!



# Input --



@pytest.mark.asyncio
async def test_create_form_answer_input(
	db: AsyncSession,
) -> None:
	# --
	
	input_answer = random_lower_string()

	form_answer_input_in = FormEntryAnswerInputSchemaCreate(
		input_answer=input_answer,
	)

	form_answer_input = await form_answer_input_crud.create(
		db=db,
		obj_in=form_answer_input_in,
	)

	assert form_answer_input.label == label
	assert form_answer_input.is_active == is_active



@pytest.mark.asyncio
async def test_create_sync_form_answer_input(
	db: AsyncSession,
) -> None:
	# --

	input_answer = random_lower_string()

	form_answer_input_in = FormEntryAnswerInputSchemaCreate(
		input_answer=input_answer,
	)

	form_answer_input = await db.run_sync(
		form_answer_input_crud.create_sync,
		obj_in=form_answer_input_in,
	)

	assert form_answer_input.label == label
	assert form_answer_input.is_active == is_active



@pytest.mark.asyncio
async def test_get_form_answer_input(
	db: AsyncSession,
) -> None:
	# --

	input_answer = random_lower_string()

	form_answer_input_in = FormEntryAnswerInputSchemaCreate(
		input_answer=input_answer,
	)

	form_answer_input = await form_answer_input_crud.create(
		db=db,
		obj_in=form_answer_input_in,
	)

	form_answer_input_2 = await form_answer_input_crud.get(
		db=db,
		id=form_answer_input.id,
	)

	assert form_answer_input_2
	assert jsonable_encoder(form_answer_input_2) == jsonable_encoder(form_answer_input)



@pytest.mark.asyncio
async def test_get_sync_form_answer_input(
	db: AsyncSession,
) -> None:
	# --

	input_answer = random_lower_string()

	form_answer_input_in = FormEntryAnswerInputSchemaCreate(
		input_answer=input_answer,
	)

	form_answer_input = await db.run_sync(
		form_answer_input_crud.create_sync,
		obj_in=form_answer_input_in,
	)

	form_answer_input_2 = await db.run_sync(
		form_answer_input_crud.get_sync,
		id=form_answer_input.id,
	)

	assert form_answer_input_2
	assert jsonable_encoder(form_answer_input_2) == jsonable_encoder(form_answer_input)



@pytest.mark.asyncio
async def test_update_form_answer_input(
	db: AsyncSession,
) -> None:
	# --

	input_answer = random_lower_string()

	form_answer_input_in = FormEntryAnswerInputSchemaCreate(
		input_answer=input_answer,
	)

	form_answer_input = await form_answer_input_crud.create(
		db=db,
		obj_in=form_answer_input_in,
	)


	new_label = random_lower_string()
	
	form_answer_input_in_update = FormEntryAnswerInputSchemaUpdate(
		label=new_label,
	)

	form_answer_input_2 = await form_answer_input_crud.update(
		db=db,
		db_obj=form_answer_input,
		obj_in=form_answer_input_in_update,
	)

	assert form_answer_input_2
	assert form_answer_input_2.label == new_label



@pytest.mark.asyncio
async def test_update_sync_form_answer_input(
	db: AsyncSession,
) -> None:
	# --

	input_answer = random_lower_string()

	form_answer_input_in = FormEntryAnswerInputSchemaCreate(
		input_answer=input_answer,
	)

	form_answer_input = await db.run_sync(
		form_answer_input_crud.create_sync,
		obj_in=form_answer_input_in,
	)


	new_label = random_lower_string()
	
	form_answer_input_in_update = FormEntryAnswerInputSchemaUpdate(
		label=new_label,
	)

	form_answer_input_2 = await db.run_sync(
		form_answer_input_crud.update_sync,
		db_obj=form_answer_input,
		obj_in=form_answer_input_in_update,
	)

	assert form_answer_input_2
	assert form_answer_input_2.label == new_label



@pytest.mark.asyncio
async def test_delete_form_answer_input(
	db: AsyncSession,
) -> None:
	# --

	input_answer = random_lower_string()

	form_answer_input_in = FormEntryAnswerInputSchemaCreate(
		input_answer=input_answer,
	)

	form_answer_input = await form_answer_input_crud.create(
		db=db,
		obj_in=form_answer_input_in,
	)

	form_answer_input_2 = await form_answer_input_crud.delete(
		db=db,
		id=form_answer_input.id,
	)

	form_answer_input_3 = await form_answer_input_crud.get(
		db=db,
		id=form_answer_input.id,
	)


	assert form_answer_input_3 is None
	assert form_answer_input_2.id == form_answer_input.id



@pytest.mark.asyncio
async def test_delete_sync_form_answer_input(
	db: AsyncSession,
) -> None:
	# --

	input_answer = random_lower_string()

	form_answer_input_in = FormEntryAnswerInputSchemaCreate(
		input_answer=input_answer,
	)

	form_answer_input = await db.run_sync(
		form_answer_input_crud.create_sync,
		obj_in=form_answer_input_in,
	)

	form_answer_input_2 = await db.run_sync(
		form_answer_input_crud.delete_sync,
		id=form_answer_input.id,
	)

	form_answer_input_3 = await db.run_sync(
		form_answer_input_crud.get_sync,
		id=form_answer_input.id,
	)


	assert form_answer_input_3 is None
	assert form_answer_input_2.id == form_answer_input.id




# Textarea --


@pytest.mark.asyncio
async def test_create_form_answer_textarea(
	db: AsyncSession,
) -> None:
	# --
	
	textarea_answer = random_lower_string()

	form_answer_textarea_in = FormEntryAnswerTextareaSchemaCreate(
		textarea_answer=textarea_answer,
	)

	form_answer_textarea = await form_answer_textarea_crud.create(
		db=db,
		obj_in=form_answer_textarea_in,
	)

	assert form_answer_textarea.label == label
	assert form_answer_textarea.is_active == is_active



@pytest.mark.asyncio
async def test_create_sync_form_answer_textarea(
	db: AsyncSession,
) -> None:
	# --

	textarea_answer = random_lower_string()

	form_answer_textarea_in = FormEntryAnswerTextareaSchemaCreate(
		textarea_answer=textarea_answer,
	)

	form_answer_textarea = await db.run_sync(
		form_answer_textarea_crud.create_sync,
		obj_in=form_answer_textarea_in,
	)

	assert form_answer_textarea.label == label
	assert form_answer_textarea.is_active == is_active



@pytest.mark.asyncio
async def test_get_form_answer_textarea(
	db: AsyncSession,
) -> None:
	# --

	textarea_answer = random_lower_string()

	form_answer_textarea_in = FormEntryAnswerTextareaSchemaCreate(
		textarea_answer=textarea_answer,
	)

	form_answer_textarea = await form_answer_textarea_crud.create(
		db=db,
		obj_in=form_answer_textarea_in,
	)

	form_answer_textarea_2 = await form_answer_textarea_crud.get(
		db=db,
		id=form_answer_textarea.id,
	)

	assert form_answer_textarea_2
	assert jsonable_encoder(form_answer_textarea_2) == jsonable_encoder(form_answer_textarea)



@pytest.mark.asyncio
async def test_get_sync_form_answer_textarea(
	db: AsyncSession,
) -> None:
	# --

	textarea_answer = random_lower_string()

	form_answer_textarea_in = FormEntryAnswerTextareaSchemaCreate(
		textarea_answer=textarea_answer,
	)

	form_answer_textarea = await db.run_sync(
		form_answer_textarea_crud.create_sync,
		obj_in=form_answer_textarea_in,
	)

	form_answer_textarea_2 = await db.run_sync(
		form_answer_textarea_crud.get_sync,
		id=form_answer_textarea.id,
	)

	assert form_answer_textarea_2
	assert jsonable_encoder(form_answer_textarea_2) == jsonable_encoder(form_answer_textarea)



@pytest.mark.asyncio
async def test_update_form_answer_textarea(
	db: AsyncSession,
) -> None:
	# --

	textarea_answer = random_lower_string()

	form_answer_textarea_in = FormEntryAnswerTextareaSchemaCreate(
		textarea_answer=textarea_answer,
	)

	form_answer_textarea = await form_answer_textarea_crud.create(
		db=db,
		obj_in=form_answer_textarea_in,
	)


	new_label = random_lower_string()
	
	form_answer_textarea_in_update = FormEntryAnswerTextareaSchemaUpdate(
		label=new_label,
	)

	form_answer_textarea_2 = await form_answer_textarea_crud.update(
		db=db,
		db_obj=form_answer_textarea,
		obj_in=form_answer_textarea_in_update,
	)

	assert form_answer_textarea_2
	assert form_answer_textarea_2.label == new_label



@pytest.mark.asyncio
async def test_update_sync_form_answer_textarea(
	db: AsyncSession,
) -> None:
	# --

	textarea_answer = random_lower_string()

	form_answer_textarea_in = FormEntryAnswerTextareaSchemaCreate(
		textarea_answer=textarea_answer,
	)

	form_answer_textarea = await db.run_sync(
		form_answer_textarea_crud.create_sync,
		obj_in=form_answer_textarea_in,
	)


	new_label = random_lower_string()
	
	form_answer_textarea_in_update = FormEntryAnswerTextareaSchemaUpdate(
		label=new_label,
	)

	form_answer_textarea_2 = await db.run_sync(
		form_answer_textarea_crud.update_sync,
		db_obj=form_answer_textarea,
		obj_in=form_answer_textarea_in_update,
	)

	assert form_answer_textarea_2
	assert form_answer_textarea_2.label == new_label



@pytest.mark.asyncio
async def test_delete_form_answer_textarea(
	db: AsyncSession,
) -> None:
	# --

	textarea_answer = random_lower_string()

	form_answer_textarea_in = FormEntryAnswerTextareaSchemaCreate(
		textarea_answer=textarea_answer,
	)

	form_answer_textarea = await form_answer_textarea_crud.create(
		db=db,
		obj_in=form_answer_textarea_in,
	)

	form_answer_textarea_2 = await form_answer_textarea_crud.delete(
		db=db,
		id=form_answer_textarea.id,
	)

	form_answer_textarea_3 = await form_answer_textarea_crud.get(
		db=db,
		id=form_answer_textarea.id,
	)


	assert form_answer_textarea_3 is None
	assert form_answer_textarea_2.id == form_answer_textarea.id



@pytest.mark.asyncio
async def test_delete_sync_form_answer_textarea(
	db: AsyncSession,
) -> None:
	# --

	textarea_answer = random_lower_string()

	form_answer_textarea_in = FormEntryAnswerTextareaSchemaCreate(
		textarea_answer=textarea_answer,
	)

	form_answer_textarea = await db.run_sync(
		form_answer_textarea_crud.create_sync,
		obj_in=form_answer_textarea_in,
	)

	form_answer_textarea_2 = await db.run_sync(
		form_answer_textarea_crud.delete_sync,
		id=form_answer_textarea.id,
	)

	form_answer_textarea_3 = await db.run_sync(
		form_answer_textarea_crud.get_sync,
		id=form_answer_textarea.id,
	)


	assert form_answer_textarea_3 is None
	assert form_answer_textarea_2.id == form_answer_textarea.id



# Select --


@pytest.mark.asyncio
async def test_create_form_answer_textarea(
	db: AsyncSession,
) -> None:
	# --
	
	textarea_answer = random_lower_string()

	form_answer_textarea_in = FormEntryAnswerSelectSchemaCreate(
		textarea_answer=textarea_answer,
	)

	form_answer_textarea = await form_answer_textarea_crud.create(
		db=db,
		obj_in=form_answer_textarea_in,
	)

	assert form_answer_textarea.label == label
	assert form_answer_textarea.is_active == is_active



@pytest.mark.asyncio
async def test_create_sync_form_answer_textarea(
	db: AsyncSession,
) -> None:
	# --

	textarea_answer = random_lower_string()

	form_answer_textarea_in = FormEntryAnswerSelectSchemaCreate(
		textarea_answer=textarea_answer,
	)

	form_answer_textarea = await db.run_sync(
		form_answer_textarea_crud.create_sync,
		obj_in=form_answer_textarea_in,
	)

	assert form_answer_textarea.label == label
	assert form_answer_textarea.is_active == is_active



@pytest.mark.asyncio
async def test_get_form_answer_textarea(
	db: AsyncSession,
) -> None:
	# --

	textarea_answer = random_lower_string()

	form_answer_textarea_in = FormEntryAnswerSelectSchemaCreate(
		textarea_answer=textarea_answer,
	)

	form_answer_textarea = await form_answer_textarea_crud.create(
		db=db,
		obj_in=form_answer_textarea_in,
	)

	form_answer_textarea_2 = await form_answer_textarea_crud.get(
		db=db,
		id=form_answer_textarea.id,
	)

	assert form_answer_textarea_2
	assert jsonable_encoder(form_answer_textarea_2) == jsonable_encoder(form_answer_textarea)



@pytest.mark.asyncio
async def test_get_sync_form_answer_textarea(
	db: AsyncSession,
) -> None:
	# --

	textarea_answer = random_lower_string()

	form_answer_textarea_in = FormEntryAnswerSelectSchemaCreate(
		textarea_answer=textarea_answer,
	)

	form_answer_textarea = await db.run_sync(
		form_answer_textarea_crud.create_sync,
		obj_in=form_answer_textarea_in,
	)

	form_answer_textarea_2 = await db.run_sync(
		form_answer_textarea_crud.get_sync,
		id=form_answer_textarea.id,
	)

	assert form_answer_textarea_2
	assert jsonable_encoder(form_answer_textarea_2) == jsonable_encoder(form_answer_textarea)



@pytest.mark.asyncio
async def test_update_form_answer_textarea(
	db: AsyncSession,
) -> None:
	# --

	textarea_answer = random_lower_string()

	form_answer_textarea_in = FormEntryAnswerSelectSchemaCreate(
		textarea_answer=textarea_answer,
	)

	form_answer_textarea = await form_answer_textarea_crud.create(
		db=db,
		obj_in=form_answer_textarea_in,
	)


	new_label = random_lower_string()
	
	form_answer_textarea_in_update = FormEntryAnswerSelectSchemaUpdate(
		label=new_label,
	)

	form_answer_textarea_2 = await form_answer_textarea_crud.update(
		db=db,
		db_obj=form_answer_textarea,
		obj_in=form_answer_textarea_in_update,
	)

	assert form_answer_textarea_2
	assert form_answer_textarea_2.label == new_label



@pytest.mark.asyncio
async def test_update_sync_form_answer_textarea(
	db: AsyncSession,
) -> None:
	# --

	textarea_answer = random_lower_string()

	form_answer_textarea_in = FormEntryAnswerSelectSchemaCreate(
		textarea_answer=textarea_answer,
	)

	form_answer_textarea = await db.run_sync(
		form_answer_textarea_crud.create_sync,
		obj_in=form_answer_textarea_in,
	)


	new_label = random_lower_string()
	
	form_answer_textarea_in_update = FormEntryAnswerSelectSchemaUpdate(
		label=new_label,
	)

	form_answer_textarea_2 = await db.run_sync(
		form_answer_textarea_crud.update_sync,
		db_obj=form_answer_textarea,
		obj_in=form_answer_textarea_in_update,
	)

	assert form_answer_textarea_2
	assert form_answer_textarea_2.label == new_label



@pytest.mark.asyncio
async def test_delete_form_answer_textarea(
	db: AsyncSession,
) -> None:
	# --

	textarea_answer = random_lower_string()

	form_answer_textarea_in = FormEntryAnswerSelectSchemaCreate(
		textarea_answer=textarea_answer,
	)

	form_answer_textarea = await form_answer_textarea_crud.create(
		db=db,
		obj_in=form_answer_textarea_in,
	)

	form_answer_textarea_2 = await form_answer_textarea_crud.delete(
		db=db,
		id=form_answer_textarea.id,
	)

	form_answer_textarea_3 = await form_answer_textarea_crud.get(
		db=db,
		id=form_answer_textarea.id,
	)


	assert form_answer_textarea_3 is None
	assert form_answer_textarea_2.id == form_answer_textarea.id



@pytest.mark.asyncio
async def test_delete_sync_form_answer_textarea(
	db: AsyncSession,
) -> None:
	# --

	textarea_answer = random_lower_string()

	form_answer_textarea_in = FormEntryAnswerSelectSchemaCreate(
		textarea_answer=textarea_answer,
	)

	form_answer_textarea = await db.run_sync(
		form_answer_textarea_crud.create_sync,
		obj_in=form_answer_textarea_in,
	)

	form_answer_textarea_2 = await db.run_sync(
		form_answer_textarea_crud.delete_sync,
		id=form_answer_textarea.id,
	)

	form_answer_textarea_3 = await db.run_sync(
		form_answer_textarea_crud.get_sync,
		id=form_answer_textarea.id,
	)


	assert form_answer_textarea_3 is None
	assert form_answer_textarea_2.id == form_answer_textarea.id




# Select --


@pytest.mark.asyncio
async def test_create_form_answer_select(
	db: AsyncSession,
) -> None:
	# --
	
	select_selected = {
		'a': 'abc',
	}

	form_answer_select_in = FormEntryAnswerSelectSchemaCreate(
		select_selected=select_selected,
	)

	form_answer_select = await form_answer_select_crud.create(
		db=db,
		obj_in=form_answer_select_in,
	)

	assert form_answer_select.label == label
	assert form_answer_select.is_active == is_active



@pytest.mark.asyncio
async def test_create_sync_form_answer_select(
	db: AsyncSession,
) -> None:
	# --

	select_selected = {
		'a': 'abc',
	}

	form_answer_select_in = FormEntryAnswerSelectSchemaCreate(
		select_selected=select_selected,
	)

	form_answer_select = await db.run_sync(
		form_answer_select_crud.create_sync,
		obj_in=form_answer_select_in,
	)

	assert form_answer_select.label == label
	assert form_answer_select.is_active == is_active



@pytest.mark.asyncio
async def test_get_form_answer_select(
	db: AsyncSession,
) -> None:
	# --

	select_selected = {
		'a': 'abc',
	}

	form_answer_select_in = FormEntryAnswerSelectSchemaCreate(
		select_selected=select_selected,
	)

	form_answer_select = await form_answer_select_crud.create(
		db=db,
		obj_in=form_answer_select_in,
	)

	form_answer_select_2 = await form_answer_select_crud.get(
		db=db,
		id=form_answer_select.id,
	)

	assert form_answer_select_2
	assert jsonable_encoder(form_answer_select_2) == jsonable_encoder(form_answer_select)



@pytest.mark.asyncio
async def test_get_sync_form_answer_select(
	db: AsyncSession,
) -> None:
	# --

	select_selected = {
		'a': 'abc',
	}

	form_answer_select_in = FormEntryAnswerSelectSchemaCreate(
		select_selected=select_selected,
	)

	form_answer_select = await db.run_sync(
		form_answer_select_crud.create_sync,
		obj_in=form_answer_select_in,
	)

	form_answer_select_2 = await db.run_sync(
		form_answer_select_crud.get_sync,
		id=form_answer_select.id,
	)

	assert form_answer_select_2
	assert jsonable_encoder(form_answer_select_2) == jsonable_encoder(form_answer_select)



@pytest.mark.asyncio
async def test_update_form_answer_select(
	db: AsyncSession,
) -> None:
	# --

	select_selected = {
		'a': 'abc',
	}

	form_answer_select_in = FormEntryAnswerSelectSchemaCreate(
		select_selected=select_selected,
	)

	form_answer_select = await form_answer_select_crud.create(
		db=db,
		obj_in=form_answer_select_in,
	)


	new_label = {

	}
	
	form_answer_select_in_update = FormEntryAnswerSelectSchemaUpdate(
		label=new_label,
	)

	form_answer_select_2 = await form_answer_select_crud.update(
		db=db,
		db_obj=form_answer_select,
		obj_in=form_answer_select_in_update,
	)

	assert form_answer_select_2
	assert form_answer_select_2.label == new_label



@pytest.mark.asyncio
async def test_update_sync_form_answer_select(
	db: AsyncSession,
) -> None:
	# --

	select_selected = {
		'a': 'abc',
	}

	form_answer_select_in = FormEntryAnswerSelectSchemaCreate(
		select_selected=select_selected,
	)

	form_answer_select = await db.run_sync(
		form_answer_select_crud.create_sync,
		obj_in=form_answer_select_in,
	)


	new_label = {

	}
	
	form_answer_select_in_update = FormEntryAnswerSelectSchemaUpdate(
		label=new_label,
	)

	form_answer_select_2 = await db.run_sync(
		form_answer_select_crud.update_sync,
		db_obj=form_answer_select,
		obj_in=form_answer_select_in_update,
	)

	assert form_answer_select_2
	assert form_answer_select_2.label == new_label



@pytest.mark.asyncio
async def test_delete_form_answer_select(
	db: AsyncSession,
) -> None:
	# --

	select_selected = {
		'a': 'abc',
	}

	form_answer_select_in = FormEntryAnswerSelectSchemaCreate(
		select_selected=select_selected,
	)

	form_answer_select = await form_answer_select_crud.create(
		db=db,
		obj_in=form_answer_select_in,
	)

	form_answer_select_2 = await form_answer_select_crud.delete(
		db=db,
		id=form_answer_select.id,
	)

	form_answer_select_3 = await form_answer_select_crud.get(
		db=db,
		id=form_answer_select.id,
	)


	assert form_answer_select_3 is None
	assert form_answer_select_2.id == form_answer_select.id



@pytest.mark.asyncio
async def test_delete_sync_form_answer_select(
	db: AsyncSession,
) -> None:
	# --

	select_selected = {
		'a': 'abc',
	}

	form_answer_select_in = FormEntryAnswerSelectSchemaCreate(
		select_selected=select_selected,
	)

	form_answer_select = await db.run_sync(
		form_answer_select_crud.create_sync,
		obj_in=form_answer_select_in,
	)

	form_answer_select_2 = await db.run_sync(
		form_answer_select_crud.delete_sync,
		id=form_answer_select.id,
	)

	form_answer_select_3 = await db.run_sync(
		form_answer_select_crud.get_sync,
		id=form_answer_select.id,
	)


	assert form_answer_select_3 is None
	assert form_answer_select_2.id == form_answer_select.id



# Checkbox --


@pytest.mark.asyncio
async def test_create_form_answer_checkbox(
	db: AsyncSession,
) -> None:
	# --
	
	checkbox_checked = True

	form_answer_checkbox_in = FormEntryAnswerCheckboxSchemaCreate(
		checkbox_checked=checkbox_checked,
	)

	form_answer_checkbox = await form_answer_checkbox_crud.create(
		db=db,
		obj_in=form_answer_checkbox_in,
	)

	assert form_answer_checkbox.label == label
	assert form_answer_checkbox.is_active == is_active



@pytest.mark.asyncio
async def test_create_sync_form_answer_checkbox(
	db: AsyncSession,
) -> None:
	# --

	checkbox_checked = True

	form_answer_checkbox_in = FormEntryAnswerCheckboxSchemaCreate(
		checkbox_checked=checkbox_checked,
	)

	form_answer_checkbox = await db.run_sync(
		form_answer_checkbox_crud.create_sync,
		obj_in=form_answer_checkbox_in,
	)

	assert form_answer_checkbox.label == label
	assert form_answer_checkbox.is_active == is_active



@pytest.mark.asyncio
async def test_get_form_answer_checkbox(
	db: AsyncSession,
) -> None:
	# --

	checkbox_checked = True

	form_answer_checkbox_in = FormEntryAnswerCheckboxSchemaCreate(
		checkbox_checked=checkbox_checked,
	)

	form_answer_checkbox = await form_answer_checkbox_crud.create(
		db=db,
		obj_in=form_answer_checkbox_in,
	)

	form_answer_checkbox_2 = await form_answer_checkbox_crud.get(
		db=db,
		id=form_answer_checkbox.id,
	)

	assert form_answer_checkbox_2
	assert jsonable_encoder(form_answer_checkbox_2) == jsonable_encoder(form_answer_checkbox)



@pytest.mark.asyncio
async def test_get_sync_form_answer_checkbox(
	db: AsyncSession,
) -> None:
	# --

	checkbox_checked = True

	form_answer_checkbox_in = FormEntryAnswerCheckboxSchemaCreate(
		checkbox_checked=checkbox_checked,
	)

	form_answer_checkbox = await db.run_sync(
		form_answer_checkbox_crud.create_sync,
		obj_in=form_answer_checkbox_in,
	)

	form_answer_checkbox_2 = await db.run_sync(
		form_answer_checkbox_crud.get_sync,
		id=form_answer_checkbox.id,
	)

	assert form_answer_checkbox_2
	assert jsonable_encoder(form_answer_checkbox_2) == jsonable_encoder(form_answer_checkbox)



@pytest.mark.asyncio
async def test_update_form_answer_checkbox(
	db: AsyncSession,
) -> None:
	# --

	checkbox_checked = True

	form_answer_checkbox_in = FormEntryAnswerCheckboxSchemaCreate(
		checkbox_checked=checkbox_checked,
	)

	form_answer_checkbox = await form_answer_checkbox_crud.create(
		db=db,
		obj_in=form_answer_checkbox_in,
	)


	new_label = {

	}
	
	form_answer_checkbox_in_update = FormEntryAnswerCheckboxSchemaUpdate(
		label=new_label,
	)

	form_answer_checkbox_2 = await form_answer_checkbox_crud.update(
		db=db,
		db_obj=form_answer_checkbox,
		obj_in=form_answer_checkbox_in_update,
	)

	assert form_answer_checkbox_2
	assert form_answer_checkbox_2.label == new_label



@pytest.mark.asyncio
async def test_update_sync_form_answer_checkbox(
	db: AsyncSession,
) -> None:
	# --

	checkbox_checked = True

	form_answer_checkbox_in = FormEntryAnswerCheckboxSchemaCreate(
		checkbox_checked=checkbox_checked,
	)

	form_answer_checkbox = await db.run_sync(
		form_answer_checkbox_crud.create_sync,
		obj_in=form_answer_checkbox_in,
	)


	new_label = {

	}
	
	form_answer_checkbox_in_update = FormEntryAnswerCheckboxSchemaUpdate(
		label=new_label,
	)

	form_answer_checkbox_2 = await db.run_sync(
		form_answer_checkbox_crud.update_sync,
		db_obj=form_answer_checkbox,
		obj_in=form_answer_checkbox_in_update,
	)

	assert form_answer_checkbox_2
	assert form_answer_checkbox_2.label == new_label



@pytest.mark.asyncio
async def test_delete_form_answer_checkbox(
	db: AsyncSession,
) -> None:
	# --

	checkbox_checked = True

	form_answer_checkbox_in = FormEntryAnswerCheckboxSchemaCreate(
		checkbox_checked=checkbox_checked,
	)

	form_answer_checkbox = await form_answer_checkbox_crud.create(
		db=db,
		obj_in=form_answer_checkbox_in,
	)

	form_answer_checkbox_2 = await form_answer_checkbox_crud.delete(
		db=db,
		id=form_answer_checkbox.id,
	)

	form_answer_checkbox_3 = await form_answer_checkbox_crud.get(
		db=db,
		id=form_answer_checkbox.id,
	)


	assert form_answer_checkbox_3 is None
	assert form_answer_checkbox_2.id == form_answer_checkbox.id



@pytest.mark.asyncio
async def test_delete_sync_form_answer_checkbox(
	db: AsyncSession,
) -> None:
	# --

	checkbox_checked = True

	form_answer_checkbox_in = FormEntryAnswerCheckboxSchemaCreate(
		checkbox_checked=checkbox_checked,
	)

	form_answer_checkbox = await db.run_sync(
		form_answer_checkbox_crud.create_sync,
		obj_in=form_answer_checkbox_in,
	)

	form_answer_checkbox_2 = await db.run_sync(
		form_answer_checkbox_crud.delete_sync,
		id=form_answer_checkbox.id,
	)

	form_answer_checkbox_3 = await db.run_sync(
		form_answer_checkbox_crud.get_sync,
		id=form_answer_checkbox.id,
	)


	assert form_answer_checkbox_3 is None
	assert form_answer_checkbox_2.id == form_answer_checkbox.id




# Radio --



@pytest.mark.asyncio
async def test_create_form_answer_radio(
	db: AsyncSession,
) -> None:
	# --
	
	radio_selected = {
		'a': 'abc',
	}

	form_answer_radio_in = FormEntryAnswerRadioSchemaCreate(
		radio_selected=radio_selected,
	)

	form_answer_radio = await form_answer_radio_crud.create(
		db=db,
		obj_in=form_answer_radio_in,
	)

	assert form_answer_radio.label == label
	assert form_answer_radio.is_active == is_active



@pytest.mark.asyncio
async def test_create_sync_form_answer_radio(
	db: AsyncSession,
) -> None:
	# --

	radio_selected = {
		'a': 'abc',
	}

	form_answer_radio_in = FormEntryAnswerRadioSchemaCreate(
		radio_selected=radio_selected,
	)

	form_answer_radio = await db.run_sync(
		form_answer_radio_crud.create_sync,
		obj_in=form_answer_radio_in,
	)

	assert form_answer_radio.label == label
	assert form_answer_radio.is_active == is_active



@pytest.mark.asyncio
async def test_get_form_answer_radio(
	db: AsyncSession,
) -> None:
	# --

	radio_selected = {
		'a': 'abc',
	}

	form_answer_radio_in = FormEntryAnswerRadioSchemaCreate(
		radio_selected=radio_selected,
	)

	form_answer_radio = await form_answer_radio_crud.create(
		db=db,
		obj_in=form_answer_radio_in,
	)

	form_answer_radio_2 = await form_answer_radio_crud.get(
		db=db,
		id=form_answer_radio.id,
	)

	assert form_answer_radio_2
	assert jsonable_encoder(form_answer_radio_2) == jsonable_encoder(form_answer_radio)



@pytest.mark.asyncio
async def test_get_sync_form_answer_radio(
	db: AsyncSession,
) -> None:
	# --

	radio_selected = {
		'a': 'abc',
	}

	form_answer_radio_in = FormEntryAnswerRadioSchemaCreate(
		radio_selected=radio_selected,
	)

	form_answer_radio = await db.run_sync(
		form_answer_radio_crud.create_sync,
		obj_in=form_answer_radio_in,
	)

	form_answer_radio_2 = await db.run_sync(
		form_answer_radio_crud.get_sync,
		id=form_answer_radio.id,
	)

	assert form_answer_radio_2
	assert jsonable_encoder(form_answer_radio_2) == jsonable_encoder(form_answer_radio)



@pytest.mark.asyncio
async def test_update_form_answer_radio(
	db: AsyncSession,
) -> None:
	# --

	radio_selected = {
		'a': 'abc',
	}

	form_answer_radio_in = FormEntryAnswerRadioSchemaCreate(
		radio_selected=radio_selected,
	)

	form_answer_radio = await form_answer_radio_crud.create(
		db=db,
		obj_in=form_answer_radio_in,
	)


	new_label = {

	}
	
	form_answer_radio_in_update = FormEntryAnswerRadioSchemaUpdate(
		label=new_label,
	)

	form_answer_radio_2 = await form_answer_radio_crud.update(
		db=db,
		db_obj=form_answer_radio,
		obj_in=form_answer_radio_in_update,
	)

	assert form_answer_radio_2
	assert form_answer_radio_2.label == new_label



@pytest.mark.asyncio
async def test_update_sync_form_answer_radio(
	db: AsyncSession,
) -> None:
	# --

	radio_selected = {
		'a': 'abc',
	}

	form_answer_radio_in = FormEntryAnswerRadioSchemaCreate(
		radio_selected=radio_selected,
	)

	form_answer_radio = await db.run_sync(
		form_answer_radio_crud.create_sync,
		obj_in=form_answer_radio_in,
	)


	new_label = {

	}
	
	form_answer_radio_in_update = FormEntryAnswerRadioSchemaUpdate(
		label=new_label,
	)

	form_answer_radio_2 = await db.run_sync(
		form_answer_radio_crud.update_sync,
		db_obj=form_answer_radio,
		obj_in=form_answer_radio_in_update,
	)

	assert form_answer_radio_2
	assert form_answer_radio_2.label == new_label



@pytest.mark.asyncio
async def test_delete_form_answer_radio(
	db: AsyncSession,
) -> None:
	# --

	radio_selected = {
		'a': 'abc',
	}

	form_answer_radio_in = FormEntryAnswerRadioSchemaCreate(
		radio_selected=radio_selected,
	)

	form_answer_radio = await form_answer_radio_crud.create(
		db=db,
		obj_in=form_answer_radio_in,
	)

	form_answer_radio_2 = await form_answer_radio_crud.delete(
		db=db,
		id=form_answer_radio.id,
	)

	form_answer_radio_3 = await form_answer_radio_crud.get(
		db=db,
		id=form_answer_radio.id,
	)


	assert form_answer_radio_3 is None
	assert form_answer_radio_2.id == form_answer_radio.id



@pytest.mark.asyncio
async def test_delete_sync_form_answer_radio(
	db: AsyncSession,
) -> None:
	# --

	radio_selected = {
		'a': 'abc',
	}

	form_answer_radio_in = FormEntryAnswerRadioSchemaCreate(
		radio_selected=radio_selected,
	)

	form_answer_radio = await db.run_sync(
		form_answer_radio_crud.create_sync,
		obj_in=form_answer_radio_in,
	)

	form_answer_radio_2 = await db.run_sync(
		form_answer_radio_crud.delete_sync,
		id=form_answer_radio.id,
	)

	form_answer_radio_3 = await db.run_sync(
		form_answer_radio_crud.get_sync,
		id=form_answer_radio.id,
	)


	assert form_answer_radio_3 is None
	assert form_answer_radio_2.id == form_answer_radio.id




