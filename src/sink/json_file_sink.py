#!/usr/bin/env python3

import json
from multiprocessing import Queue

from src.types_ import ParsingResult
from .interface import Sink


class JsonFileSink(Sink):
    in_queue: "Queue[ParsingResult]"
    target_dir: str

    def __init__(self, in_queue: "Queue[ParsingResult]", target_dir: str = "tmp") -> None:
        # TODO: create dir if not exists
        self.target_dir = target_dir
        self.in_queue = in_queue

    def run(self) -> None:
        while True:
            parsing_result: ParsingResult = self.in_queue.get()

            if parsing_result is None:
                self.in_queue.put(None)  # Alert other workers
                break

            file_path = f"{self.target_dir}/{parsing_result.object_id}.json"
            with open(file_path, "w") as target_file:
                json.dump(parsing_result.content, target_file, indent=4)
