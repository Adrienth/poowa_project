from threading import Thread, Lock
from queue import Queue

from myfavshows.backend import *
from myfavshows.classes import *

import requests

show_ids = [60735, 79744, 1408, 72844, 1425, 21720, 1413, 62643, 1399, 79460]

#q = Queue(show_ids)


class MyThread(Thread):

    __show_ids = []
    __pointer = 0
    shows = []
    lock = Lock()

    def __init__(self):
        Thread.__init__(self)

    def _get_pointer(self):
        return self.__pointer
    
    def _set_pointer(self,value):
        self.__pointer = value
    
    pointer = property(_get_pointer, _set_pointer)

    def _get_shows_ids(self):
        return self.__show_ids

    def _set_shows_ids(self,value):
        self.__show_ids = value

    show_ids = property(_get_shows_ids, _set_shows_ids)

    def run(self):
        MyThread.lock.acquire()
        show_id = MyThread.show_ids[MyThread.pointer]
        MyThread.pointer += 1
        MyThread.lock.release()

        show = ShowDetailedView(show_id)

        MyThread.lock.acquire()
        MyThread.shows.append(show)
        MyThread.lock.release()


def exo1():

    MyThread.show_ids = show_ids
    threads = []
    for i in show_ids:
        threads.append(MyThread())

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print(MyThread.shows)


exo1()