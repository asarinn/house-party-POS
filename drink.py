from dataclasses import dataclass
from PIL.ImageQt import ImageQt


@dataclass
class Drink:
    id: int
    name: str
    description: str
    price: float
    photo: ImageQt
