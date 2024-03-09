import pytest
from ..pagination_builder import pagination_builder

# Test valid cases
def test_no_pages():
    assert pagination_builder(0, 0, 2, 2) == ""

def test_no_pages_no_boundaries_or_around():
    assert pagination_builder(0, 0, 0, 0) == ""

def test_boundaries_zero_around_covers_first_page():
    assert pagination_builder(3, 10, 0, 2) == "1 2 3 4 5 ..."

def test_current_page_equal_total_pages():
    assert pagination_builder(15, 15, 3, 1) == "1 2 3 ... 13 14 15"
 
def test_small_boundaries_and_around():
    assert pagination_builder(4, 5, 1, 0) == "1 ... 4 5" 

def test_zero_boundaries_and_around_case_one():
    assert pagination_builder(5, 10, 0, 0) == "... 5 ..."

def test_zero_boundaries_and_around_case_two():
    assert pagination_builder(1, 10, 0, 0) == "1 ..."

def test_zero_boundaries_and_around_one():
    assert pagination_builder(5,10,0,1) == "... 4 5 6 ..."

def test_pages_with_around_and_boundaries():
    assert pagination_builder(5, 10, 2, 1) == "1 2 ... 4 5 6 ... 9 10"

def test_around_greater_than_total_pages():
    assert pagination_builder(1, 1, 2, 2) == "1"

def test_boundaries_greater_than_total_pages():
    assert pagination_builder(1, 1, 4, 2) == "1"

def test_entire_large_range():
  assert pagination_builder(1000, 10000000000000000, 3, 1) == "1 2 3 ... 999 1000 1001 ... 9999999999999998 9999999999999999 10000000000000000"

def test_single_page_with_no_boundaries_and_around():
    assert pagination_builder(1, 2, 0, 0) == "1 ..."

def test_large_total_page_and_small_around_small_boundary():
    assert pagination_builder(1, 1000, 3, 1) == "1 2 3 ... 998 999 1000"

def test_high_boundaries():
    assert pagination_builder(1, 10, 6, 1) == "1 2 3 4 5 6 7 8 9 10"

def test_low_boundaries_and_no_around():
    assert pagination_builder(100, 100, 1, 0) == "1 ... 100"

def test_low_boundaries_and_no_around():
    assert pagination_builder(100, 100, 1, 0) == "1 ... 100"
    
def test_low_equal_boundaries_and_around():
    assert pagination_builder(4, 10, 2, 2) == "1 2 3 4 5 6 ... 9 10"

def test_high_equal_boundaries_and_around():
    assert pagination_builder(4, 10, 6, 6) == "1 2 3 4 5 6 7 8 9 10"

def test_equal_current_page_and_total_page_with_no_boundaries_and_around():
    assert pagination_builder(100, 100, 0, 0) == "... 100"

def test_pages_with_low_boundaries_and_around():
    assert pagination_builder(50, 100, 1, 0) == "1 ... 50 ... 100"

def test_max_range_pagination():
    assert pagination_builder(4, 10, 9, 10) == "1 2 3 4 5 6 7 8 9 10"

def test_pagination_with_low_boundaries_and_around():
    assert pagination_builder(10, 20, 1, 4) == "1 ... 6 7 8 9 10 11 12 13 14 ... 20"

def test_large_numbers():
    assert pagination_builder(7000, 90000000000, 4, 1)  == "1 2 3 4 ... 6999 7000 7001 ... 89999999997 89999999998 89999999999 90000000000"


# Test type errors with string values
def test_current_page_as_string():
    with pytest.raises(TypeError):
        pagination_builder("1", 5, 2, 1)

def test_total_pages_as_string():
    with pytest.raises(TypeError):
        pagination_builder(1, "5", 2, 1)

def test_boundaries_as_string():
    with pytest.raises(TypeError):
        pagination_builder(1, 5, "2", 1)

def test_around_as_string():
    with pytest.raises(TypeError):
        pagination_builder(1, 5, 2, "1")

# Test type errors with float values
def test_current_page_as_float():
    with pytest.raises(TypeError):
        pagination_builder(1.5, 5, 2, 1)

def test_total_pages_as_float():
    with pytest.raises(TypeError):
        pagination_builder(1, 5.5, 2, 1)

def test_boundaries_as_float():
    with pytest.raises(TypeError):
        pagination_builder(1, 5, 2.5, 1)

def test_around_as_float():
    with pytest.raises(TypeError):
        pagination_builder(1, 5, 2, 1.5)
        
# Test type errors with boolean values
def test_boolean_current_page():
    with pytest.raises(TypeError):
        pagination_builder(True, 10, 2, 1)
    
def test_boolean_current_page_and_around():
    with pytest.raises(TypeError):
        pagination_builder(True, 10, 2, False)

def test_boolean_total_pages():
    with pytest.raises(TypeError):
        pagination_builder(1, True, 2, 1)

def test_boolean_boundaries():
    with pytest.raises(TypeError):
        pagination_builder(1, 10, True, 1)

def test_boolean_around():
    with pytest.raises(TypeError):
        pagination_builder(1, 10, 2, True)

def test_boolean_around_and_total_pages():
    with pytest.raises(TypeError):
        pagination_builder(1, False, 2, True)

# Test value errors
def test_negative_current_page():
    with pytest.raises(ValueError):
        pagination_builder(-1, 5, 2, 1)

def test_negative_total_pages():
    with pytest.raises(ValueError):
        pagination_builder(1, -5, 2, 1)

def test_negative_boundaries_around():
    with pytest.raises(ValueError):
        pagination_builder(6, 5, -2, -1)

def test_negative_current_page_and_total_pages():
    with pytest.raises(ValueError):    
        pagination_builder(-3, -5, 2, 2)

def test_current_page_zero():
    with pytest.raises(ValueError):
        pagination_builder(0, 5, 2, 1)

def test_current_page_greater_than_total_pages():
    with pytest.raises(ValueError):   
        pagination_builder(10, 5, 2, 2)

