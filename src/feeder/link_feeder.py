#!/usr/bin/env python3

from multiprocessing import Queue
from typing import Any, List

from .interface import Feeder


class LinkFeeder(Feeder):
    out_queue: Queue[Any]
    links: List[str]

    def __init__(self, links: str, out_queue: Queue) -> None:
        self.links = links
        self.out_queue = out_queue

    def run(self) -> None:
        raise NotImplementedError()
