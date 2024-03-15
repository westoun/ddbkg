#!/usr/bin/env python3

from multiprocessing import Queue

from src.types_ import ParsingResult
from .interface import Sink


class JsonFileSink(Sink):
    in_queue: Queue[ParsingResult]

    def __init__(self, in_queue: Queue[ParsingResult]) -> None:
        self.in_queue = in_queue

    def run(self) -> None:
        raise NotImplementedError()
