from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession


from main.crud.resource.type.article import (
	resource_article_crud,
)

from main.schemas.resource.type.article import (
	ResourceArticleSchemaCreate,
	ResourceArticleSchemaUpdate,
)



from main.tests.utils import (
	random_email,
	random_lower_string,
	random_name,
)


import pytest




@pytest.mark.asyncio
async def test_create_resource_article(
	db: AsyncSession,
) -> None:
	# --
	article_body = random_lower_string()

	resource_article_in = ResourceArticleSchemaCreate(
		article_body=article_body,
	)

	resource_article = await resource_article_crud.create(
		db=db,
		obj_in=resource_article_in,
	)

	assert resource_article.article_body == article_body


@pytest.mark.asyncio
async def test_create_sync_resource_article(
	db: AsyncSession,
) -> None:
	# --
	article_body = random_lower_string()

	resource_article_in = ResourceArticleSchemaCreate(
		article_body=article_body,
	)

	resource_article = await db.run_sync(
		resource_article_crud.create_sync,
		obj_in=resource_article_in,
	)

	assert resource_article.article_body == article_body



@pytest.mark.asyncio
async def test_get_resource_article(
	db: AsyncSession,
) -> None:
	# --

	article_body = random_lower_string()

	resource_article_in = ResourceArticleSchemaCreate(
		article_body=article_body,
	)

	resource_article = await resource_article_crud.create(
		db=db,
		obj_in=resource_article_in,
	)

	resource_article_2 = await resource_article_crud.get(
		db=db,
		id=resource_article.id,
	)

	assert resource_article_2
	assert jsonable_encoder(resource_article_2) == jsonable_encoder(resource_article)



@pytest.mark.asyncio
async def test_get_sync_resource_article(
	db: AsyncSession,
) -> None:
	# --

	article_body = random_lower_string()

	resource_article_in = ResourceArticleSchemaCreate(
		article_body=article_body,
	)

	resource_article = await db.run_sync(
		resource_article_crud.create_sync,
		obj_in=resource_article_in,
	)

	resource_article_2 = await db.run_sync(
		resource_article_crud.get_sync,
		id=resource_article.id,
	)

	assert resource_article_2
	assert jsonable_encoder(resource_article_2) == jsonable_encoder(resource_article)



@pytest.mark.asyncio
async def test_update_resource_article(
	db: AsyncSession,
) -> None:
	# --

	article_body = random_lower_string()

	resource_article_in = ResourceArticleSchemaCreate(
		article_body=article_body,
	)

	resource_article = await resource_article_crud.create(
		db=db,
		obj_in=resource_article_in,
	)

	new_article_body = random_lower_string()
	while new_article_body == article_body:
		new_article_body = random_lower_string()

	resource_article_in_update = ResourceArticleSchemaUpdate(
		article_body=new_article_body,
	)

	resource_article_2 = await resource_article_crud.update(
		db=db,
		db_obj=resource_article,
		obj_in=resource_article_in_update,
	)

	assert resource_article_2
	assert resource_article_2.article_body
	assert resource_article_2.article_body == new_article_body



@pytest.mark.asyncio
async def test_update_sync_resource_article(
	db: AsyncSession,
) -> None:
	# --

	article_body = random_lower_string()

	resource_article_in = ResourceArticleSchemaCreate(
		article_body=article_body,
	)

	resource_article = await db.run_sync(
		resource_article_crud.create_sync,
		obj_in=resource_article_in,
	)

	new_article_body = random_lower_string()
	while new_article_body == article_body:
		new_article_body = random_lower_string()

	resource_article_in_update = ResourceArticleSchemaUpdate(
		article_body=new_article_body,
	)

	resource_article_2 = await db.run_sync(
		resource_article_crud.update_sync,
		db_obj=resource_article,
		obj_in=resource_article_in_update,
	)

	assert resource_article_2
	assert resource_article_2.article_body
	assert resource_article_2.article_body == new_article_body



@pytest.mark.asyncio
async def test_delete_resource_article(
	db: AsyncSession,
) -> None:
	# --

	article_body = random_lower_string()

	resource_article_in = ResourceArticleSchemaCreate(
		article_body=article_body,
	)

	resource_article = await resource_article_crud.create(
		db=db,
		obj_in=resource_article_in,
	)

	resource_article_2 = await resource_article_crud.delete(
		db=db,
		id=resource_article.id,
	)

	resource_article_3 = await resource_article_crud.get(
		db=db,
		id=resource_article.id,
	)

	assert resource_article_3 is None
	assert resource_article_2.id == resource_article.id



@pytest.mark.asyncio
async def test_delete_sync_resource_article(
	db: AsyncSession,
) -> None:
	# --

	article_body = random_lower_string()

	resource_article_in = ResourceArticleSchemaCreate(
		article_body=article_body,
	)

	resource_article = await db.run_sync(
		resource_article_crud.create_sync,
		obj_in=resource_article_in,
	)

	resource_article_2 = await db.run_sync(
		resource_article_crud.delete_sync,
		id=resource_article.id,
	)

	resource_article_3 = await db.run_sync(
		resource_article_crud.get_sync,
		id=resource_article.id,
	)

	assert resource_article_3 is None
	assert resource_article_2.id == resource_article.id






