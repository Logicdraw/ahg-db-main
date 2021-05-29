import pytest


from typing import (
	Dict,
	Generator,
)


# from fastapi.testclient import TestClient


# from main.config import settings


# from main.database.testing.helpers import (
# 	init_testing_db,
# 	reset_testing_db,
# 	# drop_testing_db,
# 	create_testing_db_data,
# )


# from main.database.testing import (
# 	SessionTesting,
# )


# from main.main import app


# from main.api.deps import get_db




# def get_testing_db() -> Generator:
# 	try:
# 		db = SessionTesting()
# 		yield db
# 	finally:
# 		db.close()




# @pytest.fixture(scope="session")
# def db() -> Generator:
# 	try:
# 		db = SessionTesting()

# 		# "Reset" db -- every session!

# 		reset_testing_db(db=db)
# 		create_testing_db_data(db=db)

# 		yield db
# 	finally:
# 		db.close()








# # ...




