#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Protocol
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
                log_level = item.get("log_level", "")
                log_message = item.get("log_message", "")
                self._storage.append(f"{log_level}: {log_message}")
                self._total += 1
        else:
            log_level = data.get("log_level", "")
            log_message = data.get("log_message", "")
            self._storage.append(f"{log_level}: {log_message}")
            self._total += 1


class ExportPlugin(Protocol):

    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:

    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [item for _, item in data]
        print("CSV Output:")
        print(",".join(values))


class JSONExportPlugin:

    def process_output(self, data: list[tuple[int, str]]) -> None:
        pairs = ", ".join(
            f'"item_{rank}": "{value}"' for rank, value in data
        )
        print("JSON Output:")
        print("{" + pairs + "}")


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            collected: list[tuple[int, str]] = []
            count = min(nb, proc.remaining())
            for _ in range(count):
                collected.append(proc.output())
            if collected:
                plugin.process_output(collected)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")

    stream = DataStream()
    stream.print_processors_stats()

    print("Registering Processors")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    batch1: list[typing.Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING", "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]

    print(f"Send first batch of data on stream: {batch1}")
    stream.process_stream(batch1)
    stream.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVExportPlugin())
    stream.print_processors_stats()

    batch2: list[typing.Any] = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {"log_level": "NOTICE", "log_message": "Certificate expires in 10 days"},
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    print(f"Send another batch of data: {batch2}")
    stream.process_stream(batch2)
    stream.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONExportPlugin())
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
