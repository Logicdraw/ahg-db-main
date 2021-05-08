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



class ProgramGroupModel(Base, ResourceMixin):

	__tablename__ = 'program_groups'

	id = Column(Integer, primary_key=True)


	name = Column(String)


	camp_id = Column(Integer, ForeignKey('camps.id'))


	instances = relationship('ProgramInstanceGroupModel', backref='program_group', lazy='dynamic', cascade='all, delete')



