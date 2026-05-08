# Min Heap implementation for priority queue

import heapq

def demo_heap():
    data = [5, 3, 8, 1, 2]
    heapq.heapify(data)  # convert list to heap
    print("Heap:", data)

    heapq.heappush(data, 0)
    print("After insert 0:", data)

    smallest = heapq.heappop(data)
    print("Extracted min:", smallest)
    print("Heap after extract:", data)

if __name__ == "__main__":
    demo_heap()


# Heap: [1, 2, 8, 3, 5]
# After insert 0: [0, 2, 1, 3, 5, 8]
# Extracted min: 0
# Heap after extract: [1, 2, 8, 3, 5]
