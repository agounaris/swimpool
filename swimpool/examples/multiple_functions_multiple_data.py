import math
import random
import matplotlib.pyplot as plt
from ..process import Simulation


def f(x):
    return math.log(x + random.randrange(1, 100))


def y(x):
    return math.log(x + random.randrange(1, 100))


def z(x):
    return math.log(x + random.randrange(1, 100))


def j(x):
    return math.log(x + random.randrange(1, 100))


if __name__ == '__main__':
    list_of_functions = [f, y, z, j]

    input_ranges = []
    for i in range(len(list_of_functions)):
        input_ranges.append([i + 1, i + 2, i + 3, i + 4])

    s = Simulation(list_of_functions, input_ranges)
    results = s.simulate()

    print(results)

    for result_set in results:
        plt.plot(result_set.function_result)

    plt.legend([item.function_name for item in results], loc='upper left')
    plt.show()
