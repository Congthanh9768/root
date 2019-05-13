import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print("The file has been changed!")
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path='D:\\TaiLieu\lưu bút', recursive=False)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
