from sqlalchemy import (
	Boolean,
	Column,
	ForeignKey,
	Integer,
	String,
	Float,
)

from sqlalchemy.orm import relationship

from main.database.base_class import Base

from lib.util_sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)


from main.models._base.registration import (
	RegistrationBaseModel,
	SpngRegistrationBase,
	SpngRegistrationFinancialsBase,
	PlayerRegistrationBase,
)



class TeamInstanceRegistrationModel(
	RegistrationBaseModel,
	SpngRegistrationBase,
	SpngRegistrationFinancialsBase,
	PlayerRegistrationBase,
):

	__tablename__ = 'team_instance_registrations'

	id = Column(Integer, ForeignKey('registrations.id'), primary_key=True)


	# team_instance ...
	team_instance = relationship(
		'TeamInstanceModel',
		back_populates='registrations',
		uselist=False,
	)
	team_instance_id = Column(Integer, ForeignKey('team_instances.id'))


	spng_survey_team = relationship(
		'SpngSurveyTeamModel',
		back_populates='registrations',
		uselist=False,
	)
	spng_survey_team_id = Column(
		Integer,
		ForeignKey('spng_survey_teams.id'),
	)



	needs_jersey = Column(Boolean, default=False)

	needs_socks = Column(Boolean, default=False)


	# One - to - One
	jersey_socks_order = relationship(
		'TeamInstanceJerseySocksOrderModel',
		back_populates='team_instance_registration',
		uselist=False,
	)




	# Polymorphic identity ---

	__mapper_args__ = {
		'polymorphic_identity': 'team_instance',
	}



# staging -- pgweb -- .

# pg-web could be -- .