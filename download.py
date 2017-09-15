# coding=utf-8
import threading
import requests
import time
import urllib
from qqbot.utf8logger import INFO,ERROR,DEBUG
import Queue
import os


class Download(threading.Thread):
    def __init__(self, que):
        threading.Thread.__init__(self)
        self.queue = que

    def Schedule(self, a, b, c):
        """
        :param a: 已经下载的数据块
        :param b: 数据块的大小
        :param c: 远程文件的大小
        :return:
        """
        per = 100.0 * a * b / c
        if per > 100:
            per = 100
        print '%.2f%%' % per

    def run(self):
        while True:
            if not self.queue.empty():
                DEBUG(self.name)
                print self.name
                url = self.queue.get()
                ext = url.split('.')[-1]
                print 'thread download start'
                r = requests.get(url, verify=False)
                print 'thread download finished...'
                print 'thread writing start...'
                file_name = self.name + '.' + ext
                local_path = os.path.join('../', file_name)
                urllib.urlretrieve(url, local_path, self.Schedule)
                print 'thread writing finished...'


if __name__ == '__main__':

    queue = Queue.Queue(20)

    d = Download(queue)
    d.start()

    url = 'https://mp4.48.cn/live/bbf8a902-2e5d-4fa1-9c09-5151145f7c90.mp4'
    url2 = 'http://2519.liveplay.myqcloud.com/live/2519_2996320.flv'
    queue.put(url)
    queue.put(url2)

    while True:
        print 'main thread'
        time.sleep(30)
    # while True:
    #     print 'main thread'
    #     time.sleep(3)