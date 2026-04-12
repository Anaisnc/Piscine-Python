#!/usr/bin/env python3
import sys


def parse_args(args: list[str]) -> list[int]:
    scores: list[int] = []
    i = 1
    while i < len(args):
        try:
            scores.append(int(args[i]))
        except ValueError:
            print(f"Invalid parameter: '{args[i]}'")
        i += 1
    return scores


def display_stats(scores: list[int]) -> None:
    total = sum(scores)
    average = total / len(scores)
    high = max(scores)
    low = min(scores)
    score_range = high - low
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {total}")
    print(f"Average score: {average}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {score_range}")


def main() -> None:
    print("=== Player Score Analytics ===")
    scores = parse_args(sys.argv)
    if len(scores) == 0:
        usage = "python3 ft_score_analytics.py <score1> <score2> ..."
        print(f"No scores provided. Usage: {usage}")
        return
    display_stats(scores)


if __name__ == "__main__":
    main()
