"""Performs opetrations tests for."""


import pytest

from pysidetap.execptions import ProcessorException
from pysidetap.libs.operations import op_gt


def test_op_gt_int_true():
    """Test great then funcion for integer."""
    r = op_gt(2, 1)
    assert r is True


def test_op_gt_int_false():
    """Test great then funcion for integer."""
    r = op_gt(1, 2)
    assert r is False


def test_op_gt_float_true():
    """Test great then funcion for float great then."""
    r = op_gt(25.346, 25.345)
    assert r is True


def test_op_gt_float_false():
    """Test great then funcion for float not great then."""
    r = op_gt(25.345, 25.346)
    assert r is False


def test_op_gt_string_true():
    """Test great then funcion for string."""
    r = op_gt('def', 'abc')
    assert r is True


def test_op_gt_string_false():
    """Test great then funcion for string."""
    r = op_gt('abc', 'def')
    assert r is False


def test_op_gt_list_true():
    """Test great then funcion for list int."""
    r = op_gt([3, 2, 1], [1, 2, 3])
    assert r is True


def test_op_gt_list_false():
    """Test great then funcion for list int."""
    r = op_gt([1, 2, 3], [1, 2, 4])
    assert r is False


def test_op_gt_tuple_true():
    """Test great then funcion for tuple integer."""
    r = op_gt((1, 2, 4), (1, 2, 3))
    assert r is True


def test_op_gt_tuple_false():
    """Test great then funcion for tuple integer."""
    r = op_gt((1, 2, 3), (1, 2, 4))
    assert r is False


def test_op_gt_set_true():
    """Test great then funcion for set integer."""
    r = op_gt({1, 2, 3, 4}, {1, 2, 3})
    assert r is True


def test_op_gt_set_false():
    """Test great then funcion set integer."""
    r = op_gt({1, 2, 3}, {1, 2, 4})
    assert r is False


def test_op_gt_dict():
    """Test great then funcion for dict."""
    with pytest.raises(ProcessorException):
        op_gt({'value1': 2}, {'value1': 1})
