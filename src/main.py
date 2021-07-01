from clients.prepayment_client import PrepaymentClient
from clients.tag_client import TagClient
from consumer.rabbitmq_consumer import RabbitMQConsumer
from service_layer.process import process_message


def main():
    _ = TagClient()
    _ = PrepaymentClient()
    consumer = RabbitMQConsumer()

    consumer.consume(process_message)
    print("consuming")


if __name__ == "__main__":
    main()
