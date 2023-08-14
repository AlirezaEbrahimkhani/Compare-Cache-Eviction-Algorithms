import requests
from time import sleep
import json
import random
from utils.evictAlgo import EvictionAlgorithm
import matplotlib.pyplot as plt
import numpy as np

class Main:
    
    def __init__(self, test_cases) -> None:
        self.test_cases = test_cases
        self.randMin = 1
        self.randMax = 100

    def getTweet(self, evictionAlgo: EvictionAlgorithm, id: int):
        url: str = 'http://localhost:8000/tweet/' + evictionAlgo.value
        r = requests.get(url, params={'id': id})
        return r.text
    
    def lruTest(self):
        hit_count = 0
        for i in range(0, self.test_cases):
            rand_num = self.__genRandomNum(self.randMin, self.randMax)
            resp = main.getTweet(EvictionAlgorithm.LRU, rand_num)
            if json.loads(resp)['hit']:
                hit_count = hit_count + 1
        return hit_count
    
    def lfuTest(self):
        hit_count = 0
        for i in range(0, self.test_cases):
            rand_num = self.__genRandomNum(self.randMin, self.randMax)
            resp = main.getTweet(EvictionAlgorithm.LFU, rand_num)
            if json.loads(resp)['hit']:
                hit_count = hit_count + 1
        return hit_count
    
    def arcTest(self):
        hit_count = 0
        for i in range(0, self.test_cases):
            rand_num = self.__genRandomNum(self.randMin, self.randMax)
            resp = main.getTweet(EvictionAlgorithm.ARC, rand_num)
            if json.loads(resp)['hit']:
                hit_count = hit_count + 1
        return hit_count
                    
    def __genRandomNum(self, min, max):
        return random.randint(min, max)
    
    def plotHitMiss(self):
        lru_hit = self.lruTest()
        lfu_hit = self.lfuTest()
        arc_hit = self.arcTest()
        hits = [lru_hit, lfu_hit, arc_hit]
        misses = [self.test_cases - lru_hit, self.test_cases - lfu_hit, self.test_cases - arc_hit]
        species = ('LRU', 'LFU', 'ARC')
        columns = {
            'Hit': np.array(hits),
            'Miss': np.array(misses),
        }
        width = 0.6
        fig, ax = plt.subplots()
        bottom = np.zeros(3)

        for hit, miss in columns.items():
            p = ax.bar(species, miss, width, label=hit, bottom=bottom)
            bottom += miss
            ax.bar_label(p, label_type='center')

        ax.set_title('Compare Eviction Algorithms')
        ax.legend()
        plt.show()

main = Main(100)

main.plotHitMiss()
