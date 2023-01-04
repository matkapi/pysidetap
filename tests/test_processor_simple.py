"""Performs general tests."""


from asserts_simple import (
    DTableEQ,
    DTableGT_LTEQ,
    DTableLT_GTEQ,
    DTableNone
    )
from pysidetap.processor import DTProcessor


def test_DTProcessor():
    """Test create DTProcessor."""
    DTProcessor()


def test_DTProcessor_with_table():
    """Test create DTProcessor with table."""
    DTProcessor(DTableEQ)


def test_DTProcessor_load_new_table():
    """Test Load new table."""
    p = DTProcessor(DTableEQ)
    p.load_table(DTableLT_GTEQ)


def test_DTProcessor_with_DTableEQ_EQ():
    """Test if field1 is equal 1."""
    p = DTProcessor(DTableEQ)
    r = p.process({'field1': 1})
    assert r == 'field1==1'


def test_DTProcessor_with_DTableEQ_NOTEQ():
    """Test if field1 is not equal 1."""
    p = DTProcessor(DTableEQ)
    r = p.process({'field1': 0})
    assert r == 'field1!=1'


def test_DTProcessor_with_DTableLT_GTEQ_LT():
    """Just asserts True."""
    p = DTProcessor(DTableLT_GTEQ)
    r = p.process({'field1': 2})
    assert r == 'field1>=1'


def test_DTProcessor_with_DTableLT_GTEQ_GT():
    """Just asserts True."""
    p = DTProcessor(DTableLT_GTEQ)
    r = p.process({'field1': 1})
    assert r == 'field1>=1'


def test_DTProcessor_with_DTableLT_GTEQ_GTEQ():
    """Just asserts True."""
    p = DTProcessor(DTableLT_GTEQ)
    r = p.process({'field1': 0})
    assert r == 'field1<1'


def test_DTProcessor_with_DTableGT_LTEQ_LTEQ():
    """Just asserts True."""
    p = DTProcessor(DTableGT_LTEQ)
    r = p.process({'field1': 1})
    assert r == 'field1<=1'


def test_DTProcessor_with_DTableGT_LTEQ_LT():
    """Just asserts True."""
    p = DTProcessor(DTableGT_LTEQ)
    r = p.process({'field1': 0})
    assert r == 'field1<=1'


def test_DTProcessor_with_DTableGT_LTEQ_GT():
    """Just asserts True."""
    p = DTProcessor(DTableGT_LTEQ)
    r = p.process({'field1': 2})
    assert r == 'field1>1'


def test_DTProcessor_with_DTableNone():
    """Just asserts True."""
    p = DTProcessor(DTableNone)
    r = p.process({'field1': 2})
    assert r is None
