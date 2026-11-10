from pydantic import BaseModel


class Envelope[T](BaseModel):
    status: str | None = None
    data: T
