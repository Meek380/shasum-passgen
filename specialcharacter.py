import os
import random
import argparse

parser = argparse.ArgumentParser(
                    prog='add_specialchar',
                    description='add special characters with ease'
                    )
parser.add_argument("filename")
parser.add_argument("-c", "--count", default=3, required=True, help="count of special characters to add (default: 3)", dest='count')
parser.add_argument("-v", "--verbose", help="be verbose", action="store_true")

args = parser.parse_args()
verbose = args.verbose


def add_specialchar(file_path):
    with open(file_path, "r+") as file:
        # Get the size of the file
        print("Getting file size...", end=' ')
        file.seek(0, os.SEEK_END)
        file_size = file.tell()
        print(f"DONE: {file_size} bytes\n")

        count = args.count

        for _pass in range(1, int(count) + 1):
            print(f"Pass {_pass}/{count}", end='\n' if verbose else '\r')
            # Generate a random offset within the file
            if verbose: print("Generating random offset...", end=' ')
            offset = random.randint(0, file_size - 1)
            if verbose: print(f"DONE: {offset}")

            # Get the byte at the chosen offset
            file.seek(offset)
            old_str = file.read(1)
            if verbose: print(f"Byte at offset {offset}: {old_str}")

            # Generate a random byte
            if verbose: print("Generating random byte...", end=' ')
            new_str = random.choice(["!", "@", "#", "$", "%", "A", "&", "P", "Z", "D", "?", "M", "~", "Q", "I", "L"])
            if verbose: print(f"DONE: {new_str}")

            # Overwrite the byte at the chosen offset
            if verbose: print(f"Overwriting" + old_str + "with" + {new_str} + "...", end=' ')
            file.seek(offset)
            file.write(new_str)
            if verbose: print("DONE")

    print("\nFile corrupted successfully.")

if __name__ == "__main__":
  add_specialchar(args.filename)
