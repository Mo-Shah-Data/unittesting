import pytest
import unit_testing_sample as uts

# General Tests

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4

# Testing with heaps

def test_create_empty_list():
    assert uts.create_empty_list()==[]

def test_add_values_list_and_create_heap():
    assert len(uts.add_values_list_and_create_heap()) == 9

def test_add_to_heap():
    assert len(uts.add_to_heap()) == 10

#
# def test_structure_not_empty():
#     assert strucure is not empty
#
# def test_structure_inserts():
#     assert struture inserts
#
# def test_struture_appends():
#     assert structure appends
#
# def test_structure_pops():
#     assert structure pops
#
#
# # Arguments
# def test_default_structure_argument():
#     assert default_arg_output
#
# def test_manual_input_argument():
#     assert manual_input_arg
#
