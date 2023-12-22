"""Performs opetrations tests for less or equal then."""


import pytest

from pysidetap.execptions import ProcessorException
from pysidetap.libs.operations import op_lteq


def test_op_lteq_int_true():
    """Test less or equal then funcion for integer."""
    r = op_lteq(1, 2)
    assert r is True
    r = op_lteq(1, 1)
    assert r is True


def test_op_lteq_int_false():
    """Test less or equal then funcion for integer."""
    r = op_lteq(2, 1)
    assert r is False


def test_op_lteq_float_true():
    """Test less or equal then funcion for float."""
    r = op_lteq(25.345, 25.346)
    assert r is True
    r = op_lteq(25.345, 25.345)
    assert r is True


def test_op_lteq_float_false():
    """Test less or equal then funcion for float not."""
    r = op_lteq(25.346, 25.345)
    assert r is False


def test_op_lteq_string_true():
    """Test less or equal then funcion for string."""
    r = op_lteq('abc', 'def')
    assert r is True
    r = op_lteq('abc', 'abc')
    assert r is True


def test_op_lteq_string_false():
    """Test less or equal then funcion for string."""
    r = op_lteq('def', 'abc')
    assert r is False


def test_op_lteq_list_true():
    """Test less or equal then funcion for list int."""
    r = op_lteq([1, 2, 3], [1, 2, 4])
    assert r is True
    r = op_lteq([1, 2, 3], [1, 2, 3])
    assert r is True


def test_op_lteq_list_false():
    """Test less or equal then funcion for list int."""
    r = op_lteq([3, 2, 1], [1, 2, 3])
    assert r is False


def test_op_lteq_tuple_true():
    """Test less or equal then funcion for tuple integer."""
    r = op_lteq((1, 2, 3), (1, 2, 4))
    assert r is True
    r = op_lteq((1, 2, 3), (1, 2, 3))
    assert r is True


def test_op_lteq_tuple_false():
    """Test less or equal then funcion for tuple integer."""
    r = op_lteq((1, 2, 4), (1, 2, 3))
    assert r is False


def test_op_lteq_set_true():
    """Test less or equal then funcion for set integer."""
    r = op_lteq({1, 2}, {1, 2, 3})
    assert r is True
    r = op_lteq({1, 2, 3}, {1, 2, 3})
    assert r is True


def test_op_lteq_set_false():
    """Test less or equal then funcion set integer."""
    r = op_lteq({1, 2, 3, 4}, {1, 2, 3})
    assert r is False


def test_op_lteq_dict():
    """Test less or equal then funcion for dict."""
    with pytest.raises(ProcessorException):
        op_lteq({'value1': 1}, {'value1': 2})
