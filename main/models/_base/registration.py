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

from lib.util_sqlalchemy import (
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

	id = Column(Integer, primary_key=True, index=True, autoincrement=True)
	

	placed_at_datetime = Column(AwareDateTime())

	comment = Column(Text)

	coaches_comment = Column(Text)

	notes = Column(String)


	@declared_attr
	def player(cls):
		return relationship('PlayerModel', back_populates='registrations', uselist=False,)

	@declared_attr
	def player_id(cls):
		return Column(Integer, ForeignKey('players.id'))



	# edited_by_ahg = Column(Boolean, default=False) # Non-financials
	
	# edited_financials_by_ahg = Column(Boolean, default=False) # ... Pointless ... ?




class SpngRegistrationBase:

	se_survey_id = Column(Integer)
	se_survey_result_id = Column(Integer, unique=True)

	se_persona_id = Column(Integer)
	se_user_id = Column(Integer)
	roster_player_id = Column(Integer)

	status = Column(String)
	completed = Column(Boolean)

	registration_sport = Column(String)

	registration_type = Column(String)

	registrant_type = Column(String)



	extra_question_answers = Column(
		mutable_json_type(
			dbtype=JSONB,
			nested=False,
		)
	)





class SpngRegistrationFinancialsBase:

	gross = Column(Float)

	net = Column(Float)

	service_fee = Column(Float)

	gross_forecast = Column(Float)

	net_forecast = Column(Float)

	service_fee_forecast = Column(Float)

	gross_outstanding = Column(Float)

	order_number = Column(String)

	discounts = Column(Float)
	discount_names = Column(String)

	refunds = Column(Float)




class PlayerRegistrationBase:

	position = Column(String)


	registration_insurance = Column(Boolean, default=False)

	player_submitted_notes = Column(String)


