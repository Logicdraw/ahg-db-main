# SAVE FOR LATER (LAST) !


from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.program.instance.registration import (
	program_instance_registration_crud,
)

from main.schemas.data.program.instance.registration import (
	ProgramInstanceRegistrationSchemaCreate,
	ProgramInstanceRegistrationSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
	random_number,
)


import pytest


import datetime

import pytz





@pytest.mark.asyncio
async def test_create_program_instance_registration(
	db: AsyncSession,
) -> None:
	# --

	placed_at_datetime = datetime.datetime.now(pytz.utc)
	comment = random_lower_string()
	coaches_comment = random_lower_string()
	notes = random_lower_string()

	se_survey_id = random_number()
	se_survey_result_id = random_number()
	se_persona_id = random_number()
	se_user_id = random_number()
	roster_player_id = random_number()
	status = random_lower_string()
	completed = True
	registration_sport = random_lower_string()
	registration_type = random_lower_string()
	registrant_type = random_lower_string()
	extra_question_answers = {
		'apple': 'pie',
	}

	gross = float(random_number())
	net = float(random_number())
	service_fee = float(random_number())
	gross_forecast = float(random_number())
	net_forecast = float(random_number())
	service_fee_forecast = float(random_number())
	gross_outstanding = float(random_number())
	order_number = float(random_number())
	discounts = float(random_number())
	refunds = float(random_number())
	position = random_lower_string()
	invited_by_coach = True
	registration_insurance = True

	player_submitted_notes = random_lower_string()


	program_instance_registration_in = ProgramInstanceRegistrationSchemaCreate(
		placed_at_datetime=placed_at_datetime,
		comment=comment,
		coaches_comment=coaches_comment,
		notes=notes,
		se_survey_id=se_survey_id,
		se_survey_result_id=se_survey_result_id,
		se_persona_id=se_persona_id,
		se_user_id=se_user_id,
		roster_player_id=roster_player_id,
		status=status,
		completed=completed,
		registration_sport=registration_sport,
		registration_type=registration_type,
		registrant_type=registrant_type,
		extra_question_answers=extra_question_answers,
		gross=gross,
		net=net,
		service_fee=service_fee,
		gross_forecast=gross_forecast,
		net_forecast=net_forecast,
		service_fee_forecast=service_fee_forecast,
		gross_outstanding=gross_outstanding,
		order_number=order_number,
		discounts=discounts,
		refunds=refunds,
		position=position,
		invited_by_coach=invited_by_coach,
		registration_insurance=registration_insurance,
		player_submitted_notes=player_submitted_notes,
	)

	program_instance_registration = await program_instance_registration_crud.create(
		db=db,
		obj_in=program_instance_registration_in,
	)

	assert program_instance_registration.placed_at_datetime == placed_at_datetime
	assert program_instance_registration.notes == notes



@pytest.mark.asyncio
async def test_create_sync_program_instance_registration(
	db: AsyncSession,
) -> None:
	# --

	placed_at_datetime = datetime.datetime.now(pytz.utc)
	comment = random_lower_string()
	coaches_comment = random_lower_string()
	notes = random_lower_string()
	
	se_survey_id = random_number()
	se_survey_result_id = random_number()
	se_persona_id = random_number()
	se_user_id = random_number()
	roster_player_id = random_number()
	status = random_lower_string()
	completed = True
	registration_sport = random_lower_string()
	registration_type = random_lower_string()
	registrant_type = random_lower_string()
	extra_question_answers = {
		'apple': 'pie',
	}

	gross = float(random_number())
	net = float(random_number())
	service_fee = float(random_number())
	gross_forecast = float(random_number())
	net_forecast = float(random_number())
	service_fee_forecast = float(random_number())
	gross_outstanding = float(random_number())
	order_number = float(random_number())
	discounts = float(random_number())
	refunds = float(random_number())
	position = random_lower_string()
	invited_by_coach = True
	registration_insurance = True

	player_submitted_notes = random_lower_string()


	program_instance_registration_in = ProgramInstanceRegistrationSchemaCreate(
		placed_at_datetime=placed_at_datetime,
		comment=comment,
		coaches_comment=coaches_comment,
		notes=notes,
		se_survey_id=se_survey_id,
		se_survey_result_id=se_survey_result_id,
		se_persona_id=se_persona_id,
		se_user_id=se_user_id,
		roster_player_id=roster_player_id,
		status=status,
		completed=completed,
		registration_sport=registration_sport,
		registration_type=registration_type,
		registrant_type=registrant_type,
		extra_question_answers=extra_question_answers,
		gross=gross,
		net=net,
		service_fee=service_fee,
		gross_forecast=gross_forecast,
		net_forecast=net_forecast,
		service_fee_forecast=service_fee_forecast,
		gross_outstanding=gross_outstanding,
		order_number=order_number,
		discounts=discounts,
		refunds=refunds,
		position=position,
		invited_by_coach=invited_by_coach,
		registration_insurance=registration_insurance,
		player_submitted_notes=player_submitted_notes,
	)

	program_instance_registration = await db.run_sync(
		program_instance_registration_crud.create_sync,
		obj_in=program_instance_registration_in,
	)

	assert program_instance_registration.placed_at_datetime == placed_at_datetime
	assert program_instance_registration.notes == notes



@pytest.mark.asyncio
async def test_get_program_instance_registration(
	db: AsyncSession,
) -> None:
	# --

	placed_at_datetime = datetime.datetime.now(pytz.utc)
	comment = random_lower_string()
	coaches_comment = random_lower_string()
	notes = random_lower_string()

	se_survey_id = random_number()
	se_survey_result_id = random_number()
	se_persona_id = random_number()
	se_user_id = random_number()
	roster_player_id = random_number()
	status = random_lower_string()
	completed = True
	registration_sport = random_lower_string()
	registration_type = random_lower_string()
	registrant_type = random_lower_string()
	extra_question_answers = {
		'apple': 'pie',
	}

	gross = float(random_number())
	net = float(random_number())
	service_fee = float(random_number())
	gross_forecast = float(random_number())
	net_forecast = float(random_number())
	service_fee_forecast = float(random_number())
	gross_outstanding = float(random_number())
	order_number = float(random_number())
	discounts = float(random_number())
	refunds = float(random_number())
	position = random_lower_string()
	invited_by_coach = True
	registration_insurance = True

	player_submitted_notes = random_lower_string()


	program_instance_registration_in = ProgramInstanceRegistrationSchemaCreate(
		placed_at_datetime=placed_at_datetime,
		comment=comment,
		coaches_comment=coaches_comment,
		notes=notes,
		se_survey_id=se_survey_id,
		se_survey_result_id=se_survey_result_id,
		se_persona_id=se_persona_id,
		se_user_id=se_user_id,
		roster_player_id=roster_player_id,
		status=status,
		completed=completed,
		registration_sport=registration_sport,
		registration_type=registration_type,
		registrant_type=registrant_type,
		extra_question_answers=extra_question_answers,
		gross=gross,
		net=net,
		service_fee=service_fee,
		gross_forecast=gross_forecast,
		net_forecast=net_forecast,
		service_fee_forecast=service_fee_forecast,
		gross_outstanding=gross_outstanding,
		order_number=order_number,
		discounts=discounts,
		refunds=refunds,
		position=position,
		invited_by_coach=invited_by_coach,
		registration_insurance=registration_insurance,
		player_submitted_notes=player_submitted_notes,
	)

	program_instance_registration = await program_instance_registration_crud.create(
		db=db,
		obj_in=program_instance_registration_in,
	)

	program_instance_registration_2 = await program_instance_registration_crud.get(
		db=db,
		id=program_instance_registration.id,
	)

	assert program_instance_registration_2
	assert jsonable_encoder(program_instance_registration_2) == jsonable_encoder(program_instance_registration)


@pytest.mark.asyncio
async def test_get_sync_program_instance_registration(
	db: AsyncSession,
) -> None:
	# --

	placed_at_datetime = datetime.datetime.now(pytz.utc)
	comment = random_lower_string()
	coaches_comment = random_lower_string()
	notes = random_lower_string()
	
	se_survey_id = random_number()
	se_survey_result_id = random_number()
	se_persona_id = random_number()
	se_user_id = random_number()
	roster_player_id = random_number()
	status = random_lower_string()
	completed = True
	registration_sport = random_lower_string()
	registration_type = random_lower_string()
	registrant_type = random_lower_string()
	extra_question_answers = {
		'apple': 'pie',
	}

	gross = float(random_number())
	net = float(random_number())
	service_fee = float(random_number())
	gross_forecast = float(random_number())
	net_forecast = float(random_number())
	service_fee_forecast = float(random_number())
	gross_outstanding = float(random_number())
	order_number = float(random_number())
	discounts = float(random_number())
	refunds = float(random_number())
	position = random_lower_string()
	invited_by_coach = True
	registration_insurance = True

	player_submitted_notes = random_lower_string()


	program_instance_registration_in = ProgramInstanceRegistrationSchemaCreate(
		placed_at_datetime=placed_at_datetime,
		comment=comment,
		coaches_comment=coaches_comment,
		notes=notes,
		se_survey_id=se_survey_id,
		se_survey_result_id=se_survey_result_id,
		se_persona_id=se_persona_id,
		se_user_id=se_user_id,
		roster_player_id=roster_player_id,
		status=status,
		completed=completed,
		registration_sport=registration_sport,
		registration_type=registration_type,
		registrant_type=registrant_type,
		extra_question_answers=extra_question_answers,
		gross=gross,
		net=net,
		service_fee=service_fee,
		gross_forecast=gross_forecast,
		net_forecast=net_forecast,
		service_fee_forecast=service_fee_forecast,
		gross_outstanding=gross_outstanding,
		order_number=order_number,
		discounts=discounts,
		refunds=refunds,
		position=position,
		invited_by_coach=invited_by_coach,
		registration_insurance=registration_insurance,
		player_submitted_notes=player_submitted_notes,
	)

	program_instance_registration = await db.run_sync(
		program_instance_registration_crud.create_sync,
		obj_in=program_instance_registration_in,
	)

	program_instance_registration_2 = await db.run_sync(
		program_instance_registration_crud.get_sync,
		id=program_instance_registration.id,
	)

	assert program_instance_registration_2
	assert jsonable_encoder(program_instance_registration_2) == jsonable_encoder(program_instance_registration)




@pytest.mark.asyncio
async def test_update_program_instance_registration(
	db: AsyncSession,
) -> None:
	# --

	placed_at_datetime = datetime.datetime.now(pytz.utc)
	comment = random_lower_string()
	coaches_comment = random_lower_string()
	notes = random_lower_string()

	se_survey_id = random_number()
	se_survey_result_id = random_number()
	se_persona_id = random_number()
	se_user_id = random_number()
	roster_player_id = random_number()
	status = random_lower_string()
	completed = True
	registration_sport = random_lower_string()
	registration_type = random_lower_string()
	registrant_type = random_lower_string()
	extra_question_answers = {
		'apple': 'pie',
	}

	gross = float(random_number())
	net = float(random_number())
	service_fee = float(random_number())
	gross_forecast = float(random_number())
	net_forecast = float(random_number())
	service_fee_forecast = float(random_number())
	gross_outstanding = float(random_number())
	order_number = float(random_number())
	discounts = float(random_number())
	refunds = float(random_number())
	position = random_lower_string()
	invited_by_coach = True
	registration_insurance = True

	player_submitted_notes = random_lower_string()


	program_instance_registration_in = ProgramInstanceRegistrationSchemaCreate(
		placed_at_datetime=placed_at_datetime,
		comment=comment,
		coaches_comment=coaches_comment,
		notes=notes,
		se_survey_id=se_survey_id,
		se_survey_result_id=se_survey_result_id,
		se_persona_id=se_persona_id,
		se_user_id=se_user_id,
		roster_player_id=roster_player_id,
		status=status,
		completed=completed,
		registration_sport=registration_sport,
		registration_type=registration_type,
		registrant_type=registrant_type,
		extra_question_answers=extra_question_answers,
		gross=gross,
		net=net,
		service_fee=service_fee,
		gross_forecast=gross_forecast,
		net_forecast=net_forecast,
		service_fee_forecast=service_fee_forecast,
		gross_outstanding=gross_outstanding,
		order_number=order_number,
		discounts=discounts,
		refunds=refunds,
		position=position,
		invited_by_coach=invited_by_coach,
		registration_insurance=registration_insurance,
		player_submitted_notes=player_submitted_notes,
	)

	program_instance_registration = await program_instance_registration_crud.create(
		db=db,
		obj_in=program_instance_registration_in,
	)


	new_comment = random_lower_string()
	while new_comment == comment:
		new_comment = random_lower_string()

	program_instance_registration_in_update = ProgramInstanceRegistrationSchemaCreate(
		comment=new_comment,
	)

	program_instance_registration_2 = await program_instance_registration_crud.update(
		db=db,
		db_obj=program_instance_registration,
		obj_in=program_instance_registration_in_update,
	)

	assert program_instance_registration_2
	assert program_instance_registration_2.comment == new_comment



@pytest.mark.asyncio
async def test_update_sync_program_instance_registration(
	db: AsyncSession,
) -> None:
	# --

	placed_at_datetime = datetime.datetime.now(pytz.utc)
	comment = random_lower_string()
	coaches_comment = random_lower_string()
	notes = random_lower_string()
	
	se_survey_id = random_number()
	se_survey_result_id = random_number()
	se_persona_id = random_number()
	se_user_id = random_number()
	roster_player_id = random_number()
	status = random_lower_string()
	completed = True
	registration_sport = random_lower_string()
	registration_type = random_lower_string()
	registrant_type = random_lower_string()
	extra_question_answers = {
		'apple': 'pie',
	}

	gross = float(random_number())
	net = float(random_number())
	service_fee = float(random_number())
	gross_forecast = float(random_number())
	net_forecast = float(random_number())
	service_fee_forecast = float(random_number())
	gross_outstanding = float(random_number())
	order_number = float(random_number())
	discounts = float(random_number())
	refunds = float(random_number())
	position = random_lower_string()
	invited_by_coach = True
	registration_insurance = True

	player_submitted_notes = random_lower_string()


	program_instance_registration_in = ProgramInstanceRegistrationSchemaCreate(
		placed_at_datetime=placed_at_datetime,
		comment=comment,
		coaches_comment=coaches_comment,
		notes=notes,
		se_survey_id=se_survey_id,
		se_survey_result_id=se_survey_result_id,
		se_persona_id=se_persona_id,
		se_user_id=se_user_id,
		roster_player_id=roster_player_id,
		status=status,
		completed=completed,
		registration_sport=registration_sport,
		registration_type=registration_type,
		registrant_type=registrant_type,
		extra_question_answers=extra_question_answers,
		gross=gross,
		net=net,
		service_fee=service_fee,
		gross_forecast=gross_forecast,
		net_forecast=net_forecast,
		service_fee_forecast=service_fee_forecast,
		gross_outstanding=gross_outstanding,
		order_number=order_number,
		discounts=discounts,
		refunds=refunds,
		position=position,
		invited_by_coach=invited_by_coach,
		registration_insurance=registration_insurance,
		player_submitted_notes=player_submitted_notes,
	)

	program_instance_registration = await db.run_sync(
		program_instance_registration_crud.create_sync,
		obj_in=program_instance_registration_in,
	)

	new_comment = random_lower_string()
	while new_comment == comment:
		new_comment = random_lower_string()

	program_instance_registration_in_update = ProgramInstanceRegistrationSchemaCreate(
		comment=new_comment,
	)

	program_instance_registration_2 = await db.run_sync(
		program_instance_registration_crud.update_sync,
		db_obj=program_instance_registration,
		obj_in=program_instance_registration_in_update,
	)

	assert program_instance_registration_2
	assert program_instance_registration_2.comment == new_comment




@pytest.mark.asyncio
async def test_delete_program_instance_registration(
	db: AsyncSession,
) -> None:
	# --

	placed_at_datetime = datetime.datetime.now(pytz.utc)
	comment = random_lower_string()
	coaches_comment = random_lower_string()
	notes = random_lower_string()

	se_survey_id = random_number()
	se_survey_result_id = random_number()
	se_persona_id = random_number()
	se_user_id = random_number()
	roster_player_id = random_number()
	status = random_lower_string()
	completed = True
	registration_sport = random_lower_string()
	registration_type = random_lower_string()
	registrant_type = random_lower_string()
	extra_question_answers = {
		'apple': 'pie',
	}

	gross = float(random_number())
	net = float(random_number())
	service_fee = float(random_number())
	gross_forecast = float(random_number())
	net_forecast = float(random_number())
	service_fee_forecast = float(random_number())
	gross_outstanding = float(random_number())
	order_number = float(random_number())
	discounts = float(random_number())
	refunds = float(random_number())
	position = random_lower_string()
	invited_by_coach = True
	registration_insurance = True

	player_submitted_notes = random_lower_string()


	program_instance_registration_in = ProgramInstanceRegistrationSchemaCreate(
		placed_at_datetime=placed_at_datetime,
		comment=comment,
		coaches_comment=coaches_comment,
		notes=notes,
		se_survey_id=se_survey_id,
		se_survey_result_id=se_survey_result_id,
		se_persona_id=se_persona_id,
		se_user_id=se_user_id,
		roster_player_id=roster_player_id,
		status=status,
		completed=completed,
		registration_sport=registration_sport,
		registration_type=registration_type,
		registrant_type=registrant_type,
		extra_question_answers=extra_question_answers,
		gross=gross,
		net=net,
		service_fee=service_fee,
		gross_forecast=gross_forecast,
		net_forecast=net_forecast,
		service_fee_forecast=service_fee_forecast,
		gross_outstanding=gross_outstanding,
		order_number=order_number,
		discounts=discounts,
		refunds=refunds,
		position=position,
		invited_by_coach=invited_by_coach,
		registration_insurance=registration_insurance,
		player_submitted_notes=player_submitted_notes,
	)

	program_instance_registration = await program_instance_registration_crud.create(
		db=db,
		obj_in=program_instance_registration_in,
	)

	program_instance_registration_2 = await program_instance_registration_crud.delete(
		db=db,
		id=program_instance_registration.id,
	)

	program_instance_registration_3 = await program_instance_registration_crud.get(
		db=db,
		id=program_instance_registration.id,
	)


	assert program_instance_registration_3 is None
	assert program_instance_registration_2.id == program_instance_registration.id



@pytest.mark.asyncio
async def test_delete_sync_program_instance_registration(
	db: AsyncSession,
) -> None:
	# --

	placed_at_datetime = datetime.datetime.now(pytz.utc)
	comment = random_lower_string()
	coaches_comment = random_lower_string()
	notes = random_lower_string()
	
	se_survey_id = random_number()
	se_survey_result_id = random_number()
	se_persona_id = random_number()
	se_user_id = random_number()
	roster_player_id = random_number()
	status = random_lower_string()
	completed = True
	registration_sport = random_lower_string()
	registration_type = random_lower_string()
	registrant_type = random_lower_string()
	extra_question_answers = {
		'apple': 'pie',
	}

	gross = float(random_number())
	net = float(random_number())
	service_fee = float(random_number())
	gross_forecast = float(random_number())
	net_forecast = float(random_number())
	service_fee_forecast = float(random_number())
	gross_outstanding = float(random_number())
	order_number = float(random_number())
	discounts = float(random_number())
	refunds = float(random_number())
	position = random_lower_string()
	invited_by_coach = True
	registration_insurance = True

	player_submitted_notes = random_lower_string()


	program_instance_registration_in = ProgramInstanceRegistrationSchemaCreate(
		placed_at_datetime=placed_at_datetime,
		comment=comment,
		coaches_comment=coaches_comment,
		notes=notes,
		se_survey_id=se_survey_id,
		se_survey_result_id=se_survey_result_id,
		se_persona_id=se_persona_id,
		se_user_id=se_user_id,
		roster_player_id=roster_player_id,
		status=status,
		completed=completed,
		registration_sport=registration_sport,
		registration_type=registration_type,
		registrant_type=registrant_type,
		extra_question_answers=extra_question_answers,
		gross=gross,
		net=net,
		service_fee=service_fee,
		gross_forecast=gross_forecast,
		net_forecast=net_forecast,
		service_fee_forecast=service_fee_forecast,
		gross_outstanding=gross_outstanding,
		order_number=order_number,
		discounts=discounts,
		refunds=refunds,
		position=position,
		invited_by_coach=invited_by_coach,
		registration_insurance=registration_insurance,
		player_submitted_notes=player_submitted_notes,
	)

	program_instance_registration = await db.run_sync(
		program_instance_registration_crud.create_sync,
		obj_in=program_instance_registration_in,
	)


	program_instance_registration_2 = await db.run_sync(
		program_instance_registration_crud.delete_sync,
		id=program_instance_registration.id,
	)

	program_instance_registration_3 = await db.run_sync(
		program_instance_registration_crud.get_sync,
		id=program_instance_registration.id,
	)


	assert program_instance_registration_3 is None
	assert program_instance_registration_2.id == program_instance_registration.id




