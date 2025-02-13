import logging
from typing import Protocol

from design_patterns.src.challenge5.challenge import RequestHandler


class RequestHandlerProtocol(Protocol):
    def handle_request(self, request) -> None: ...


class LoggingDecorator(RequestHandlerProtocol):
    request_handler: RequestHandlerProtocol
    logger: logging.Logger

    def __init__(self, request_handler: RequestHandlerProtocol):
        self.request_handler = request_handler
        self.logger = logging.getLogger(type(request_handler).__name__)

    def handle_request(self, request):
        self.logger.info(f"Handling request: {request}")

        return self.request_handler.handle_request(request)


class AuthDecorator(RequestHandlerProtocol):
    request_handler: RequestHandlerProtocol

    def __init__(self, request_handler: RequestHandlerProtocol):
        self.request_handler = request_handler

    def handle_request(self, request):
        # Do some auth checking here, if not authenticated, raise error

        return self.request_handler.handle_request(request)


if __name__ == "__main__":
    request_handler = RequestHandler()
    authenticated_request_handler = AuthDecorator(request_handler)
    logging_request_handler = LoggingDecorator(authenticated_request_handler)