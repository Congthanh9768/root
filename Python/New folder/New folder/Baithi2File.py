import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# 1 Watcher: Chờ và đợi cho bất kỳ sự kiện nào trên thư mục đã xem

class Watcher:
    DIRECTORY_TO_WATCH = "E:\\Python"

    def __init__(self):
        self.observer = Observer()
        print("Watching %s for Directory" % self.DIRECTORY_TO_WATCH)

    def run(self):
        event_handler = Handler()
        self.observer.schedule(
            event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()

# 2 Handler: Trình xử lý sự kiện thực hiện hành động khi nhận được một sự kiện


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            print(" Created File - %s." % event.src_path)

        elif event.event_type == 'modified':
            print(" Modified File - %s." % event.src_path)

        elif event.event_type == 'deleted':
            print(" Delete File - %s." % event.src_path)


if __name__ == '__main__':
    w = Watcher()
    w.run()
