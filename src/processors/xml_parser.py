#!/usr/bin/env python3

from multiprocessing import Queue
from typing import Any

from .interface import Processor
from src.types_ import XmlObject, ParsingResult


class XmlParser(Processor):
    in_queue: Queue[XmlObject]
    out_queue: Queue[ParsingResult]

    def __init__(
        self, in_queue: Queue[XmlObject], out_queue: Queue[ParsingResult]
    ) -> None:
        self.in_queue = in_queue
        self.out_queue = out_queue
