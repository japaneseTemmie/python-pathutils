from pathutils import Folder
from os.path import join, abspath
from typing import Generator

def write_bytes_chunks_example() -> None:
    def _get_content() -> Generator[bytes, None, None]:
        for _ in range(50):
            yield b"Hello, World!\n"
    
    try:
        folder = Folder("testFolder", True)
        file = folder.add_file("file.txt")

        total = file.write_bytes_chunks(
            lambda: _get_content()
        )

        print(f"Successfully written {total} bytes to {file.path}")
    except (OSError, ValueError) as exc:
        print(f"An error occurred while writing to file.\nErr: {exc}")

def link_to_example() -> None:
    try:
        folder = Folder("testFolder", True)
        other_folder = folder.make_subfolder("otherTestFolder")
        link = other_folder.link_to(join(folder.path, f"linkto{other_folder.name}"))

        print(f"Linked {folder.path} to {link.path}")
    except (OSError, ValueError) as exc:
        print(f"An error occurred while linking file.\nErr: {exc}")

def copy_to_example() -> None:
    try:
        folder = Folder("testFolder")
        folder.copy_to("testFolder_backup", False)
    except (OSError, ValueError) as exc:
        print(f"An error occurred while coping folder.\nErr: {exc}")
def main() -> None:
    write_bytes_chunks_example()
    link_to_example()
    copy_to_example()

if __name__ == "__main__":
    main()