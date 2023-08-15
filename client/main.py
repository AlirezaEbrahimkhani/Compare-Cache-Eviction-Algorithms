import requests
import json
import random
from utils.evictAlgo import EvictionAlgorithm
import matplotlib.pyplot as plt
import numpy as np

class Main:

    def __init__(self):
        self.real_test_case = [1, 2, 3, 4, 1, 1, 1, 3, 4, 6, 2, 1]  # main idea :D
        self.test_nums = [1, 2, 3, 4, 1, 1, 1, 3, 4, 6, 2, 1, 3, 5, 5, 6, 3, 3, 3, 5, 6, 8, 4, 3, 5, 6, 7, 8, 5, 5, 5, 7, 8, 10, 6, 5, 8, 9, 9, 10, 7, 7, 7, 9, 10, 12, 8, 7]

    def getTweet(self, evictionAlgo: EvictionAlgorithm, id: int):
        url: str = 'http://localhost:8000/tweet/' + evictionAlgo.value
        r = requests.get(url, params={'id': id})
        return r.text

    def clearCache(self):
        url: str = 'http://localhost:8000/tweet/clear'
        r = requests.get(url)
        return r.text

    def generate_rand_test_case(self, count, min, max):
        return [self.__genRandomNum(min, max) for _ in range(0, count)]

    def generate_weighted_rand_test_case(self, count, min, max):
        nums = []
        weights = []
        num = 0
        for i in range(min, max):
            nums.append(i)
            num = num + self.__genRandomNum(0, 3)
            weights.append(num)
        return random.choices(nums, cum_weights=tuple(weights), k=count)

    def test_algorithms(self, data):
        lru_hit_count = 0
        lfu_hit_count = 0
        arc_hit_count = 0
        for item in data:
            lru_resp = main.getTweet(EvictionAlgorithm.LRU, item)
            if json.loads(lru_resp)['hit']:
                lru_hit_count = lru_hit_count + 1
        self.clearCache()
        for item in data:
            lfu_resp = main.getTweet(EvictionAlgorithm.LFU, item)
            if json.loads(lfu_resp)['hit']:
                lfu_hit_count = lfu_hit_count + 1
        for item in data:
            arc_resp = main.getTweet(EvictionAlgorithm.ARC, item)
            if json.loads(arc_resp)['hit']:
                arc_hit_count = arc_hit_count + 1

        return [lru_hit_count, lfu_hit_count, arc_hit_count]

    def __genRandomNum(self, min, max):
        return random.randint(min, max)

    def plotHitMiss(self, data):
        hits = self.test_algorithms(data)
        misses = [len(data) - hits[0], len(data) - hits[1], len(data) - hits[2]]
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


main = Main()

rand_nums = main.generate_rand_test_case(1000, 1, 800)
weighted_rand_nums = main.generate_weighted_rand_test_case(1000, 1, 800)

main.plotHitMiss(rand_nums)
