#!/usr/bin/env python3

from abc import abstractmethod, abstractproperty, ABC
from multiprocessing import Queue
from typing import Any


class Processor(ABC):
    in_queue: "Queue[Any]"
    out_queue: "Queue[Any]"

    @abstractmethod
    def __init__(self, in_queue: "Queue[Any]", out_queue: "Queue[Any]") -> None: ...

    @abstractmethod
    def run(self) -> None: ...
