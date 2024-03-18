#!/usr/bin/env python3

from multiprocessing import Queue
from typing import Any, List

from .interface import Feeder


class LinkFeeder(Feeder):
    out_queue: "Queue[str]"
    links: List[str]

    def __init__(self, links: str, out_queue: "Queue[str]") -> None:
        self.links = links
        self.out_queue = out_queue

    def run(self) -> None:
        for link in self.links:
            self.out_queue.put(link)

        self.out_queue.put(None)
