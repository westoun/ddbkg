#!/usr/bin/env python3

from abc import abstractmethod, abstractproperty, ABC
from multiprocessing import Queue
from typing import Any

from src.types_ import XmlObject, ParsingResult


class Processor(ABC):
    in_queue: "Queue[XmlObject]"
    out_queue: "Queue[ParsingResult]"

    @abstractmethod
    def __init__(
        self, in_queue: "Queue[XmlObject]", out_queue: "Queue[ParsingResult]"
    ) -> None: ...

    @abstractmethod
    def run(self) -> None: ...
