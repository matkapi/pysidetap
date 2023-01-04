"""Asserts from simple tests."""


DTableEQ = [
    {
        'fields': {
            'field1': {'op': '==', 'value': 1},
            },
        'return': 'field1==1'
        },
    {
        'fields': {
            'field1': {'op': '!=', 'value': 1},
            },
        'return': 'field1!=1'
        }
    ]

DTableLT_GTEQ = [
    {
        'fields': {
            'field1': {'op': '<', 'value': 1},
            },
        'return': 'field1<1'
        },
    {
        'fields': {
            'field1': {'op': '>=', 'value': 1},
            },
        'return': 'field1>=1'
        }
    ]

DTableGT_LTEQ = [
    {
        'fields': {
            'field1': {'op': '<=', 'value': 1},
            },
        'return': 'field1<=1'
        },
    {
        'fields': {
            'field1': {'op': '>', 'value': 1},
            },
        'return': 'field1>1'
        }
    ]

DTableNone = [
    {
        'fields': {
            'field1': {'op': '==', 'value': 1},
            },
        'return': 'field1<=1'
        }
    ]
