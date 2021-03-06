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

from sqlalchemy.ext.declarative import declared_attr




class RegistrationBaseModel(
	AbstractConcreteBase,
	Base,
):

	id = Column(
		Integer,
		primary_key=True,
		index=True,
		autoincrement=True,
	)


	placed_at_datetime = Column(
		AwareDateTime(),
	)

	comment = Column(
		Text,
	)

	coaches_comment = Column(
		Text,
	)

	notes = Column(
		String,
	)


	@declared_attr
	def players_sc(cls):
		return relationship(
			'PlayerModel',
			back_populates='registrations',
		)

	@declared_attr
	def player_id(cls):
		return Column(
			Integer,
			ForeignKey('players.id'),
		)



	__mapper_args__ = {
		'eager_defaults': True,
	}



class SpngRegistrationMixin:
	# --

	spng_survey_id = Column(
		Integer,
	)
	spng_survey_result_id = Column(
		Integer,
		unique=True,
	)

	spng_persona_id = Column(
		Integer,
	)
	spng_user_id = Column(
		Integer,
	)
	roster_player_id = Column(
		Integer,
	)

	status = Column(
		String,
	)
	completed = Column(
		Boolean,
	)

	registration_sport = Column(
		String,
	)

	registration_type = Column(
		String,
	)

	registrant_type = Column(
		String,
	)


	extra_question_answers = Column(
		mutable_json_type(
			dbtype=JSONB,
			nested=False,
		)
	)



class RegistrationFinancialsMixin:
	# --

	total = Column(
		Float,
	)

	paid = Column(
		Float,
	)

	owes = Column(
		Float,
	)


	discounts = Column(
		Float,
	)

	discount_names = Column(
		String,
	)

	refunds = Column(
		Float,
	)

	refund_reason = Column(
		Text,
	)



class SpngRegistrationFinancialsMixin:
	# --

	spng_order_number = Column(
		String,
	)




class PlayerRegistrationMixin:
	# --

	jersey_number = Column(
		Integer,
	)

	jersey_size = Column(
		String,
	)
	

	position = Column(
		String,
	)


	registration_insurance = Column(
		Boolean,
		server_default='0',
	)

	player_submitted_notes = Column(
		String,
	)




