import random

import string

from typing import Dict


from fastapi.testclient import TestClient

from main.config import settings


from faker import Faker


fake = Faker()


def random_lower_string() -> str:
	return "".join(random.choices(string.ascii_lowercase, k=32))



def random_email() -> str:
	return fake.email()



def random_name() -> str:
	return fake.name()

