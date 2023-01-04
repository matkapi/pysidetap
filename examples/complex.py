""" This example show use case off complex decisions
"""

from src.pysidetap.processor import DTProcessor

min_temp = 48.0
max_temp = 55.0
cooldown = 30*60
warmup = 60*60
DTableEQ = [
    {
        'fields': {
            'reservoar_temp': {'op':'<', 'value':min_temp},
            'cooldown': {'op':'>', 'value':cooldown},
            'heat_status': {'op':'==', 'value':'off'}
        },
        'return': {'heat':'on', 'message':'reservoar heat_status was off and temp was under min_temp and cooldown was passed '}
    },
    {
        'fields': {
            'reservoar_temp': {'op':'<=', 'value':max_temp},
            'cooldown': {'op':'<', 'value':warmup},
            'heat_status': {'op':'==', 'value':'on'}
        },
        'return': {'heat':'on', 'message':'reservoar heat_status was on and temp was under max_temp and warmup is not passed '}
    },
    {
        'fields': {
            'reservoar_temp': {'op':'>=', 'value':max_temp},
            'cooldown': {'op':'<', 'value':warmup},
            'heat_status': {'op':'==', 'value':'on'}
        },
        'return': {'heat':'on', 'message':'reservoar heat_status was on and temp was oves max_temp and warmup is not passed '}
    },
    {
        'return': {'heat':'off', 'message':'something else then heat off'}
    },
]

p = DTProcessor(DTableEQ)
for heat_status in ['on', 'off']:
    for temp in range(40, 60):
        for cooldown in range(0,2*3600, 60):
            r = p.process({'reservoar_temp':temp, 'cooldown':cooldown, 'heat_status':heat_status})
            if r == None:
                pass
            print(temp, cooldown, heat_status, r)
