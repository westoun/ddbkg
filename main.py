#!/usr/bin/env python3

from multiprocessing import Queue, Process
from typing import List

from src.feeder import Feeder, LinkFeeder
from src.processors import Processor, LinkProcessor, XmlParser
from src.sink import Sink, JsonFileSink, PrintSink
from src.types_ import ParsingResult, XmlObject


def main():

    link_queue: Queue[str] = Queue(1000)
    xml_object_queue: Queue[XmlObject] = Queue(1000)
    result_queue: Queue[ParsingResult] = Queue(1000)

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
    # sink: Sink = JsonFileSink(in_queue=result_queue)
    sink: Sink = PrintSink(in_queue=result_queue)

    # allocate workers based on which process step is the
    # bottleneck and how many resources are available.

    workers: List[Process] = []

    for _ in range(1):
        worker = Process(target=link_processor.run, daemon=True, args=())
        worker.start()
        workers.append(worker)

    for _ in range(1):
        worker = Process(target=parser.run, daemon=True, args=())
        worker.start()
        workers.append(worker)

    for _ in range(1):
        worker = Process(target=sink.run, daemon=True, args=())
        worker.start()
        workers.append(worker)

    # Since link feeder is lightweight, no need for
    # multiprocessing here...
    link_feeder.run()

    for worker in workers:
        worker.join()


if __name__ == "__main__":
    main()
