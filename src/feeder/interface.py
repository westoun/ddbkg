#!/usr/bin/env python3

from abc import abstractmethod, abstractproperty, ABC
from multiprocessing import Queue
from typing import Any


class Feeder(ABC):
    out_queue: "Queue[Any]"

    @abstractmethod
    def __init__(self, out_queue: "Queue[Any]") -> None: ...

    @abstractmethod
    def run(self) -> None: ...
