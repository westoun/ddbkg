#!/usr/bin/env python3

from dataclasses import dataclass


@dataclass
class ParsingResult:
    text: str
    object_id: str
