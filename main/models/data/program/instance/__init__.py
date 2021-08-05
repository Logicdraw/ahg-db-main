from sqlalchemy import (
	Boolean,
	Column,
	ForeignKey,
	Integer,
	String,
	Date,
)

from sqlalchemy.orm import relationship

from main.database.base_class import Base

from main.utils.sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)



class ProgramInstanceModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'program_instances'


	id = Column(
		Integer,
		primary_key=True,
	)



	programs_sc = relationship(
		'ProgramModel',
		back_populates='program_instances',
	)

	program_id = Column(
		Integer,
		ForeignKey('programs.id'),
	)



	program_instances_program_instance_registrations = relationship(
		'ProgramInstancesProgramInstanceRegistrationsModel',
		back_populates='program_instances_sc',
		lazy='selectin',
	)



	program_group_instances = relationship(
		'ProgramGroupInstanceModel',
		back_populates='program_instances_sc',
		lazy='selectin',
		cascade='delete',
	)

	program_instances_coaches = relationship(
		'ProgramInstancesCoachesModel',
		back_populates='program_instances_sc',
		lazy='selectin',
	)


	# program_instance_registration_invites = relationship(
	# 	'ProgramInstanceRegistrationInviteModel',
	# 	back_populates='program_instances_sc',
	# 	lazy='selectin',
	# )



	year_start = Column(
		Integer,
	)

	year_end = Column(
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


	__mapper_args__ = {
		'eager_defaults': True,
	}

	
