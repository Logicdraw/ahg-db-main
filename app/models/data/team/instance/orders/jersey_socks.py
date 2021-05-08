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



class TeamInstanceJerseySocksOrderModel(Base, ResourceMixin):

	__tablename__ = 'team_instance_jersey_socks_orders'

	id = Column(Integer, primary_key=True)


