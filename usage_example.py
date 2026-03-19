from pathutils import File
from typing import Generator

def get_content() -> Generator[bytes, None, None]:
    for _ in range(50):
        yield b"Hello, World!\n"

def main() -> None:
    try:
        file = File("file.txt", True)

        total = file.write_bytes_chunks(
            lambda: get_content()
        )

        print(f"Successfully written {total} bytes to {file.path}")
    except (OSError, ValueError) as exc:
        print(f"An error occurred while writing to file.\nErr: {exc}")

if __name__ == "__main__":
    main()