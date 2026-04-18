#!/usr/bin/env python3


import sys
import typing


def print_error(msg: str) -> None:
    sys.stderr.write(f"[STDERR] {msg}\n")
    sys.stderr.flush()


def read_file(filename: str) -> str:
    print(f"Accessing file '{filename}'")
    file: typing.IO
    try:
        file = open(filename, "r")
    except OSError as e:
        print_error(f"Error opening file '{filename}': {e}")
        return ""

    content: str = file.read()
    file.close()
    print("---")
    print(content, end="")
    print("---")
    print(f"File '{filename}' closed.")
    return content


def transform(content: str) -> str:
    lines = content.splitlines()
    return "\n".join(line + "#" for line in lines) + "\n"


def save_file(filename: str, content: str) -> None:
    print(f"Saving data to '{filename}'")
    file: typing.IO
    try:
        file = open(filename, "w")
    except OSError as e:
        print_error(f"Error opening file '{filename}': {e}")
        print("Data not saved.")
        return
    file.write(content)
    file.close()
    print(f"Data saved in file '{filename}'.")


def get_input(prompt: str) -> str:
    sys.stdout.write(prompt)
    sys.stdout.flush()
    return sys.stdin.readline().rstrip("\n")


def main() -> None:
    if len(sys.argv) != 2:
        sys.stderr.write(f"Usage: {sys.argv[0]} <file>\n")
        return

    print("=== Cyber Archives Recovery & Preservation ===")
    content: str = read_file(sys.argv[1])
    if not content:
        return

    new_content: str = transform(content)
    print("\nTransform data:")
    print("---")
    print(new_content, end="")
    print("---")

    dest: str = get_input("Enter new file name (or empty): ")
    if not dest:
        print("Not saving data.")
        return
    save_file(dest, new_content)


if __name__ == "__main__":
    main()