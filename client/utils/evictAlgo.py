from enum import Enum
 
class EvictionAlgorithm(Enum):
    LRU = 'lru'
    LFU = 'lfu'
    ARC = 'arc'
