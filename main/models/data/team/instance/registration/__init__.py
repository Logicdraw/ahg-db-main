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

from main.utils.sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)


from main.models._base.registration import (
	RegistrationBaseModel,
	SpngRegistrationMixin,
	SpngRegistrationFinancialsMixin,
	PlayerRegistrationMixin,
)



class TeamInstanceRegistrationModel(
	RegistrationBaseModel,
	ResourceMixin,
	SpngRegistrationMixin,
	SpngRegistrationFinancialsMixin,
	PlayerRegistrationMixin,
):

	__tablename__ = 'team_instance_registrations'


	# team_instance ...
	team_instances_sc = relationship(
		'TeamInstanceModel',
		back_populates='team_instance_registrations',
		uselist=False,
	)
	team_instance_id = Column(Integer, ForeignKey('team_instances.id'))


	spng_survey_teams_sc = relationship(
		'SpngSurveyTeamModel',
		back_populates='team_instance_registrations',
		uselist=False,
	)
	spng_survey_team_id = Column(
		Integer,
		ForeignKey('spng_survey_teams.id'),
	)



	team_instance_registration_jersey_sponsors = relationship(
		'TeamInstanceRegistrationJerseySponsorModel',
		back_populates='team_instance_registrations_sc',
		lazy='selectin',
	)

	# sum jersey_sponsors total (quick function)



	needs_jersey = Column(Boolean, server_default='0')

	needs_socks = Column(Boolean, server_default='0')



	team_instance_jersey_socks_orders = relationship(
		'TeamInstanceJerseySocksOrderModel',
		back_populates='team_instance_registrations_sc',
		lazy='selectin',
	)



	# Polymorphic identity ---

	__mapper_args__ = {
		'polymorphic_identity': 'team_instance',
		'concrete': True,
		'eager_defaults': True,
	}



# staging -- pgweb -- .

# pg-web could be -- .



