"""Performs opetrations tests for equal."""


import pysidetap.libs.operations as op


def test_op_eq_int_true():
    """Test equal funcion for integer equal."""
    r = op.op_eq(1, 1)
    assert r is True


def test_op_eq_int_false():
    """Test equal funcion for integer not equal."""
    r = op.op_eq(1, 2)
    assert r is False


def test_op_eq_float_true():
    """Test equal funcion for float equal."""
    r = op.op_eq(25.345, 25.345)
    assert r is True


def test_op_eq_float_false():
    """Test equal funcion for float not equal."""
    r = op.op_eq(25.345, 25.344)
    assert r is False


def test_op_eq_string_true():
    """Test equal funcion for string equal."""
    r = op.op_eq('\\text1', '\\text1')
    assert r is True


def test_op_eq_string_false():
    """Test equal funcion for string not equal."""
    r = op.op_eq('\\text1', '\\text2')
    assert r is False


def test_op_eq_list_true():
    """Test equal funcion for list int equal."""
    r = op.op_eq([1, 2, 3], [1, 2, 3])
    assert r is True


def test_op_eq_list_false():
    """Test equal funcion for list int not equal."""
    r = op.op_eq([1, 2, 3], [1, 2, 4])
    assert r is False


def test_op_eq_tuple_true():
    """Test equal funcion for tuple integer equal."""
    r = op.op_eq((1, 2, 3), (1, 2, 3))
    assert r is True


def test_op_eq_tuple_false():
    """Test equal funcion for tuple integer not equal."""
    r = op.op_eq((1, 2, 3), (1, 2, 4))
    assert r is False


def test_op_eq_set_true():
    """Test equal funcion for set integer equal."""
    r = op.op_eq({1, 2, 3}, {1, 2, 3})
    assert r is True


def test_op_eq_set_false():
    """Test equal funcion set integer not equal."""
    r = op.op_eq({1, 2, 3}, {1, 2, 4})
    assert r is False


def test_op_eq_dict_true():
    """Test equal funcion for dict equal."""
    r = op.op_eq({'value1': 1}, {'value1': 1})
    assert r is True


def test_op_eq_dict_false():
    """Test equal funcion for dict not equal."""
    r = op.op_eq({'value1': 1}, {'value1': 2})
    assert r is False
