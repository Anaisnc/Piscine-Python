from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    def __init__(self):
        self._storage: list[str] = []
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        self._rank += 1
        return (self._rank, self._storage.pop(0))


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list) and all(isinstance
                                          (x, (int, float)) for x in data):
            return True
        return False

    def ingest(self, data: int | float | list) -> None:
        if not self.validate(data):
            raise TypeError(f"NumericProcessor: invalid data: {type(data)}")
        self._storage.append(str(data))


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
        self._storage.append(str(data))


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
        self._storage.append(str(data))

def main() -> None:
    num = NumericProcessor()
    num.ingest(42)
    num.ingest(3.14)
    num.ingest([1, 2, 3])
    print(num.output())
    print(num.output())
    print(num.output())

    txt = TextProcessor()
    txt.ingest("hello")
    txt.ingest(["foo", "bar"])
    print(txt.output())
    print(txt.output())

    log = LogProcessor()
    log.ingest({"level": "INFO", "msg": "started"})
    log.ingest([{"level": "WARNING", "msg": "low memory"}, {"level": "ERROR", "msg": "crash"}])
    print(log.output())
    print(log.output())

    try:
        num.ingest("not a number")
    except TypeError as e:
        print(e)


if __name__ == "__main__":
    main()
