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



class ProgramGroupModel(Base, ResourceMixin):

	__tablename__ = 'program_groups'

	id = Column(Integer, primary_key=True)


	name = Column(String)


	program = relationship(
		'ProgramModel',
		back_populates='groups',
		uselist=False,
	)
	program_id = Column(Integer, ForeignKey('programs.id'))


	instances = relationship(
		'ProgramGroupInstanceModel',
		back_populates='program_group',
		lazy='selectin',
		cascade='delete',
	)



