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
	RegistrationFinancialsMixin,
	SpngRegistrationFinancialsMixin,
	PlayerRegistrationMixin,
)



class TeamInstanceRegistrationModel(
	RegistrationBaseModel,
	ResourceMixin,
	SpngRegistrationMixin,
	RegistrationFinancialsMixin,
	SpngRegistrationFinancialsMixin,
	PlayerRegistrationMixin,
):

	__tablename__ = 'team_instance_registrations'


	team_instances_team_instance_registrations = relationship(
		'TeamInstancesTeamInstanceRegistrationsModel',
		back_populates='team_instance_registrations_sc',
		lazy='selectin',
	)



	spng_survey_team_instances_sc = relationship(
		'SpngSurveyTeamInstanceModel',
		back_populates='team_instance_registrations',
	)

	spng_survey_team_instance_id = Column(
		Integer,
		ForeignKey('spng_survey_team_instances.id'),
	)



	# sum jersey_sponsors total (quick function)



	needs_jersey = Column(
		Boolean,
		server_default='0',
	)

	needs_socks = Column(
		Boolean,
		server_default='0',
	)



	team_instance_jersey_socks_orders = relationship(
		'TeamInstanceJerseySocksOrderModel',
		back_populates='team_instance_registrations_sc',
		lazy='selectin',
	)



	team_instance_jersey_socks_order_requests = relationship(
		'TeamInstanceJerseySocksOrderRequestModel',
		back_populates='team_instance_registrations_sc',
		lazy='selectin',
	)



	team_instance_registration_invites_sc = relationship(
		'TeamInstanceRegistrationInviteModel',
		back_populates='team_instance_registrations_sc',
		uselist=False,
	)



	team_instance_jersey_sponsor_orders = relationship(
		'TeamInstanceJerseySponsorOrderModel',
		back_populates='team_instance_registrations_sc',
		lazy='dynamic',
	)


	team_instance_jersey_sponsor_order_requests = relationship(
		'TeamInstanceJerseySponsorOrderRequestModel',
		back_populates='team_instance_registrations_sc',
		lazy='dynamic',
	)



	# Polymorphic identity ---

	__mapper_args__ = {
		'polymorphic_identity': 'team_instance',
		'concrete': True,
		'eager_defaults': True,
	}



# staging -- pgweb -- .

# pg-web could be -- .



