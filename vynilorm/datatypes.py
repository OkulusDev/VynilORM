
class BaseType:
	field_type: str #название типа данных поля, например, "INTEGER"

	def __init__(self, unique: bool = False, null: bool = True, default: int = None):
		self.unique = unique
		self.null = null
		self.default = default


def json(self):
	attributes = {}
	for key, value in vars(self).items():
		if not key.startswith("__") and not callable(value):#проверка на системные методы и поля
			attributes[key] = value

	return attributes


class IntegerField(BaseType):
	field_type = 'INTEGER'


class TextField(BaseType):
	field_type = 'TEXT'


class BlobField(BaseType):
	field_type = 'BLOB'


class RealField(BaseType):
	field_type = 'REAL'


class NumericField(BaseType):
	field_type = 'NUMERIC'
