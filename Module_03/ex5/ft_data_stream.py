#!/usr/bin/env python3
import random
from typing import Generator


PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = ["run", "jump", "move", "sleep", "eat", "grab",
           "release", "climb", "swim", "use"]


def gen_event() -> Generator:
    while True:
        name = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (name, action)


def consume_event(events: list) -> Generator:
    while len(events) > 0:
        idx = random.randint(0, len(events) - 1)
        event = events[idx]
        events.pop(idx)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")
    stream = gen_event()
    i = 0
    while i < 1000:
        name, action = next(stream)
        print(f"Event {i}: Player {name} did action {action}")
        i += 1
    event_list: list = []
    stream2 = gen_event()
    i = 0
    while i < 10:
        event_list.append(next(stream2))
        i += 1
    print(f"Built list of 10 events: {event_list}")
    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()