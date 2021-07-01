from consumer.rabbitmq_consumer import Message


def process_message(message: Message):
    return message.id >= 10
