from sqlalchemy import (
	Boolean,
	Column,
	ForeignKey,
	Integer,
	String,
	Float,
)

from sqlalchemy.orm import relationship

from app.database.base_class import Base

from lib.util_sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)


from app.models._base.registration import (
	SpngRegistrationBase,
	SpngRegistrationFinancialsBase,
	PlayerRegistrationBase,
)


class CampInstanceRegistrationModel(
	Base,
	ResourceMixin,
	SpngRegistrationBase,
	SpngRegistrationFinancialsBase,
	PlayerRegistrationBase,
):

	__tablename__ = 'camp_instance_registrations'

	id = Column(Integer, primary_key=True)


	camp_instance_id = Column(Integer, ForeignKey('camp_instances.id'))


	camp_instance_group = relationship('CampInstanceGroupModel', uselist=False)
	camp_instance_group_id = Column(Integer, ForeignKey('camp_instance_groups.id'))



	# other information

