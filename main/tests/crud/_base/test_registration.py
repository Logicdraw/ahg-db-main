from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud._base.registration import (
	registration_base_crud,
)

from main.schemas._base.registration import (
	RegistrationBaseSchemaCreate,
	RegistrationBaseSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest


import datetime

import pytz




# @pytest.mark.asyncio
# async def test_get_registration_base(
# 	db: AsyncSession,
# ) -> None:
# 	# --
# 	placed_at_datetime = datetime.datetime.now(tz=pytz.utc)
# 	comment = random_lower_string()
# 	coaches_comment = random_lower_string()
# 	notes = random_lower_string()

# 	registration_base_in = RegistrationBaseSchemaCreate(
# 		placed_at_datetime=placed_at_datetime,
# 		comment=comment,
# 		coaches_comment=coaches_comment,
# 		notes=notes,
# 		type='team_instance',
# 	)
# 	registration_base = await registration_base_crud.create(
# 		db=db,
# 		obj_in=registration_base_in,
# 	)

# 	registration_base_2 = await registration_base_crud.get(
# 		db=db,
# 		id=registration_base.id,
# 	)


# 	assert registration_base_2
# 	assert jsonable_encoder(registration_base) == jsonable_encoder(registration_base_2)



# @pytest.mark.asyncio
# async def test_update_registration_base(
# 	db: AsyncSession,
# ) -> None:
# 	# --
# 	placed_at_datetime = datetime.datetime.now(tz=pytz.utc)
# 	comment = random_lower_string()
# 	coaches_comment = random_lower_string()
# 	notes = random_lower_string()

# 	registration_base_in = RegistrationBaseSchemaCreate(
# 		placed_at_datetime=placed_at_datetime,
# 		comment=comment,
# 		coaches_comment=coaches_comment,
# 		notes=notes,
# 		type='team_instance',
# 	)
# 	registration_base = await registration_base_crud.create(
# 		db=db,
# 		obj_in=registration_base_in,
# 	)

# 	registration_base_in_update = RegistrationBaseSchemaUpdate(
# 		comment=random_lower_string(),
# 	)

# 	await registration_base_crud.update(
# 		db=db,
# 		db_obj=registration_base,
# 		obj_in=registration_base_in_update,
# 	)

# 	registration_base_2 = await registration_base_crud.get(
# 		db=db,
# 		id=registration_base.id,
# 	)


# 	assert registration_base_2
# 	assert registration_base_2.comment
# 	assert registration_base_2.comment != registration_base.comment



# @pytest.mark.asyncio
# async def test_delete_registration_base(
# 	db: AsyncSession,
# ) -> None:
# 	# --
# 	placed_at_datetime = datetime.datetime.now(tz=pytz.utc)
# 	comment = random_lower_string()
# 	coaches_comment = random_lower_string()
# 	notes = random_lower_string()

# 	registration_base_in = RegistrationBaseSchemaCreate(
# 		placed_at_datetime=placed_at_datetime,
# 		comment=comment,
# 		coaches_comment=coaches_comment,
# 		notes=notes,
# 		type='team_instance',
# 	)
# 	registration_base = await registration_base_crud.create(
# 		db=db,
# 		obj_in=registration_base_in,
# 	)

# 	registration_base_2 = await registration_base_crud.delete(
# 		db=db,
# 		id=registration_base.id,
# 	)

# 	registration_base_3 = await registration_base_crud.get(
# 		db=db,
# 		id=registration_base.id,
# 	)

# 	assert registration_base_3 is None
# 	assert registration_base_2.id == registration_base.id




# _sync ...




