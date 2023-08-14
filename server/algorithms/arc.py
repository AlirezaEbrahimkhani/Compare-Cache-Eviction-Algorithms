from utils.finder import Finder
from models.types import Response, TweetLike
from collections import OrderedDict
import math

class ARCAlgorithm:
    def __init__(self, capacity):
        self.c = capacity
        self.p = 0
        self.finder = Finder()
        self.t1 = set()
        self.t2 = OrderedDict()
        self.b1 = set()
        self.b2 = set()

    def get(self, key) -> Response[TweetLike]:
        res: Response[TweetLike] = self.__adjust_cache(key)
        return res

    def __adjust_cache(self, key: str):
        hit = True
        if key in self.t1:
            self.t1.remove(key)
            self.t2[key] = 0

        elif key in self.t2:
            data = self.t2.get(key)
            data = data + 1
            self.t2[key] = data

        elif key in self.b1:
            self.p = min(self.c, self.p + max(len(self.b2) / len(self.b1), 1))
            self.__replace(key)
            self.b1.remove(key)
            self.t2[key] = 0

        elif key in self.b2:
            self.p = max(0, self.p - max(len(self.b1) / len(self.b2), 1))
            self.__replace(key)
            self.b2.remove(key)
            self.t2[key] = 0

        else:
            if len(self.t1) == self.c:
                evicted_key = self.t1.pop()
                self.b1.add(evicted_key)
            elif len(self.t1) + len(self.t2) == self.c:
                evicted_key = self.__find_min(self.t2)
                if evicted_key != '':
                    self.t2.pop(evicted_key)
                    self.b2.add(evicted_key)
            self.t1.add(key)
            hit = False

        response: Response[TweetLike] = {
            "data": self.finder.find(key),
            "hit": hit
        }
        return response

    def __replace(self, key):
        if self.t1 and ((key in self.b2 and len(self.t1) == self.p) or (len(self.t1) > self.p)):
            old = self.t1.pop()
            self.b1.add(old)
        else:
            evicted_key = self.__find_min(self.t2)
            if evicted_key != '':
                self.t2.pop(evicted_key)
                self.b2.add(evicted_key)

    def __find_min(self, dict: OrderedDict):
        min = math.inf
        find_key = ""
        for key, value in dict.items():
            if value < min:
                min = value
                find_key = key
        return find_key
