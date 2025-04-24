from collections import defaultdict
from typing import List


def solution(tasks:List[int], space:int):
    last_completed = defaultdict(int)
    num_days = 0
    for i, task in enumerate(tasks):
        
