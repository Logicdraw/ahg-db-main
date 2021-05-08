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


from lib.util_sqlalchemy import (
	AwareDateTime,
)



from sqlalchemy.dialects.postgresql import JSONB

from sqlalchemy_json import mutable_json_type



from main.config import get_settings
settings = get_settings()



class RegistrationBase:

	placed_at_datetime = Column(AwareDateTime())

	comment = Column(Text)

	coaches_comment = Column(Text)

	notes = Column(String)





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


	if settings.USE_SQLITE_FOR_TESTING:

		extra_question_answers = Column(JSON)

	else:

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


	invited_by_coach = Column(Boolean, default=False)

	registration_insurance = Column(Boolean, default=False)


	current_minor_hockey_level = Column(String)

	current_division_played = Column(String)


	preferred_language = Column(String)

	player_submitted_notes = Column(String)





