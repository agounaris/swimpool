# -*- coding: utf-8 -*-
from multiprocessing import Pool, TimeoutError
from inspect import isfunction
import random
import math


class ResultSet(object):
    def __init__(self, function_name, function_result):
        self._function_name = function_name
        self._function_result = function_result

    @property
    def function_name(self):
        return self._function_name

    @property
    def function_result(self):
        return self._function_result


class Process(object):
    def __init__(self, process_unit=None, process_units=None, process_data=None, processes=None):
        self._process_unit = process_unit
        self._process_units = process_units
        self._process_data = process_data
        self._processes = processes
        self._pool = Pool(processes)

    def simulate(self):
        if self._process_units is None:
            raise AttributeError("Process units should be a function or a list of functions")

        if self._process_data is None:
            raise AttributeError("Process data should a scalar type or a list of scalars")

        if isinstance(self._process_units, list):
            return self._simulate_list_functions_single_data()

        if isfunction(self._process_unit) and isinstance(self._process_data, list):
            return self._simulate_single_function_list_data()


    def _simulate_list_functions_list_data(self):
        pass

    def _simulate_single_function_list_data(self):
        pass

    def _simulate_list_functions_single_data(self):
        results = []
        for item in self._process_units:
            result_set = ResultSet(item.__name__, self._pool.map_async(item, self._process_data).get())
            results.append(result_set)

        return results


# def f(x):
#     return math.log(x + random.randrange(1, 100))
#
#
# def y(x):
#     return math.log(x + random.randrange(1, 100))
#
#
# def z(x):
#     return math.log(x + random.randrange(1, 100))
#
#
# def j(x):
#     return math.log(x + random.randrange(1, 100))


# if __name__ == '__main__':
#     pool = Pool(processes=4)  # start 4 worker processes
#     # pool = Pool()              # start 4 worker processes
#
#     result_set = []
#     # print "[0, 1, 4,..., 81]"
#     # input_range = range(1000000)
#     sample = 50
#     input_range = random.sample(range(1, sample), sample - 1)
#
#     list_of_functions = [f, y, z, j]
#
#     results = []
#     for item in list_of_functions:
#         result_set = ResultSet(item.__name__, pool.map_async(item, input_range).get())
#         results.append(result_set)
#
#     for result_set in results:
#         plt.plot(result_set.function_result)
#
#     plt.legend([item.function_name for item in results], loc='upper left')
#     plt.show()
