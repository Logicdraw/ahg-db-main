from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.resource.type.pdf import (
	resource_pdf_crud,
)

from main.schemas.resource.type.pdf import (
	ResourcePDFSchemaCreate,
	ResourcePDFSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest




@pytest.mark.asyncio
async def test_create_resource_pdf(
	db: AsyncSession,
) -> None:
	# --
	pdf_url = random_lower_string()

	resource_pdf_in = ResourcePDFSchemaCreate(
		pdf_url=pdf_url,
	)

	resource_pdf = await resource_pdf_crud.create(
		db=db,
		obj_in=resource_pdf_in,
	)

	assert resource_pdf.pdf_url == pdf_url


@pytest.mark.asyncio
async def test_create_sync_resource_pdf(
	db: AsyncSession,
) -> None:
	# --
	pdf_url = random_lower_string()

	resource_pdf_in = ResourcePDFSchemaCreate(
		pdf_url=pdf_url,
	)

	resource_pdf = await db.run_sync(
		resource_pdf_crud.create_sync,
		obj_in=resource_pdf_in,
	)

	assert resource_pdf.pdf_url == pdf_url



@pytest.mark.asyncio
async def test_get_resource_pdf(
	db: AsyncSession,
) -> None:
	# --

	pdf_url = random_lower_string()

	resource_pdf_in = ResourcePDFSchemaCreate(
		pdf_url=pdf_url,
	)

	resource_pdf = await resource_pdf_crud.create(
		db=db,
		obj_in=resource_pdf_in,
	)

	resource_pdf_2 = await resource_pdf_crud.get(
		db=db,
		id=resource_pdf.id,
	)

	assert resource_pdf_2
	assert jsonable_encoder(resource_pdf_2) == jsonable_encoder(resource_pdf)



@pytest.mark.asyncio
async def test_get_sync_resource_pdf(
	db: AsyncSession,
) -> None:
	# --

	pdf_url = random_lower_string()

	resource_pdf_in = ResourcePDFSchemaCreate(
		pdf_url=pdf_url,
	)

	resource_pdf = await db.run_sync(
		resource_pdf_crud.create_sync,
		obj_in=resource_pdf_in,
	)

	resource_pdf_2 = await db.run_sync(
		resource_pdf_crud.get_sync,
		id=resource_pdf.id,
	)

	assert resource_pdf_2
	assert jsonable_encoder(resource_pdf_2) == jsonable_encoder(resource_pdf)



@pytest.mark.asyncio
async def test_update_resource_pdf(
	db: AsyncSession,
) -> None:
	# --

	pdf_url = random_lower_string()

	resource_pdf_in = ResourcePDFSchemaCreate(
		pdf_url=pdf_url,
	)

	resource_pdf = await resource_pdf_crud.create(
		db=db,
		obj_in=resource_pdf_in,
	)

	new_pdf_url = random_lower_string()
	while new_pdf_url == pdf_url:
		new_pdf_url = random_lower_string()

	resource_pdf_in_update = ResourcePDFSchemaUpdate(
		pdf_url=new_pdf_url,
	)

	resource_pdf_2 = await resource_pdf_crud.update(
		db=db,
		db_obj=resource_pdf,
		obj_in=resource_pdf_in_update,
	)

	assert resource_pdf_2
	assert resource_pdf_2.pdf_url
	assert resource_pdf_2.pdf_url == new_pdf_url



@pytest.mark.asyncio
async def test_update_sync_resource_pdf(
	db: AsyncSession,
) -> None:
	# --

	pdf_url = random_lower_string()

	resource_pdf_in = ResourcePDFSchemaCreate(
		pdf_url=pdf_url,
	)

	resource_pdf = await db.run_sync(
		resource_pdf_crud.create_sync,
		obj_in=resource_pdf_in,
	)

	new_pdf_url = random_lower_string()
	while new_pdf_url == pdf_url:
		new_pdf_url = random_lower_string()

	resource_pdf_in_update = ResourcePDFSchemaUpdate(
		pdf_url=new_pdf_url,
	)

	resource_pdf_2 = await db.run_sync(
		resource_pdf_crud.update_sync,
		db_obj=resource_pdf,
		obj_in=resource_pdf_in_update,
	)

	assert resource_pdf_2
	assert resource_pdf_2.pdf_url
	assert resource_pdf_2.pdf_url == new_pdf_url



@pytest.mark.asyncio
async def test_delete_resource_pdf(
	db: AsyncSession,
) -> None:
	# --

	pdf_url = random_lower_string()

	resource_pdf_in = ResourcePDFSchemaCreate(
		pdf_url=pdf_url,
	)

	resource_pdf = await resource_pdf_crud.create(
		db=db,
		obj_in=resource_pdf_in,
	)

	resource_pdf_2 = await resource_pdf_crud.delete(
		db=db,
		id=resource_pdf.id,
	)

	resource_pdf_3 = await resource_pdf_crud.get(
		db=db,
		id=resource_pdf.id,
	)

	assert resource_pdf_3 is None
	assert resource_pdf_2.id == resource_pdf.id



@pytest.mark.asyncio
async def test_delete_sync_resource_pdf(
	db: AsyncSession,
) -> None:
	# --

	pdf_url = random_lower_string()

	resource_pdf_in = ResourcePDFSchemaCreate(
		pdf_url=pdf_url,
	)

	resource_pdf = await db.run_sync(
		resource_pdf_crud.create_sync,
		obj_in=resource_pdf_in,
	)

	resource_pdf_2 = await db.run_sync(
		resource_pdf_crud.delete_sync,
		id=resource_pdf.id,
	)

	resource_pdf_3 = await db.run_sync(
		resource_pdf_crud.get_sync,
		id=resource_pdf.id,
	)

	assert resource_pdf_3 is None
	assert resource_pdf_2.id == resource_pdf.id






