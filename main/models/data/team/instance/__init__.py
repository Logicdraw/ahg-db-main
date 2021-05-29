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

from lib.util_sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)



from collections import OrderedDict



class TeamInstanceModel(Base, ResourceMixin):

	__tablename__ = 'team_instances'


	id = Column(Integer, primary_key=True, index=True)


	team = relationship(
		'TeamModel',
		back_populates='instances',
		uselist=False,
	)
	team_id = Column(Integer, ForeignKey('teams.id'))


	division_instance = relationship(
		'DivisionInstanceModel',
		back_populates='teams',
		uselist=False,
	)
	division_instance_id = Column(Integer, ForeignKey('division_instances.id'))

	conference_instance = relationship(
		'ConferenceInstanceModel',
		back_populates='teams',
		uselist=False,
	)
	conference_instance_id = Column(Integer, ForeignKey('conference_instances.id'))

	league_instance = relationship(
		'LeagueInstanceModel',
		back_populates='teams',
		uselist=False,
	)
	league_instance_id = Column(Integer, ForeignKey('league_instances.id'))

	season_instance = relationship(
		'ConferenceInstanceModel',
		back_populates='teams',
		uselist=False,
	)
	season_instance_id = Column(Integer, ForeignKey('season_instances.id'))



	registrations = relationship(
		'TeamInstanceRegistrationModel',
		back_populates='team_instance',
		lazy='selectin',
	)


	players = relationship(
		'TeamInstancesPlayersModel',
		back_populates='team_instance',
		lazy='selectin',
	)

	coaches = relationship(
		'TeamInstancesCoachesModel',
		back_populates='team_instance',
		lazy='selectin',
	)


	jersey_socks_orders = relationship(
		'TeamInstanceJerseySocksOrderModel',
		back_populates='team_instance',
		lazy='selectin',
	)

	tracksuit_orders = relationship(
		'TeamInstanceTracksuitOrderModel',
		back_populates='team_instance',
		lazy='selectin',
	)



	year_start = Column(Integer)

	year_end = Column(Integer)
	
	
	birth_year = Column(Integer)



	# SportsEngine --

	se_name_snake = Column(String, index=True)

	se_shared_question_id = Column(Integer, index=True)


	# Gamesheet --

	gs_team_id = Column(Integer)





	# Tracksuit Orders --

	number_of_tracksuits_available = Column(Integer)



	# Jersey orders --

	jersey_numbers_options = Column(String)


	has_jersey_size_option = Column(Boolean, default=False)

	jersey_sizes_options = Column(String)



	registrations_needs_jersey_default_value = Column(
		Boolean,
		default=False,
	)


	# Socks orders --

	has_socks_size_option = Column(Boolean, default=False)

	socks_sizes_options = Column(String)


	registrations_needs_socks_default_value = Column(
		Boolean,
		default=False,
	)






