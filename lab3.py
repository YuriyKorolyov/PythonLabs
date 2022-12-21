#-*- coding:utf-8*-
from random import randint
from pyDatalog import pyDatalog
number = 10
pyDatalog.create_terms('X, Y, Result, Sum, Average, Range, RandSum, Median, Rand')

print(f"Сумма чисел 0 - {number}:\n")
(Sum[Range] == sum_(X, for_each = X)) <= X.in_(range_(Range + 1))
print(f"{Sum == Sum[number]}\n")

print(f"среднее значение:\n")
(Average[Range] == Result) <= (Range / 2 == Result)
print(f"{Average == Average[number]}\n")

randlist = [randint(0, 99) for _ in range(0, 100)]
randlist.sort()

print(f"сумма 100 рандомных интов:\n")
(Sum[Rand] == sum_(X, for_each = X)) <= X.in_(Rand)
print(f"{Sum[randlist] == RandSum}\n")

print(f"медиана:\n")
(Median[Rand] == Result) <= ((Rand[49] + Rand[50]) / 2 == Result)
print(Median[randlist] == Median)
