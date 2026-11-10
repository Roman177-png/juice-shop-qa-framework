from pydantic import BaseModel, ConfigDict, Field


class Product(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int
    name: str
    description: str
    price: float
    deluxe_price: float | None = Field(default=None, alias="deluxePrice")
    image: str | None = None
    category: str | None = None
