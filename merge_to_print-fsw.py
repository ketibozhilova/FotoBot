import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import saveOrigPicture
import os
import numpy as np
import PIL
from PIL import Image
import printing


class Watcher:
    DIRECTORY_TO_WATCH = "/home/pi/Pictures/erhalten/"

    def __init__(self):
        self.observer = Observer()  #beobachter

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

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
                            
            print ("Received created event - %s." % event.src_path)

        elif event.event_type == 'modified':
           # Taken any action here when a file is modified.
            if  os.path.exists('/home/pi/Pictures/original/original.jpg'):
                list_im = ['/home/pi/Pictures/original/original.jpg', '/home/pi/Pictures/erhalten/abgeholt.jpg']
                imgs    = [ PIL.Image.open(i) for i in list_im ]

                 # pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
                min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
                imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )

                 # save that beautiful picture
                #imgs_comb = PIL.Image.fromarray( imgs_comb)
                #imgs_comb.save( '/home/pi/Pictures/merge-to-print/Trifecta.jpg' )    

                 # for a vertical stacking it is simple: use vstack
                imgs_comb = np.vstack( (np.asarray(i.resize(min_shape) ) for i in imgs ) )
                imgs_comb = PIL.Image.fromarray(imgs_comb)
                imgs_comb.save('/home/pi/Pictures/merge-to-print/merge.jpg')

                pathtosave = '/home/pi/Pictures/merge-to-print/merge.jpg'
                printing.toprint(pathtosave)

                print ("Received modified event - %s." % event.src_path)
            else: print("merge.jpg not found")

            

if __name__ == '__main__':
    w = Watcher()
    w.run()



      #list_im = ['/home/pi/Pictures/original/orig1.jpg', '/home/pi/Pictures/original/orig2.jpg']
                #imgs    = [ PIL.Image.open(i) for i in list_im ]

                ## pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
                #min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
                #imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )

                ## save that beautiful picture
                ##imgs_comb = PIL.Image.fromarray( imgs_comb)
                ##imgs_comb.save( '/home/pi/Pictures/merge-to-print/Trifecta.jpg' )    

                ## for a vertical stacking it is simple: use vstack
                #imgs_comb = np.vstack( (np.asarray(i.resize(min_shape) ) for i in imgs ) )
                #imgs_comb = PIL.Image.fromarray(imgs_comb)
                #imgs_comb.save('/home/pi/Pictures/merge-to-print/Trifecta.jpg')