import pytest
import unit_testing_sample as uts
import heapq

# create happy, edge and bad cases.

# General Tests

# def func(x):
#     return x + 1

# def test_answer():
#     assert func(3) == 4

# Testing with heaps

def test_create_empty_list():
    assert uts.create_empty_list()==[]

def test_add_values_list_and_create_heap():
    assert len(uts.add_values_list_and_create_heap()) == 9

def test_add_to_heap():
    assert len(uts.add_to_heap()) == 10

def test_check_heap_for_specific_value():
    heap = uts.add_values_list_and_create_heap()
    # heap should contain 1002
    assert 1002 in heap

def test_check_heap_for_non_value():
    with pytest.raises(AssertionError):
        heap = uts.add_values_list_and_create_heap()
        # heap should contain 1002
        assert 100222 in heap

def test_heappop(): # make sure it pops the smallest value in the heap
    values_list = [1001, 199, 1002, 1003, 10, 12, 200, 1004, 1005]
    heapq.heapify(values_list)
    assert heapq.heappop(values_list) == 10 #  10 is the minimum value here

# happy case
def test_heapushpop_happy(): # inserts smallest vlaue and then pops smallest value
    values_list = [1001, 199, 1002, 1003, 10, 12, 200, 1004, 1005]
    heapq.heapify(values_list)
    assert heapq.heappushpop(values_list, 1) == 1

# edge case
def test_heapushpop_edge(): # test edge case
    values_list = [1001, 199, 1002, 1003,0.99, 10, 12, 200, 1004, 1005]
    heapq.heapify(values_list)
    assert heapq.heappushpop(values_list,1) == 0.99

#Todo: complete the folloing:

def test_heapushpop_bad(): # test bad case
    with pytest.raises(AssertionError) as excinfo:
        values_list = [1001, 199, 1002, 1003, 0.99, 10, 12, 200, 1004, 1005]
        heapq.heapify(values_list)
        popped_value =  heapq.heappushpop(values_list,0.1) == 0.99
        assert popped_value is True


# # bad case
def test_heapreplace():
    with pytest.raises(IndexError): #as excinfo:
        values_list = []
        heapq.heapify(values_list)
        heapq.heapreplace(values_list, 10)
        #assert "IndexError" in str(excinfo.value)

@pytest.mark.xfail(raises=IndexError)
def test_heapreplace_exp_fail():
        values_list = []
        heapq.heapify(values_list)
        heapq.heapreplace(values_list, 10)


# happy case
def test_heapreplace_happy():
    values_list = [101,9]
    heapq.heapify(values_list)
    heapq.heapreplace(values_list, 10) # value inserted is larger than what is popped

# edge case
def test_heapreplace_bad():
    values_list = [101,9.99]
    heapq.heapify(values_list)
    heapq.heapreplace(values_list, 10) # value inserted si larger than what is popped


def test_merge_happy():
    values_list_1 = [10, 100, 1000]
    values_list_2 = [20, 200, 2000]
    assert list(heapq.merge(values_list_1, values_list_2)) == [10,20,100,200,1000,2000]

def test_merge_edge():
    values_list_1 = [10, 100, 1000]
    values_list_2 = [20, 100.001, 2000]
    assert list(heapq.merge(values_list_1, values_list_2)) == [10,20,100,100.001,1000,2000]

def test_merge_bad():
    with pytest.raises(TypeError):
        values_list_1 = [10, 100, 1000]
        values_list_2 = [20, '200', 2000]
        test_merge = list(heapq.merge(values_list_1, values_list_2))

def test_nlargest_happy():
    values_list = [10, 20, 100,30000, 1000, 2000]
    largest = heapq.nlargest(1,values_list)
    assert largest[0] == 30000 # list position is used here as that is what is returned

def test_nlargest_bad():
    with pytest.raises(AssertionError):
        values_list = [10, 20, 100, 30000, 1000, 2000]
        largest = heapq.nlargest(1, values_list)
        assert largest[0] == 10  # list position is used here as that is what is returned

def test_nlargest_edge():
    values_list = [10, 20, 100, 30000,29999.99, 1000, 2000]
    largest = heapq.nlargest(1, values_list)
    assert largest[0] == 30000  # list position is used here as that is what is returned









# import heapq
#
# values_list_1 = [10,100,1000]
# values_list_2 = [20,"200",2000]
# def mergearray(vl1,vl2):
#     return heapq.merge(values_list_1,values_list_2)
#
# test = list(mergearray(values_list_1,values_list_2))


#
# values_list = [1001, 199, 1002, 1003, 0.99, 10, 12, 200, 1004, 1005]
# heapq.heapify(values_list)
# popped_value = heapq.heappushpop(values_list, 0.1) == 0.99


