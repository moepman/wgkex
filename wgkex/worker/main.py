#!/usr/bin/env python3
import os
import sys

import pika


def callback(ch, method, properties, body):
    print(f"Received message: {body}")


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.queue_declare(queue="wgkex")

    channel.basic_consume(queue="wgkex", auto_ack=True, on_message_callback=callback)

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
