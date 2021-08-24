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

from main.utils.sqlalchemy import (
	AwareDateTime,
	ResourceMixin,
)



class TeamInstanceJerseySponsorOrderUpdateModel(
	Base,
	ResourceMixin,
):

	__tablename__ = 'team_instance_jersey_sponsor_order_updates'

	id = Column(
		Integer,
		primary_key=True,
	)



	team_instance_jersey_sponsor_orders_sc = relationship(
		'TeamInstanceJerseySponsorOrderModel',
		back_populates='team_instance_jersey_sponsor_order_updates',
	)

	team_instance_jersey_sponsor_order_id = Column(
		Integer,
		ForeignKey('team_instance_jersey_sponsor_orders.id')
	)


	old_player_full_name = Column(
		String,
		index=True,
	)

	old_name = Column(
		String,
		index=True,
	)

	old_amount = Column(
		Float,
	)


	new_player_full_name = Column(
		String,
		index=True,
	)

	new_name = Column(
		String,
		index=True,
	)

	new_amount = Column(
		Float,
	)


	__mapper_args__ = {
		'eager_defaults': True,
	}






