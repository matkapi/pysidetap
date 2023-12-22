Python Simple decision table procesor
=====================================

.. image:: https://github.com/matkapi/pysidetap/workflows/ci/badge.svg?branch=main
    :target: https://github.com/matkapi/pysidetap/actions?workflow=ci
    :alt: CI

.. image:: https://codecov.io/gh/matkapi/pysidetap/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/matkapi/pysidetap
    :alt: Codecov

.. image:: https://api.codeclimate.com/v1/badges/d96cc9a1841a819cd4f5/maintainability
   :target: https://codeclimate.com/github/matkapi/pysidetap/maintainability
   :alt: Maintainability

.. image:: https://img.shields.io/codeclimate/tech-debt/matkapi/pysidetap
    :target: https://codeclimate.com/github/matkapi/pysidetap
    :alt: Code Climate technical debt

.. image:: https://img.shields.io/readthedocs/pysidetap/latest?label=Read%20the%20Docs
    :target: https://pysidetap.readthedocs.io/en/latest/index.html
    :alt: Read the Docs

.. image:: https://badge.fury.io/py/pysidetap.svg
    :target: https://badge.fury.io/py/pysidetap
    :alt: PyPi

Install
-------

pysidetap is available on PyPI `pypi-pysidetap`_ and you can install it using pip:

```sh
pip install pysidetap
```

Summary
-------

Simple Decision Table Processor

https://en.wikipedia.org/wiki/Decision_table

This function find and return field 'return' from Decision Table,
        when all operands in row by 'fields' are True.

Example:
--------
This example show use case off Traffic lights decisions.

https://en.wikipedia.org/wiki/Traffic_light#Meanings_of_signals

Decision Table:

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

.. code-block:: python

    from pysidetap.processor import DTProcessor

    DTableTL = [
        {
            'fields': {
                'red': {'op':'==', 'value':'on'},
                'yellow': {'op':'==', 'value':'off'},
                'green': {'op':'==', 'value':'off'},
            },
            # Traffic may not proceed beyond the stop line or 
            # otherwise enter the intersection
            'return': {'stop'} 
        },
        {
            'fields': {
                'red': {'op':'==', 'value':'on'},
                'yellow': {'op':'==', 'value':'on'},
                'green': {'op':'==', 'value':'off'},
            },
            # The signal is about to change, but the red light rules do apply
            'return': {'ready'} 
        },
        {
            'fields': {
                'red': {'op':'==', 'value':'off'},
                'yellow': {'op':'==', 'value':'off'},
                'green': {'op':'==', 'value':'on'},
            },
            # Traffic may not pass the stop line or enter the intersection 
            # unless it cannot safely stop when the light shows
            'return': {'go'} 
        },
        {
            'fields': {
                'red': {'op':'==', 'value':'off'},
                'yellow': {'op':'==', 'value':'on'},
                'green': {'op':'==', 'value':'off'},
            },
            # Traffic may proceed unless it would not clear the intersection
            # before the next change of phase
            'return': {'break'}
        },
        {
            'fields': {
                'red': {'op':'==', 'value':'off'},
                'yellow': {'op':'==', 'value':'off'},
                'green': {'op':'==', 'value':'off'},
            },
            # Traffic lights is off
            'return': {'off'} 
        },
    ]

    p = DTProcessor(DTableTL)
    for red in ['on','off']:
        for yellow in ['on','off']:
            for green in ['on','off']:
                result = p.process({'red':red, 'yellow':yellow, 'green':green})
                print(f'red: {red}, yellow: {yellow}, green: {green}, result:{result}')


Issues and Discussions
----------------------

As usual for any GitHub-based project, raise an `issue`_ if you find any bug or
want to suggest an improvement, or open a `discussion`_ if you want to discuss
or chat :wink:

Version
-------

v0.0.10

.. _GitHub Actions: https://github.com/features/actions
.. _PyPI: https://pypi.org
.. _discussion: https://github.com/matkapi/pysidetap/discussions
.. _documentation: https://pysidetap.readthedocs.io/
.. _even for scientific software: https://github.com/MolSSI/cookiecutter-cms
.. _hypothesis: https://hypothesis.readthedocs.io/en/latest/
.. _ionel: https://github.com/ionelmc
.. _issue: https://github.com/matkapi/pysidetap/issues
.. _latest branch: https://github.com/matkapi/pysidetap/tree/latest
.. _master branch: https://github.com/matkapi/pysidetap/tree/master
.. _pdb-tools: https://github.com/haddocking/pdb-tools/blob/2a070bbacee9d6608b44bb6d2f749beefd6a7690/.github/workflows/bump-version-on-push.yml
.. _project's documentation: https://pysidetap.readthedocs.io/en/latest/index.html
.. _pytest: https://docs.pytest.org/en/stable/
.. _python-nameless: https://github.com/ionelmc/python-nameless
.. _structlog: https://github.com/hynek/structlog
.. _test.pypi.org: https://test.pypi.org
.. _tox-gh-actions: https://github.com/ymyzk/tox-gh-actions
.. _tox: https://tox.readthedocs.io/en/latest/
.. _ReadTheDocs: https://readthedocs.org/
.. _pypi-pysidetap: https://pypi.org/project/pysidetap/
