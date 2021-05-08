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


	team_id = Column(Integer, ForeignKey('teams.id'))


	division_instance_id = Column(Integer, ForeignKey('division_instances.id'))

	conference_instance_id = Column(Integer, ForeignKey('conference_instances.id'))

	league_instance_id = Column(Integer, ForeignKey('league_instances.id'))

	season_instance_id = Column(Integer, ForeignKey('season_instances.id'))



	registrations = relationship('TeamInstanceRegistrationModel', backref='team_instance', lazy='dynamic', cascade='all, delete')


	players = relationship('TeamInstancesPlayersModel', back_populates='team_instance', lazy='dynamic')

	coaches = relationship('TeamInstancesCoachesModel', back_populates='team_instance', lazy='dynamic')


	jersey_socks_orders = relationship('TeamInstanceJerseySocksOrderModel', backref='team_instance', lazy='dynamic', cascade='all, delete')

	tracksuit_orders = relationship('TeamInstanceTracksuitOrderModel', backref='team_instance', lazy='dynamic', cascade='all, delete')



	year_start = Column(Integer)

	year_end = Column(Integer)
	
	
	birth_year = Column(Integer)



	se_name_snake = Column(String, index=True)

	se_shared_question_id = Column(Integer, index=True)


	gs_team_id = Column(Integer)



	number_of_tracksuits_available = Column(Integer)



	jersey_numbers_options = Column(String)


	has_jersey_size_option = Column(Boolean, default=False)

	jersey_sizes_options = Column(String)



	has_socks_size_option = Column(Boolean, default=False)

	socks_sizes_options = Column(String)




