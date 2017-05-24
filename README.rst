========
swimpool
========


.. image:: https://img.shields.io/pypi/v/swimpool.svg
        :target: https://pypi.python.org/pypi/swimpool

.. image:: https://img.shields.io/travis/agounaris/swimpool.svg
        :target: https://travis-ci.org/agounaris/swimpool

.. image:: https://readthedocs.org/projects/swimpool/badge/?version=latest
        :target: https://swimpool.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/agounaris/swimpool/shield.svg
     :target: https://pyup.io/repos/github/agounaris/swimpool/
     :alt: Updates


A wrapper of multiprocessing pool


* Free software: BSD license


Features
--------

This tool was build mainly for simple monte carlo simulations using the multiprocess tool. I need a simple interface where I can throw in any number of functions and test them across the same or multiple inputs.

Clone the project, install the swimpool/examples/requirements_example.txt and checkout the sample code.

    python -m swimpool.examples.single_function_single_data
    
    python -m swimpool.examples.multiple_functions_same_data
    
    python -m swimpool.examples.multiple_functions_multiple_data

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

