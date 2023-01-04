"""Asserts from complex tests."""

min_temp = 48.0
max_temp = 55.0
cooldown = 30 * 60
warmup = 60 * 60

DTableReservoar = [
    {
        'fields': {
            'reservoar_temp': {'op': '<', 'value': min_temp},
            'cooldown': {'op': '>', 'value': cooldown},
            'heat_status': {'op': '==', 'value': 'off'}
            },
        'return': {
            'heat': 'on',
            'message': 'reservoar heat_status was off and temp was under '
            'min_temp and cooldown was passed'
            }
        },
    {
        'fields': {
            'reservoar_temp': {'op': '<=', 'value': max_temp},
            'cooldown': {'op': '<', 'value': warmup},
            'heat_status': {'op': '==', 'value': 'on'}
            },
        'return': {
            'heat': 'on',
            'message': 'reservoar heat_status was on and temp was under '
            'max_temp and warmup is not passed'
            }
        },
    {
        'fields': {
            'reservoar_temp': {'op': '>=', 'value': max_temp},
            'cooldown': {'op': '<', 'value': warmup},
            'heat_status': {'op': '==', 'value': 'on'}
            },
        'return': {
            'heat': 'on',
            'message': 'reservoar heat_status was on and temp was over '
            'max_temp and warmup is not passed'
            }
        },
    {
        'return': {'heat': 'off', 'message': 'something else then heat off'}
        },
    ]

DTableTermostat = [
    {
        'fields': {
            'termostat_min': {'op': '<=', 'value': 20},
            'termostat_max': {'op': '>=', 'value': 22},
            'field1': {'op': '!=', 'value': 1},
            },
        'return': 'field1!=1'
        }
    ]
