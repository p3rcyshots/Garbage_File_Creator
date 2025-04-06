import sys
import signal
import time

def create_garbage_file(size_mb):
    filename = f"garbage_{size_mb}MB.txt"
    try:
        chunk_size = 1 * 1024 * 1024  # Write 1 MB at a time
        total_chunks = size_mb
        start_time = time.time()

        with open(filename, "wb") as file:
            for chunk in range(total_chunks):
                file.write(b"\0" * chunk_size)
                # Calculate progress percentage
                progress = ((chunk + 1) / total_chunks) * 100
                print(f"Progress: {progress:.2f}% complete", end="\r")

        end_time = time.time()
        print(f"\n{filename} created with size {size_mb}MB in {end_time - start_time:.2f} seconds.")
    except Exception as e:
        print(f"Error while creating the file: {e}")

def handle_interrupt(signal, frame):
    print("\nProcess interrupted with Ctrl+C. Exiting gracefully.")
    sys.exit(0)

if __name__ == "__main__":
    # Handle Ctrl+C
    signal.signal(signal.SIGINT, handle_interrupt)

    if len(sys.argv) != 3 or sys.argv[1] != "-s":
        print("Usage: python script.py -s <size_in_MB>")
        sys.exit(1)

    try:
        size_mb = int(sys.argv[2].replace("MB", ""))
        if size_mb <= 0:
            raise ValueError("Size must be greater than 0.")
        create_garbage_file(size_mb)
    except ValueError:
        print("Invalid size. Please enter a positive number in megabytes (e.g., 1, 1000).")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")