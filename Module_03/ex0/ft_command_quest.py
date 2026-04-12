#!/usr/bin/env python3

import sys


def main() -> None:
    program_name: str = sys.argv[0]
    args: list[str] = sys.argv[1:]
    print("=== Command Quest ===")
    print(f"Program name: {program_name}")

    if not args:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(args)}")
        i = 1
        for arg in args:
            print(f"Argument {i}: {arg}")
            i += 1

    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
