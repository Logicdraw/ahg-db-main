from sqlalchemy import (
	Boolean,
	Column,
	ForeignKey,
	Integer,
	String,
	Float,
)

from sqlalchemy.orm import relationship

from main.database.base_class import Base

from lib.util_sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)



class TeamInstanceTracksuitOrderModel(Base, ResourceMixin):

	__tablename__ = 'team_instance_tracksuit_orders'

	id = Column(Integer, primary_key=True)


