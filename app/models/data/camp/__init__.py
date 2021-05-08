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



class CampModel(Base, ResourceMixin):

	__tablename__ = 'camps'

	id = Column(Integer, primary_key=True)


	name = Column(String)


	instances = relationship('CampInstanceModel', backref='camp', lazy='dynamic', cascade='all, delete')

	groups = relationship('CampGroupModel', backref='camp', lazy='dynamic', cascade='all, delete')

