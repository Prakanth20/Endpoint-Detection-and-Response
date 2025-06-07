import os
import time
import hashlib
import json
import psutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

LOG_FILE = "edr_log.json"
WATCH_DIR = os.path.expanduser("~")  # Monitor user's home directory

# --- Utility Functions ---
def hash_file(path):
    try:
        with open(path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except Exception:
        return None

def log_event(event_type, data):
    event = {
        "event_type": event_type,
        "timestamp": time.ctime(),
        "data": data
    }
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(event) + "\n")
    print(f"[{event_type}] {data}")

# --- File Monitor ---
class FileMonitorHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            log_event("file_modified", {"path": event.src_path, "hash": hash_file(event.src_path)})

    def on_created(self, event):
        if not event.is_directory:
            log_event("file_created", {"path": event.src_path, "hash": hash_file(event.src_path)})

    def on_deleted(self, event):
        if not event.is_directory:
            log_event("file_deleted", {"path": event.src_path})

# --- Process Monitor ---
def monitor_processes(known_pids):
    current = set(psutil.pids())
    new = current - known_pids
    terminated = known_pids - current

    for pid in new:
        try:
            p = psutil.Process(pid)
            log_event("process_started", {"pid": pid, "name": p.name(), "exe": p.exe(), "cmdline": p.cmdline()})
        except Exception:
            pass

    for pid in terminated:
        log_event("process_terminated", {"pid": pid})

    return current

# --- Main Function ---
def start_edr():
    print("Starting Python EDR...")
    known_pids = set(psutil.pids())

    # File system watcher
    observer = Observer()
    handler = FileMonitorHandler()
    observer.schedule(handler, WATCH_DIR, recursive=True)
    observer.start()

    try:
        while True:
            known_pids = monitor_processes(known_pids)
            time.sleep(2)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    print("EDR stopped.")

if __name__ == "__main__":
    start_edr()
