from typing import Any

from sqlalchemy.ext.declarative import (
	as_declarative,
	declared_attr,
)


from sqlalchemy import inspect



@as_declarative()
class Base:
	id: Any
	__name__: str


	# --
	def as_dict(self) -> dict:
		return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}




