# importing "heapq" to implement heap queue
import heapq


def create_empty_list():
    # initializing list
    main_list = []
    return main_list


def add_values_list_and_create_heap():
    main_list = create_empty_list()
    main_list.extend([1001, 199, 1002, 1003, 10, 12, 200, 1004, 1005])
    # using heapify to convert list into heap
    heapq.heapify(main_list)
    return main_list
#
# # printing created heap
# print ("The created heap is : ",(list(li)))

def add_to_heap():
    main_list = add_values_list_and_create_heap()
    heapq.heappush(main_list, 14)
    return main_list

