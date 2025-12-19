from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os, time, subprocess

EXCLUDE_PATHS = {".git", ".venv", "__pycache__", "output"}

def run(cmd):
    print(f"$ {cmd}")
    subprocess.run(cmd, shell=True, check=False)

class GitHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        # Skip excluded paths
        if any(x in event.src_path for x in EXCLUDE_PATHS):
            return
        print(f"Change detected: {event.src_path}")
        run("git add .")
        run('git commit -m "auto-update"')
        run("git push origin main")

if __name__ == "__main__":
    path = "."
    observer = Observer()
    handler = GitHandler()
    observer.schedule(handler, path, recursive=True)
    observer.start()
    print("✅ Auto Git Sync started. Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
