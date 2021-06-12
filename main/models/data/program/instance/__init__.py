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

from lib.util_sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)



class ProgramInstanceModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'program_instances'

	id = Column(Integer, primary_key=True)



	program = relationship(
		'ProgramModel',
		back_populates='instances',
		uselist=False,
	)
	program_id = Column(Integer, ForeignKey('programs.id'))



	registrations = relationship(
		'ProgramInstanceRegistrationModel',
		back_populates='program_instance',
		lazy='selectin',
	)

	groups = relationship(
		'ProgramGroupInstanceModel',
		back_populates='program_instance',
		lazy='selectin',
		cascade='delete',
	)

	coaches = relationship(
		'ProgramInstancesCoachesModel',
		back_populates='program_instance',
		lazy='selectin',
	)



	year_start = Column(Integer)

	year_end = Column(Integer)



	# SportsEngine --

	se_name_snake = Column(String, index=True)

	se_shared_question_id = Column(Integer, index=True)


