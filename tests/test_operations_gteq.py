"""Performs opetrations tests for."""


import pytest

# from pysidetap.execptions import ProcessorException
from pysidetap.libs.operations import op_gteq


def test_op_gteq_int_true():
    """Test great or equal then funcion for integer."""
    r = op_gteq(2, 1)
    assert r is True
    r = op_gteq(1, 1)
    assert r is True


def test_op_gteq_int_false():
    """Test great or equal then funcion for integer."""
    r = op_gteq(1, 2)
    assert r is False


def test_op_gteq_float_true():
    """Test great or equal then funcion for float."""
    r = op_gteq(25.346, 25.345)
    assert r is True
    r = op_gteq(25.345, 25.345)
    assert r is True


def test_op_gteq_float_false():
    """Test great or equal then funcion for float not."""
    r = op_gteq(25.345, 25.346)
    assert r is False


def test_op_gteq_string_true():
    """Test great or equal then funcion for string."""
    r = op_gteq('def', 'abc')
    assert r is True
    r = op_gteq('abc', 'abc')
    assert r is True


def test_op_gteq_string_false():
    """Test great or equal then funcion for string."""
    r = op_gteq('abc', 'def')
    assert r is False


def test_op_gteq_list_true():
    """Test great or equal then funcion for list int."""
    r = op_gteq([3, 2, 1], [1, 2, 3])
    assert r is True
    r = op_gteq([1, 2, 3], [1, 2, 3])
    assert r is True


def test_op_gteq_list_false():
    """Test great or equal then funcion for list int."""
    r = op_gteq([1, 2, 3], [1, 2, 4])
    assert r is False


def test_op_gteq_tuple_true():
    """Test great or equal then funcion for tuple integer."""
    r = op_gteq((1, 2, 4), (1, 2, 3))
    assert r is True
    r = op_gteq((1, 2, 3), (1, 2, 3))
    assert r is True


def test_op_gteq_tuple_false():
    """Test great or equal then funcion for tuple integer."""
    r = op_gteq((1, 2, 3), (1, 2, 4))
    assert r is False


def test_op_gteq_set_true():
    """Test great or equal then funcion for set integer."""
    r = op_gteq({1, 2, 3, 4}, {1, 2, 3})
    assert r is True
    r = op_gteq({1, 2, 3}, {1, 2, 3})
    assert r is True


def test_op_gteq_set_false():
    """Test great or equal then funcion set integer."""
    r = op_gteq({1, 2, 3}, {1, 2, 4})
    assert r is False


def test_op_gteq_dict():
    """Test great or equal then funcion for dict."""
    with pytest.raises(TypeError):
        op_gteq({'value1': 2}, {'value1': 1})
