from sqlalchemy import (
	Boolean,
	Column,
	ForeignKey,
	Integer,
	String,
	Enum,
)

from sqlalchemy.orm import relationship

from main.database.base_class import Base

from main.utils.sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)



from collections import OrderedDict



class TeamInstanceModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'team_instances'


	id = Column(
		Integer,
		primary_key=True,
		index=True,
	)


	teams_sc = relationship(
		'TeamModel',
		back_populates='team_instances',
	)

	team_id = Column(
		Integer,
		ForeignKey('teams.id'),
	)


	division_instances_sc = relationship(
		'DivisionInstanceModel',
		back_populates='team_instances',
	)

	division_instance_id = Column(
		Integer,
		ForeignKey('division_instances.id'),
	)


	conference_instances_sc = relationship(
		'ConferenceInstanceModel',
		back_populates='team_instances',
	)
	conference_instance_id = Column(
		Integer,
		ForeignKey('conference_instances.id'),
	)


	league_instances_sc = relationship(
		'LeagueInstanceModel',
		back_populates='team_instances',
	)
	league_instance_id = Column(
		Integer,
		ForeignKey('league_instances.id'),
	)


	season_instances_sc = relationship(
		'SeasonInstanceModel',
		back_populates='team_instances',
	)

	season_instance_id = Column(
		Integer,
		ForeignKey('season_instances.id'),
	)



	team_instances_team_instance_registrations = relationship(
		'TeamInstancesTeamInstanceRegistrationsModel',
		back_populates='team_instances_sc',
		lazy='selectin',
	)


	team_instances_players = relationship(
		'TeamInstancesPlayersModel',
		back_populates='team_instances_sc',
		lazy='selectin',
	)

	team_instances_coaches = relationship(
		'TeamInstancesCoachesModel',
		back_populates='team_instances_sc',
		lazy='selectin',
	)

	team_instances_adult_reps = relationship(
		'TeamInstancesAdultRepsModel',
		back_populates='team_instances_sc',
		lazy='selectin',
	)


	team_instance_jersey_socks_orders = relationship(
		'TeamInstanceJerseySocksOrderModel',
		back_populates='team_instances_sc',
		lazy='selectin',
	)

	team_instance_jersey_sponsor_orders = relationship(
		'TeamInstanceJerseySponsorOrderModel',
		back_populates='team_instances_sc',
		lazy='dynamic',
	)

	team_instance_tracksuit_orders = relationship(
		'TeamInstanceTracksuitOrderModel',
		back_populates='team_instances_sc',
		lazy='selectin',
	)



	team_instance_jersey_socks_order_requests = relationship(
		'TeamInstanceJerseySocksOrderRequestModel',
		back_populates='team_instances_sc',
		lazy='selectin',
	)

	team_instance_jersey_sponsor_order_requests = relationship(
		'TeamInstanceJerseySponsorOrderRequestModel',
		back_populates='team_instances_sc',
		lazy='dynamic',
	)

	team_instance_tracksuit_order_requests = relationship(
		'TeamInstanceTracksuitOrderRequestModel',
		back_populates='team_instances_sc',
		lazy='selectin',
	)



	team_instance_jersey_socks_order_group_sheets = relationship(
		'TeamInstanceJerseySocksOrderGroupSheetModel',
		back_populates='team_instances_sc',
		lazy='selectin',
	)

	team_instance_jersey_sponsor_order_group_sheets = relationship(
		'TeamInstanceJerseySponsorOrderGroupSheetModel',
		back_populates='team_instances_sc',
		lazy='dynamic',
	)

	team_instance_tracksuit_order_group_sheets = relationship(
		'TeamInstanceTracksuitOrderGroupSheetModel',
		back_populates='team_instances_sc',
		lazy='selectin',
	)


	team_instance_registration_invites = relationship(
		'TeamInstanceRegistrationInviteModel',
		back_populates='team_instances_sc',
		lazy='selectin',
	)



	year_start = Column(
		Integer,
	)

	year_end = Column(
		Integer,
	)
	
	
	birth_year = Column(
		Integer,
	)



	# SportsEngine --

	spng_name_snake = Column(
		String,
		index=True,
	)

	spng_shared_question_id = Column(
		Integer,
		index=True,
	)


	# Gamesheet --

	gs_team_id = Column(
		Integer,
	)





	# Tracksuit Orders --

	number_of_tracksuits_available = Column(
		Integer,
	)



	# Jersey orders --

	jersey_numbers_options = Column(
		String,
	)
	# Example: 0:68-70:99 | (inclusive)
	# or: 0:10-11,12,13-15:99


	has_jersey_size_option = Column(
		Boolean,
		server_default='0',
	)

	jersey_sizes_options = Column(
		String,
	)



	# What does this mean? --
	registrations_needs_jersey_default_value = Column(
		Boolean,
		default=False,
	)


	# Socks orders --

	has_socks_size_option = Column(
		Boolean,
		server_default='0',
	)

	socks_sizes_options = Column(
		String,
	)


	# What does this mean? --
	registrations_needs_socks_default_value = Column(
		Boolean,
		default=False,
	)


	__mapper_args__ = {
		'eager_defaults': True,
	}




