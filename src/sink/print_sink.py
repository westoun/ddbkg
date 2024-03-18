#!/usr/bin/env python3

import json
from multiprocessing import Queue

from src.types_ import ParsingResult
from .interface import Sink


class PrintSink(Sink):
    in_queue: "Queue[ParsingResult]"

    def __init__(self, in_queue: "Queue[ParsingResult]") -> None:
        self.in_queue = in_queue

    def run(self) -> None:
        while True:
            parsing_result: ParsingResult = self.in_queue.get()

            # TODO: Check if this is best way to detect
            # end of queue.
            if parsing_result is None:
                break

            print(json.dumps(parsing_result.content, indent=4, ensure_ascii=False))
