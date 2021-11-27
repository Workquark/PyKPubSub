from uuid import UUID
from restaurants.hours import Hours

class Restaurant:
    id: int
    uid: UUID
    name: str
    type: str
    description: str
    review: str
    logo: str
    phone_number: str
    address: str
    hours: Hours

    def __init__(self, id: int, uid: UUID, name: str, type: str, description: str, review: str, logo: str, phone_number: str, address: str, hours: Hours) -> None:
        self.id = id
        self.uid = uid
        self.name = name
        self.type = type
        self.description = description
        self.review = review
        self.logo = logo
        self.phone_number = phone_number
        self.address = address
        self.hours = hours