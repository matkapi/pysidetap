"""Performs general tests."""


# isort: skip_file
from asserts_complex import DTableReservoar
from pysidetap.processor import DTProcessor


def test_DTProcessor_reservoar1():
    """Test when reservoar temp is under 47."""
    p = DTProcessor(DTableReservoar)
    r = p.process({
        'reservoar_temp': 47.0,
        'cooldown': 60 * 60,
        'heat_status': 'off'
        })
    assert r == {
        'heat': 'on',
        'message': 'reservoar heat_status was off and temp was under '
        'min_temp and cooldown was passed'
        }


def test_DTProcessor_reservoar2():
    """Test when reservoar temp is over 49."""
    p = DTProcessor(DTableReservoar)
    r = p.process({
        'reservoar_temp': 49.0,
        'cooldown': 60,
        'heat_status': 'on'
        })
    assert r == {
        'heat': 'on',
        'message': 'reservoar heat_status was on and temp was under '
        'max_temp and warmup is not passed'
        }


def test_DTProcessor_reservoar3():
    """Test when reservoar temp is over 56."""
    p = DTProcessor(DTableReservoar)
    r = p.process({
        'reservoar_temp': 56.0,
        'cooldown': 29 * 60,
        'heat_status': 'on'
        })
    assert r == {
        'heat': 'on',
        'message': 'reservoar heat_status was on and temp was over '
        'max_temp and warmup is not passed'
        }


def test_DTProcessor_reservoar4():
    """Test when reservoar temp is over 56."""
    p = DTProcessor(DTableReservoar)
    r = p.process({
        'reservoar_temp': 56.0,
        'cooldown': 31 * 60,
        'heat_status': 'on'
        })
    assert r == {
        'heat': 'on',
        'message': 'reservoar heat_status was on and temp was over '
        'max_temp and warmup is not passed'
        }


def test_DTProcessor_reservoar5():
    """Test when reservoar temp is under 56."""
    p = DTProcessor(DTableReservoar)
    r = p.process({
        'reservoar_temp': 54.0,
        'cooldown': 2 * 60,
        'heat_status': 'off'
        })
    assert r == {
        'heat': 'off',
        'message': 'something else then heat off'
        }


def test_DTProcessor_reservoar_all():
    """Test reservoar cover all statuses."""
    p = DTProcessor(DTableReservoar)
    for temp in range(40, 60):
        for cooldown in (0, 60 * 60):
            for heat_status in ['on', 'off']:
                r = p.process({
                    'reservoar_temp': temp,
                    'cooldown': cooldown,
                    'heat_status': heat_status
                    })
                assert r is not None
