from heapq import heapify,heappop

a_list = ['R', 'C', 'T', 'H', 'E', 'D', 'L']

heap = heapify(a_list)
print(a_list)
heappop(a_list)
print("After popping")
print(a_list)


# using a while loop to pop
from heapq import heapify, heappop

a_list = ['D', 'E', 'L', 'H', 'R', 'T']
heapify(a_list)
while len(a_list) > 0:
    print(heappop(a_list))

# using heap push

from heapq import heapify, heappush

a_list = ['D', 'E', 'L', 'H', 'R', 'T']
heapify(a_list)
heappush(a_list,'Z')
print(a_list)

# pythn only supports min heaps, but you can turn it into a max heap by multiplying each value by -1