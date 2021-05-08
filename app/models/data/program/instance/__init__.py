from sqlalchemy import (
	Boolean,
	Column,
	ForeignKey,
	Integer,
	String,
	Date,
)

from sqlalchemy.orm import relationship

from app.database.base_class import Base

from lib.util_sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)



class ProgramInstanceModel(Base, ResourceMixin):

	__tablename__ = 'program_instances'

	id = Column(Integer, primary_key=True)


	program_id = Column(Integer, ForeignKey('programs.id'))



	registrations = relationship(
		'ProgramInstanceRegistrationModel',
		backref='program_instance',
		lazy='dynamic',
		cascade='all, delete',
	)

	groups = relationship(
		'ProgramInstanceGroupModel',
		backref='program_instance',
		lazy='dynamic',
		cascade='all, delete',
	)

	coaches = relationship(
		'ProgramInstancesCoachesModel',
		back_populates='program_instance',
		lazy='dynamic',
	)



	year_start = Column(Integer)

	year_end = Column(Integer)


	se_name_snake = Column(String, index=True)

	se_shared_question_id = Column(Integer, index=True)


