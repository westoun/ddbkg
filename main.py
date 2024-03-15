#!/usr/bin/env python3

from multiprocessing import Queue

from src.feeder import Feeder, LinkFeeder
from src.processors import Processor, LinkProcessor, XmlParser
from src.sink import Sink, JsonFileSink
from src.types_ import ParsingResult, XmlObject

if __name__ == "__main__":

    link_queue: Queue[str] = Queue()
    xml_object_queue: Queue[XmlObject] = Queue()
    result_queue: Queue[ParsingResult] = Queue()

    link_feeder: Feeder = LinkFeeder(
        links=[
            "http://deutsche-digitale-bibliothek.de/item/xml/SXWUDEQ3XNNHGZAIBUEEVH43ONU7TKOH"
        ],
        out_queue=link_queue,
    )
    link_processor: Processor = LinkProcessor(
        in_queue=link_queue, out_queue=xml_object_queue
    )
    parser: Processor = XmlParser(in_queue=xml_object_queue, out_queue=result_queue)
    sink: Sink = JsonFileSink(in_queue=result_queue)
