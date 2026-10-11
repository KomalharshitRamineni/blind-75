"""
heap-topk 

Trigger: you need the min or max repeatedly, while the set is changing — top-k · merge k sorted lists · streaming median (two heaps) · scheduling by earliest end time. If the set is static, just sort — no heap. Python `heapq` is min-only; negate for a max-heap. Complexity: O(n log k)
"""



import heapq

def heap_topk(arr, k):

    hashMap = {}

    for item in arr:
        hashMap = 1 + hashMap.get(item, 0)

    heap = []

    for item, freq in arr.items():
        heapq.heappush(heap, (freq,item))
        if len(heap) > k:
            heapq.heappop(heap)

    #This limits size of heap to k and also functions by removing min so remaining are largest

    #Pop from heap as needed
