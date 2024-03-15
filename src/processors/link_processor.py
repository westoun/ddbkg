#!/usr/bin/env python3

from multiprocessing import Queue
from typing import List

from src.types_ import XmlObject
from .interface import Processor


class LinkProcessor(Processor):
    in_queue: Queue[str]
    out_queue: Queue[XmlObject]

    def __init__(self, in_queue: Queue[str], out_queue: Queue[XmlObject]) -> None:
        self.in_queue = in_queue
        self.out_queue = out_queue

    def run(self) -> None:
        raise NotImplementedError()

    # def run(self) -> None:
    #     # for link in self.links:
    #     #     text = self.process(link)
    #     #     object_id = link.split("/")[-1]

    #     #     xml_object = XmlObject(text=text, id=object_id)

    #     #     self.queue.put(xml_object)
    #     pass

    # def process(self, link: str) -> str:
    #     pass
