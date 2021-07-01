import pytest

from src.consumer.rabbitmq_consumer import Message
from src.service_layer.process import process_message


@pytest.fixture
def build_message_with_id():
    def _build_message_with_id(message_id: int) -> Message:
        return Message(id=message_id)

    return _build_message_with_id


def test_process_message_when_id_lesser_than_10(build_message_with_id):
    assert process_message(build_message_with_id(3)) is False


def test_process_message_when_id_greater_than_10(build_message_with_id):
    assert process_message(build_message_with_id(11)) is True
