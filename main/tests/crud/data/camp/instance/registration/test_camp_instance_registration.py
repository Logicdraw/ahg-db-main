# SAVE FOR LATER (LAST!!) --


from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.data.camp.instance.registration import (
	camp_instance_registration_crud,
)

from main.schemas.data.camp.instance.registration import (
	CampInstanceRegistrationSchemaCreate,
	CampInstanceRegistrationSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest



@pytest.mark.asyncio
async def test_create_camp_instance_registration(
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


	camp_instance_registration_in = CampInstanceRegistrationSchemaCreate(
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

	camp_instance_registration = await camp_instance_registration_crud.create(
		db=db,
		obj_in=camp_instance_registration_in,
	)

	assert camp_instance_registration.placed_at_datetime == placed_at_datetime
	assert camp_instance_registration.notes == notes



@pytest.mark.asyncio
async def test_create_sync_camp_instance_registration(
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


	camp_instance_registration_in = CampInstanceRegistrationSchemaCreate(
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

	camp_instance_registration = await db.run_sync(
		camp_instance_registration_crud.create_sync,
		obj_in=camp_instance_registration_in,
	)

	assert camp_instance_registration.placed_at_datetime == placed_at_datetime
	assert camp_instance_registration.notes == notes



@pytest.mark.asyncio
async def test_get_camp_instance_registration(
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


	camp_instance_registration_in = CampInstanceRegistrationSchemaCreate(
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

	camp_instance_registration = await camp_instance_registration_crud.create(
		db=db,
		obj_in=camp_instance_registration_in,
	)

	camp_instance_registration_2 = await camp_instance_registration_crud.get(
		db=db,
		id=camp_instance_registration.id,
	)

	assert camp_instance_registration_2
	assert jsonable_encoder(camp_instance_registration_2) == jsonable_encoder(camp_instance_registration)


@pytest.mark.asyncio
async def test_get_sync_camp_instance_registration(
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


	camp_instance_registration_in = CampInstanceRegistrationSchemaCreate(
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

	camp_instance_registration = await db.run_sync(
		camp_instance_registration_crud.create_sync,
		obj_in=camp_instance_registration_in,
	)

	camp_instance_registration_2 = await db.run_sync(
		camp_instance_registration_crud.get_sync,
		id=camp_instance_registration.id,
	)

	assert camp_instance_registration_2
	assert jsonable_encoder(camp_instance_registration_2) == jsonable_encoder(camp_instance_registration)




@pytest.mark.asyncio
async def test_update_camp_instance_registration(
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


	camp_instance_registration_in = CampInstanceRegistrationSchemaCreate(
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

	camp_instance_registration = await camp_instance_registration_crud.create(
		db=db,
		obj_in=camp_instance_registration_in,
	)


	new_comment = random_lower_string()
	while new_comment == comment:
		new_comment = random_lower_string()

	camp_instance_registration_in_update = CampInstanceRegistrationSchemaCreate(
		comment=new_comment,
	)

	camp_instance_registration_2 = await camp_instance_registration_crud.update(
		db=db,
		db_obj=camp_instance_registration,
		obj_in=camp_instance_registration_in_update,
	)

	assert camp_instance_registration_2
	assert camp_instance_registration_2.comment == new_comment



@pytest.mark.asyncio
async def test_update_sync_camp_instance_registration(
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


	camp_instance_registration_in = CampInstanceRegistrationSchemaCreate(
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

	camp_instance_registration = await db.run_sync(
		camp_instance_registration_crud.create_sync,
		obj_in=camp_instance_registration_in,
	)

	new_comment = random_lower_string()
	while new_comment == comment:
		new_comment = random_lower_string()

	camp_instance_registration_in_update = CampInstanceRegistrationSchemaCreate(
		comment=new_comment,
	)

	camp_instance_registration_2 = await db.run_sync(
		camp_instance_registration_crud.update_sync,
		db_obj=camp_instance_registration,
		obj_in=camp_instance_registration_in_update,
	)

	assert camp_instance_registration_2
	assert camp_instance_registration_2.comment == new_comment




@pytest.mark.asyncio
async def test_delete_camp_instance_registration(
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


	camp_instance_registration_in = CampInstanceRegistrationSchemaCreate(
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

	camp_instance_registration = await camp_instance_registration_crud.create(
		db=db,
		obj_in=camp_instance_registration_in,
	)

	camp_instance_registration_2 = await camp_instance_registration_crud.delete(
		db=db,
		id=camp_instance_registration.id,
	)

	camp_instance_registration_3 = await camp_instance_registration_crud.get(
		db=db,
		id=camp_instance_registration.id,
	)


	assert camp_instance_registration_3 is None
	assert camp_instance_registration_2.id == camp_instance_registration.id



@pytest.mark.asyncio
async def test_delete_sync_camp_instance_registration(
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


	camp_instance_registration_in = CampInstanceRegistrationSchemaCreate(
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

	camp_instance_registration = await db.run_sync(
		camp_instance_registration_crud.create_sync,
		obj_in=camp_instance_registration_in,
	)


	camp_instance_registration_2 = await db.run_sync(
		camp_instance_registration_crud.delete_sync,
		id=camp_instance_registration.id,
	)

	camp_instance_registration_3 = await db.run_sync(
		camp_instance_registration_crud.get_sync,
		id=camp_instance_registration.id,
	)


	assert camp_instance_registration_3 is None
	assert camp_instance_registration_2.id == camp_instance_registration.id





