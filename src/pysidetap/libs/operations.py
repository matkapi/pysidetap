"""library that result simple Comparison operations."""


def op_eq(value1: any, value2: any) -> bool:
    """op_eq Operation equal.

    Args
    ----
        value1 : any
            first value to be evaluated by operation
        value2 : any
            second value to be evaluated by operation

    Returns
    -------
        bool
            if value1 == value2 True else False
    """
    if value1 == value2:
        return True
    return False


def op_noteq(value1: any, value2: any) -> bool:
    """op_noteq Operation not equal.

    Args
    ----
        value1: any
            first value to be evaluated by operation
        value2: any
            second value to be evaluated by operation

    Returns
    -------
        bool: if value1 != value2 True else False
    """
    if value1 != value2:
        return True
    return False


def op_gt(value1: any, value2: any) -> bool:
    """op_gt Operation great then.

    For args sets is testet subset https://en.wikipedia.org/wiki/Subset.

    Args
    ----
        value1: any
            first value to be evaluated by operation
        value2: any
            second value to be evaluated by operation

    Returns
    -------
        bool
            if value1 > value2 True else False
    """
    if value1 > value2:
        return True
    return False


def op_gteq(value1: any, value2: any) -> bool:
    """op_gt Operation great then or equal.

    For args sets is testet subset https://en.wikipedia.org/wiki/Subset.

    Args
    ----
        value1: any
            first value to be evaluated by operation
        value2: any
            second value to be evaluated by operation

    Returns
    -------
        bool
            if value1 >= value2 True else False
    """
    if value1 >= value2:
        return True
    return False


def op_lt(value1: any, value2: any) -> bool:
    """op_lt Operation less then.

    Args
    ----
        value1: any
            first value to be evaluated by operation
        value2: any
            second value to be evaluated by operation

    Returns
    -------
        bool
            if value1<value2 True else False
    """
    if value1 < value2:
        return True
    return False


def op_lteq(value1: any, value2: any) -> bool:
    """op_lteq Operation less then or equal.

    Args
    ----
        value1: any
            first value to be evaluated by operation
        value2: any
            second value to be evaluated by operation

    Returns
    -------
        bool
            if value1 <= value2 True else False
    """
    if value1 <= value2:
        return True
    return False
