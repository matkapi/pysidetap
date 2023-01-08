"""
This example show use case off Traffic lights decisions.

https://en.wikipedia.org/wiki/Traffic_light#Meanings_of_signals

+-------+----------+---------+--------+
| red   | yellow   | green   | return |
+=======+==========+=========+========+
| ==on  | ==off    | ==off   | stop   |
+-------+----------+---------+--------+
| ==on  | ==on     | ==off   | ready  |
+-------+----------+---------+--------+
| ==off | ==off    | ==on    | go     |
+-------+----------+---------+--------+
| ==off | ==on     | ==off   | break  |
+-------+----------+---------+--------+
| ==off | ==off    | ==off   | off    |
+-------+----------+---------+--------+
"""

import sys
  
# appending the parent directory path
sys.path.append('../src')

from pysidetap.processor import DTProcessor

DTableTL = [
    {
        'fields': {
            'red': {'op':'==', 'value':'on'},
            'yellow': {'op':'==', 'value':'off'},
            'green': {'op':'==', 'value':'off'},
        },
        'return': {'stop'} # Traffic may not proceed beyond the stop line or otherwise enter the intersection
    },
    {
        'fields': {
            'red': {'op':'==', 'value':'on'},
            'yellow': {'op':'==', 'value':'on'},
            'green': {'op':'==', 'value':'off'},
        },
        'return': {'ready'} # The signal is about to change, but the red light rules do apply
    },
    {
        'fields': {
            'red': {'op':'==', 'value':'off'},
            'yellow': {'op':'==', 'value':'off'},
            'green': {'op':'==', 'value':'on'},
        },
        'return': {'go'} # Traffic may not pass the stop line or enter the intersection unless it cannot safely stop when the light shows
    },
    {
        'fields': {
            'red': {'op':'==', 'value':'off'},
            'yellow': {'op':'==', 'value':'on'},
            'green': {'op':'==', 'value':'off'},
        },
        'return': {'break'} # Traffic may proceed unless it would not clear the intersection before the next change of phase
    },
    {
        'fields': {
            'red': {'op':'==', 'value':'off'},
            'yellow': {'op':'==', 'value':'off'},
            'green': {'op':'==', 'value':'off'},
        },
        'return': {'off'} # Traffic lights is off
    },
]

p = DTProcessor(DTableTL)
for red in ['on','off']:
    for yellow in ['on','off']:
        for green in ['on','off']:
            result = p.process({'red':red, 'yellow':yellow, 'green':green})
            print(f'red: {red}, yellow: {yellow}, green: {green}, result:{result}')