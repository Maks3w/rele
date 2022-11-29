import logging

from google.cloud.pubsub_v1.subscriber.message import Message

from rele.contrib.unrecoverable_middleware import UnrecoverableException
from rele.middleware import BaseMiddleware

logger = logging.getLogger(__name__)


class RetryMiddleWare(BaseMiddleware):
    def post_process_message_failure(
        self, subscription, err, start_time, message: Message
    ):
        if isinstance(err, UnrecoverableException):
            return
        # Release message from Lease manager (ACK deadline is not increased any more)
        # Eventually ACK expired
        message.modify_ack_deadline(20)
        message.drop()
