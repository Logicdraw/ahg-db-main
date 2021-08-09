from sqlalchemy import (
	Boolean,
	Column,
	ForeignKey,
	Integer,
	String,
	Date,
	Text,
	Float,
	JSON,
)


from sqlalchemy.orm import relationship

from main.utils.sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)

from main.database.base_class import Base


from sqlalchemy.dialects.postgresql import JSONB

from sqlalchemy_json import mutable_json_type



from main.config import settings


from sqlalchemy.ext.declarative import AbstractConcreteBase


from sqlalchemy.dialects.postgresql import JSONB

from sqlalchemy_json import mutable_json_type



from sqlalchemy.ext.declarative import declared_attr




class RegistrationInviteBaseModel(
	AbstractConcreteBase,
	Base,
):

	id = Column(
		Integer,
		primary_key=True,
		index=True,
		autoincrement=True,
	)


	email_to = Column(
		String,
		index=True,
	)

	has_registered = Column(
		Boolean,
		default=False,
	)


	extra_question_answers = Column(
		mutable_json_type(
			dbtype=JSONB,
			nested=False,
		)
	)


	__mapper_args__ = {
		'eager_defaults': True,
	}


