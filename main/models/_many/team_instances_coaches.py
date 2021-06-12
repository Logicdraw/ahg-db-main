from sqlalchemy import (
	Boolean,
	Column,
	ForeignKey,
	Integer,
	String,
	Text,
	Enum,
)

from sqlalchemy.orm import relationship

from main.database.base_class import Base

from lib.util_sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)


from collections import OrderedDict



class TeamInstancesCoachesModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'team_instances_coaches'
	
	team_instance_id = Column(
		Integer,
		ForeignKey('team_instances.id'),
		primary_key=True,
	)
	coach_id = Column(
		Integer,
		ForeignKey('coaches.id'),
		primary_key=True,
	)


	role = Column(String)


	team_instance = relationship(
		'TeamInstanceModel',
		back_populates='coaches',
		uselist=False,
	)

	coach = relationship(
		'CoachModel',
		back_populates='team_instances',
		uselist=False,
	)


