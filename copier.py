import sys
import pathlib
import hashlib
import shutil
import time
from datetime import datetime


def log_message(message, log_path):
    """
    Function for logging messages to console and log file with timestamp.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"[{timestamp}] {message}"
    print(message)
    with open(log_path, "a") as log_file:
        log_file.write(message + "\n")


def calculate_md5(file_path):
    """
    Function for calculating MD5 from:
    https://www.geeksforgeeks.org/python/finding-md5-of-files-recursively-in-directory-in-python/
    """
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as file:
        for piece in iter(lambda: file.read(4096), b""):
            hash_md5.update(piece)
    return hash_md5.hexdigest()


def sync_folders(source, replica, log_path):
    """
    Function to synchronize source folder to replica folder.
    """
    # Source to Replica
    for item in source.rglob("*"):
        relative_path = item.relative_to(source)
        replica_item = replica / relative_path

        if item.is_dir():
            if not replica_item.exists():
                replica_item.mkdir(parents=True)
                log_message(f"Directory for Replica created: {replica_item}", log_path)
        else:
            if not replica_item.exists() or calculate_md5(item) != calculate_md5(
                replica_item
            ):
                shutil.copy2(item, replica_item)
                log_message(f"File copied or updated: {replica_item}", log_path)

    # Check Replica for 'extra' files
    for item in replica.rglob("*"):
        relative_path = item.relative_to(replica)
        source_item = source / relative_path

        if not source_item.exists():
            if not item.exists():
                continue
            if item.is_dir():
                shutil.rmtree(item)
                log_message(f"Directory deleted from Replica: {item}", log_path)
            else:
                item.unlink()
                log_message(f"File deleted from Replica: {item}", log_path)


def read_arguments():
    """
    Check the command line arguments and return them if the number and types are correct.
    """
    if len(sys.argv) != 6:
        print(
            "Check the arguments: "
            "path source, "
            "path destination, "
            "interval between sincronization"
            "amount of sincroznizations"
            "path to log file"
        )
        return None

    try:
        source_path = pathlib.Path(sys.argv[1])
        replica_path = pathlib.Path(sys.argv[2])
        interval = int(sys.argv[3])
        amount = int(sys.argv[4])
        log_file_path = pathlib.Path(sys.argv[5])

        return source_path, replica_path, interval, amount, log_file_path
    except ValueError as e:
        print(f"Error in arguments: {e}")
        return None


def main():
    args = read_arguments()
    if args is None:
        return

    source_path, replica_path, interval, amount, log_file_path = args

    # Check the args
    print(
        f"Source: {source_path}, Replica: {replica_path}, Interval: {interval}, Amount: {amount}, Log file: {log_file_path}"
    )

    if not source_path.exists():
        print(f"Source path does not exist: {source_path}")
        return

    if not replica_path.exists():
        try:
            replica_path.mkdir(parents=True, exist_ok=True)
            log_message(f"Created replica directory: {replica_path}", log_file_path)
        except OSError as e:
            log_message(f"Error creating replica directory: {e}", log_file_path)
            return

    while amount > 0:
        sync_folders(source_path, replica_path, log_file_path)
        amount -= 1
        if amount > 0:
            time.sleep(interval)


if __name__ == "__main__":
    main()
