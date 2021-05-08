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



class TeamInstanceRegistrationModel(
	Base,
	ResourceMixin,
	SpngRegistrationBase,
	SpngRegistrationFinancialsBase,
	PlayerRegistrationBase,
):

	__tablename__ = 'team_instance_registrations'

	id = Column(Integer, primary_key=True)


	# team_instance ...
	team_instance_id = Column(Integer, ForeignKey('team_instances.id'))


# staging -- pgweb -- .

# pg-web could be -- .