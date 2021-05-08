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
	PlayerRegistrationBase,
	SpngRegistrationBase,
	SpngRegistrationFinancialsBase,
)



class ProgramInstanceRegistrationModel(
	Base,
	ResourceMixin,
	SpngRegistrationBase,
	SpngRegistrationFinancialsBase,
	PlayerRegistrationBase,
):

	__tablename__ = 'program_instance_registrations'

	id = Column(Integer, primary_key=True)


	program_instance_id = Column(Integer, ForeignKey('program_instances.id'))
	

	program_instance_group = relationship('ProgramInstanceGroupModel', uselist=False)
	program_instance_group_id = Column(Integer, ForeignKey('program_instance_groups.id'))





