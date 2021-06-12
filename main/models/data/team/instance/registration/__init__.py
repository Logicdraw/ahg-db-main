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
	ResourceMixin,
	SpngRegistrationBase,
	SpngRegistrationFinancialsBase,
	PlayerRegistrationBase,
):

	__tablename__ = 'team_instance_registrations'


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



	jersey_sponsors = relationship(
		'TeamInstanceRegistrationJerseySponsorModel',
		back_populates='team_instance_registration',
		lazy='selectin',
	)

	# sum jersey_sponsors total (quick function)



	needs_jersey = Column(Boolean, server_default='0')

	needs_socks = Column(Boolean, server_default='0')



	# One - to - One
	jersey_socks_order = relationship(
		'TeamInstanceJerseySocksOrderModel',
		back_populates='team_instance_registration',
		uselist=False,
	)



	# Polymorphic identity ---

	__mapper_args__ = {
		'polymorphic_identity': 'team_instance',
		'concrete': True,
		'eager_defaults': True,
	}



# staging -- pgweb -- .

# pg-web could be -- .