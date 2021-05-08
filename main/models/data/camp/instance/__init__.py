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



class CampInstanceModel(Base, ResourceMixin):

	__tablename__ = 'camp_instances'

	id = Column(Integer, primary_key=True)


	camp_id = Column(Integer, ForeignKey('camps.id'))



	registrations = relationship(
		'CampInstanceRegistrationModel',
		backref='camp_instance',
		lazy='dynamic',
		cascade='all, delete',
	)

	groups = relationship(
		'CampInstanceGroupModel',
		backref='camp_instance',
		lazy='dynamic',
		cascade='all, delete',
	)

	coaches = relationship(
		'CampInstancesCoachesModel',
		back_populates='camp_instance',
		lazy='dynamic',
	)



	year_start = Column(Integer)

	year_end = Column(Integer)


	se_name_snake = Column(String, index=True)

	se_shared_question_id = Column(Integer, index=True)

