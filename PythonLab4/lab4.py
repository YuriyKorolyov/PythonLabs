import csv
from functools import reduce


def accumulata(accumulator, x):
    return (accumulator * x[0] + x[1]) / float(x[0] + 1)

#Посчитать средний уровень pH в красном вине
#pH - 8й по индексу столбец

with open("winequality-red.csv",'r') as file:

    reader = csv.reader(file,delimiter=";")
    next(reader)

    mapped_to_float_reader = enumerate(map(lambda x : float(x[8]),reader))

    res = reduce(accumulata,mapped_to_float_reader,0)

with open("RESULT.txt",'w') as file_writer:
    file_writer.write(str(res))
