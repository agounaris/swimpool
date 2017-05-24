# -*- coding: utf-8 -*-
from multiprocessing import Pool


class ResultSet(object):
    def __init__(self, function_name, function_result):
        """ResultSet initialization, standarises output

        Args:
            function_name (string): The name of the function
            function_result (list): Results
        """
        self._function_name = function_name
        self._function_result = function_result

    @property
    def function_name(self):
        return self._function_name

    @property
    def function_result(self):
        return self._function_result


class Simulation(object):
    def __init__(self, process_units=None, process_data=None, processes=None):
        """Process initialization

        Args:
            process_units (list): list of input functions
            process_data (list): list of input data
            processes (int): Number of pool processes to use
        """
        self._process_units = process_units
        self._process_data = process_data
        self._processes = processes
        self._pool = Pool(processes)

    def simulate(self):
        """Simulation start function

        Returns:
            list: a list containing ResultSet objects

        Raises:
        AttributeError: If functions or data are empty
        ValueError: If number of functions are different than
            the number of given data in case of multiple data
        """
        if self._process_units is None:
            raise AttributeError('Process units is needed')

        if self._process_data is None:
            raise AttributeError('Process data is needed')

        if isinstance(self._process_units, list) and \
           all(isinstance(i, list) for i in self._process_data):
            # multiple functions pointing to multiple inputs

            if len(self._process_units) != len(self._process_data):
                raise ValueError(
                    'Process units count is different than process data')
            return self._simulate_list_functions_list_data()

        if isinstance(self._process_units, list) and \
           isinstance(self._process_data, list):
            return self._simulate_list_functions_single_data()

    def _simulate_list_functions_list_data(self):
        """Simulates multiple functions with multiple data

        Returns:
            list: a list containing ResultSet objects
        """
        results = []
        for counter, item in enumerate(self._process_units):
            result_set = ResultSet(item.__name__, self._pool.map_async(
                item, self._process_data[counter]).get())
            results.append(result_set)

        return results

    def _simulate_list_functions_single_data(self):
        """Simulates multiple functions with the same data

        Returns:
            list: a list containing ResultSet objects
        """
        results = []
        for item in self._process_units:
            result_set = ResultSet(item.__name__, self._pool.map_async(
                item, self._process_data).get())
            results.append(result_set)

        return results
