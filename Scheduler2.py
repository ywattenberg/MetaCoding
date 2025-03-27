from collections import defaultdict


def solution(tasks, space):
    last_completed = defaultdict(int)
    num_days = 0
    for i, task in enumerate(tasks):
        
