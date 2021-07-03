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

from main.utils.sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)


from collections import OrderedDict



class CampInstancesCoachesModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'camp_instances_coaches'


	camp_instance_id = Column(
		Integer,
		ForeignKey('camp_instances.id'),
		primary_key=True,
	)

	coach_id = Column(
		Integer,
		ForeignKey('coaches.id'),
		primary_key=True,
	)



	role = Column(
		String,
	)



	camp_instances_sc = relationship(
		'CampInstanceModel',
		back_populates='camp_instances_coaches',
		uselist=False,
	)

	coaches_sc = relationship(
		'CoachModel',
		back_populates='camp_instances_coaches',
		uselist=False,
	)


	__mapper_args__ = {
		'eager_defaults': True,
	}





