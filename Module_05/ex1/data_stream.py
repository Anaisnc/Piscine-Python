#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any
import typing


class DataProcessor(ABC):

    def __init__(self):
        self._storage: list[str] = []
        self._rank: int = 0
        self._total: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        self._rank += 1
        return (self._rank, self._storage.pop(0))

    def remaining(self) -> int:
        return len(self._storage)

    def total(self) -> int:
        return self._total


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list) and all(
            isinstance(x, (int, float)) for x in data
        ):
            return True
        return False

    def ingest(self, data: int | float | list) -> None:
        if not self.validate(data):
            raise TypeError(f"NumericProcessor: invalid data: {type(data)}")
        if isinstance(data, list):
            for item in data:
                self._storage.append(str(item))
                self._total += 1
        else:
            self._storage.append(str(data))
            self._total += 1


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list) and all(isinstance(x, str) for x in data):
            return True
        return False

    def ingest(self, data: str | list) -> None:
        if not self.validate(data):
            raise TypeError(f"TextProcessor: invalid data: {type(data)}")
        if isinstance(data, list):
            for item in data:
                self._storage.append(item)
                self._total += 1
        else:
            self._storage.append(data)
            self._total += 1


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict) and all(
            isinstance(k, str) and isinstance(v, str)
            for k, v in data.items()
        ):
            return True
        if isinstance(data, list) and all(
            isinstance(d, dict) and all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in d.items()
            )
            for d in data
        ):
            return True
        return False

    def ingest(self, data: dict | list) -> None:
        if not self.validate(data):
            raise TypeError(f"LogProcessor: invalid data: {type(data)}")
        if isinstance(data, list):
            for item in data:
                self._storage.append(str(item))
                self._total += 1
        else:
            self._storage.append(str(data))
            self._total += 1


class DataStream:

    def __init__(self):
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            handled = False
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    handled = True
                    break
            if not handled:
                print(
                    f"DataStream error - Can't process element in stream:"
                    f" {element}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            name = type(proc).__name__
            print(
                f"{name}: total {proc.total()} items processed,"
                f" remaining {proc.remaining()} on processor"
            )


def main() -> None:
    print("=== Code Nexus - Data Stream ===")
    print("Initialize Data Stream...")

    stream = DataStream()
    stream.print_processors_stats()

    print("Registering Numeric Processor")
    stream.register_processor(NumericProcessor())

    batch: list[typing.Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING", "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]

    print(f"Send first batch of data on stream: {batch}")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("Registering other data processors")
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    print("Send the same batch again")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("Consume some elements from the data processors: Numeric 3, Text 2, Log 1")
    processors = stream._processors
    for _ in range(3):
        processors[0].output()
    for _ in range(2):
        processors[1].output()
    processors[2].output()

    stream.print_processors_stats()


if __name__ == "__main__":
    main()
