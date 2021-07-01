from typing import Callable

from pydantic import BaseModel


class Message(BaseModel):
    id: int


class RabbitMQConsumer:
    def consume(self, func: Callable):
        pass
