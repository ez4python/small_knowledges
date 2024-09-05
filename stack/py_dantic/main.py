import json
from datetime import date

from pydantic import BaseModel, ValidationError


class Supervisor(BaseModel):
    id: int
    first_name: str
    last_name: str


class Student(BaseModel):
    id: int
    first_name: str
    last_name: str
    birthdate: date = None
    type: str
    supervisor: Supervisor


input_data = """
{
    "id": 123,
    "first_name": "Akbarali",
    "last_name": "Salohiddinov",
    "birthdate": "2003-09-14",
    "type": "male",
    "supervisor": {
        "id": 7,
        "first_name": Ziyoda,
        "last_name": Adilova
    }
}
"""


def printable():
    try:
        student = Student.parse_raw(input_data)
        return student
    except ValidationError as e:
        return json.dumps(json.loads(e.json()), indent=3)


print(printable())
