import pytest
from ..pagination_builder import pagination_builder

#test for valid inputs
def test_valid_inputs():
    assert pagination_builder(4, 5, 1, 0)  == "1 ... 4 5"
    assert pagination_builder(4, 10, 2, 2)  == "1 2 3 4 5 6 ... 9 10"
    assert pagination_builder(700, 9000, 3, 1)  == "1 2 3 ... 699 700 701 ... 8998 8999 9000"
    assert pagination_builder(0, 0, 2, 2)  == ""

# test for type errors
def test_pagination_for_type_error():
    with pytest.raises(TypeError):
        pagination_builder("1", 5, 2, 1)
    with pytest.raises(TypeError):
        pagination_builder(1, "5", 2, 1)
        
# test for value erros
def test_pagination_for_value_error(): 
    with pytest.raises(ValueError):
        pagination_builder(-1, 5, 2, 1)
    with pytest.raises(ValueError):
        pagination_builder(1, -5, 2, 1)
    with pytest.raises(ValueError):
        pagination_builder(6, 5, -2, -1)