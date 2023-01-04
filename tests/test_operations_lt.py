"""Performs opetrations tests for."""


# isort: skip_file
import pytest
from pysidetap.libs.operations import op_lt


def test_op_lt_int_true():
    """Test less then funcion for integer."""
    r = op_lt(1, 2)
    assert r is True


def test_op_lt_int_false():
    """Test less then funcion for integer."""
    r = op_lt(2, 1)
    assert r is False


def test_op_lt_float_true():
    """Test less then funcion for float."""
    r = op_lt(25.345, 25.346)
    assert r is True


def test_op_lt_float_false():
    """Test less then funcion for float not."""
    r = op_lt(25.346, 25.345)
    assert r is False


def test_op_lt_string_true():
    """Test less then funcion for string."""
    r = op_lt('abc', 'def')
    assert r is True


def test_op_lt_string_false():
    """Test less then funcion for string."""
    r = op_lt('def', 'abc')
    assert r is False


def test_op_lt_list_true():
    """Test less then funcion for list int."""
    r = op_lt([1, 2, 3], [1, 2, 4])
    assert r is True


def test_op_lt_list_false():
    """Test less then funcion for list int."""
    r = op_lt([3, 2, 1], [1, 2, 3])
    assert r is False


def test_op_lt_tuple_true():
    """Test less then funcion for tuple integer."""
    r = op_lt((1, 2, 3), (1, 2, 4))
    assert r is True


def test_op_lt_tuple_false():
    """Test less then funcion for tuple integer."""
    r = op_lt((1, 2, 4), (1, 2, 3))
    assert r is False


def test_op_lt_set_true():
    """Test less then funcion for set integer."""
    r = op_lt({1, 2}, {1, 2, 3})
    assert r is True


def test_op_lt_set_false():
    """Test less then funcion set integer."""
    r = op_lt({1, 2, 3, 4}, {1, 2, 3})
    assert r is False


def test_op_lt_dict():
    """Test less then funcion for dict."""
    with pytest.raises(Exception):
        op_lt({'value1': 1}, {'value1': 2})
