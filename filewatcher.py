import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from subprocess import call
 
 
class Watcher:
    DIRECTORY_TO_WATCH = "/home/pi/Pictures/Aufnahme/image" + str(i) + ".jpg"
 
    def __init__(self):
        self.observer = Observer()
 
    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print ("Error")
 
        self.observer.join()
 
 
class Handler(FileSystemEventHandler):