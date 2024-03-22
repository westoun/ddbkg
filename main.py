#!/usr/bin/env python3

from multiprocessing import Queue, Process
from typing import List

from src.feeder import Feeder, LinkFeeder, Sqlite3Feeder
from src.processors import Processor, XmlParser
from src.sink import Sink, JsonFileSink, PrintSink, JsonlFileSink
from src.types_ import ParsingResult, XmlObject


def main():

    xml_object_queue: Queue[XmlObject] = Queue(1000)
    result_queue: Queue[ParsingResult] = Queue(1000)

    # sqlite3_feeder: Feeder = Sqlite3Feeder(
    #     out_queue=xml_object_queue, db_path="sector2.sqlite3"
    # )
    link_feeder: Feeder = LinkFeeder(
        links=[
            "http://deutsche-digitale-bibliothek.de/item/xml/SXWUDEQ3XNNHGZAIBUEEVH43ONU7TKOH",
            "http://deutsche-digitale-bibliothek.de/item/xml/SXWUDEQ3XNNHGZAIBUEEVH43ONU7TKOH",
        ],
        out_queue=xml_object_queue,
    )
    parser: Processor = XmlParser(in_queue=xml_object_queue, out_queue=result_queue)
    sink: Sink = JsonlFileSink(in_queue=result_queue, target_dir="tmp", batch_size=10)
    # sink: Sink = PrintSink(in_queue=result_queue)

    workers: List[Process] = []

    # Allocate workers based on which process step is the
    # bottleneck and how many resources are available.
    for _ in range(1):
        worker = Process(target=parser.run, daemon=True, args=())
        worker.start()
        workers.append(worker)

    for _ in range(1):
        worker = Process(target=sink.run, daemon=True, args=())
        worker.start()
        workers.append(worker)

    # To avoid race conditions if one feeder process finishes before the
    # other, run feeder only in a single process.
    link_feeder.run()

    for worker in workers:
        worker.join()


if __name__ == "__main__":
    main()
