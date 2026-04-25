#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any

class DataProcessor(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def validate(self, data):
        isinstance(data, Any)

    @abstractmethod
    def ingest(self, data):
        pass

class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data):
        return isinstance(data, (int, float))

    def ingest(self, data):
        if self.validate(data):
            return data
        else:
            raise ValueError("Invalid data type")

class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data):
        return isinstance(data, str)

    def ingest(self, data):
        if self.validate(data):
            return data
        else:
            raise ValueError("Invalid data type")

class NumericProcessor(LogProcessor):