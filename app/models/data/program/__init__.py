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



class ProgramModel(Base, ResourceMixin):

	__tablename__ = 'programs'

	id = Column(Integer, primary_key=True)


	name = Column(String)


	instances = relationship('ProgramInstanceModel', backref='program', lazy='dynamic', cascade='all, delete')

	groups = relationship('ProgramGroupModel', backref='program', lazy='dynamic', cascade='all, delete')

