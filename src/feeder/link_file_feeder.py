#!/usr/bin/env python3

from multiprocessing import Queue
import requests
from typing import Any, List

from .interface import Feeder
from src.types_ import XmlObject


class LinkFileFeeder(Feeder):
    """Fetch xml objects as text from a file that contains links
    separated by new line.."""

    out_queue: "Queue[XmlObject]"
    links: List[str]

    def __init__(self, path: str, out_queue: "Queue[XmlObject]") -> None:
        self.links = self.load_links(path)
        self.out_queue = out_queue

    def load_links(self, path: str) -> List[str]:
        with open(path) as link_file:
            links = [line.strip() for line in link_file]
            return links

    def run(self) -> None:
        for link in self.links:
            response = requests.get(link)

            object_id = link.split("/")[-1]
            xml = response.text

            xml_object = XmlObject(text=xml, object_id=object_id)

            self.out_queue.put(xml_object)

        self.out_queue.put(None)
