"""Performs opetrations tests for not equal."""


import pysidetap.libs.operations as op


def test_op_noteq_int_true():
    """Test not equal funcion for integer not equal."""
    r = op.op_noteq(1, 2)
    assert r is True


def test_op_noteq_int_false():
    """Test not equal funcion for integer equal."""
    r = op.op_noteq(1, 1)
    assert r is False


def test_op_noteq_float_true():
    """Test not equal funcion for float not equal."""
    r = op.op_noteq(25.345, 25.344)
    assert r is True


def test_op_noteq_float_false():
    """Test not equal funcion for float equal."""
    r = op.op_noteq(25.345, 25.345)
    assert r is False


def test_op_noteq_string_true():
    """Test not equal funcion for string not equal."""
    r = op.op_noteq('\\text1', '\\text2')
    assert r is True


def test_op_noteq_string_false():
    """Test not equal funcion for string equal."""
    r = op.op_noteq('\\text1', '\\text1')
    assert r is False


def test_op_noteq_list_true():
    """Test not equal funcion for list int not equal."""
    r = op.op_noteq([1, 2, 3], [1, 2, 4])
    assert r is True


def test_op_noteq_list_false():
    """Test not equal funcion for list int equal."""
    r = op.op_noteq([1, 2, 3], [1, 2, 3])
    assert r is False


def test_op_noteq_tuple_true():
    """Test not equal funcion for tuple integer not equal."""
    r = op.op_noteq((1, 2, 3), (1, 2, 4))
    assert r is True


def test_op_noteq_tuple_false():
    """Test not equal funcion for tuple integer equal."""
    r = op.op_noteq((1, 2, 3), (1, 2, 3))
    assert r is False


def test_op_noteq_set_true():
    """Test not equal funcion set integer not equal."""
    r = op.op_noteq({1, 2, 3}, {1, 2, 4})
    assert r is True


def test_op_noteq_set_false():
    """Test not equal funcion for set integer equal."""
    r = op.op_noteq({1, 2, 3}, {1, 2, 3})
    assert r is False


def test_op_noteq_dict_true():
    """Test not equal funcion for dict not equal."""
    r = op.op_noteq({'value1': 1}, {'value1': 2})
    assert r is True


def test_op_noteq_dict_false():
    """Test not equal funcion for dict equal."""
    r = op.op_noteq({'value1': 1}, {'value1': 1})
    assert r is False
