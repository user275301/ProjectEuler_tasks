import itertools
flatten_iter = itertools.chain.from_iterable
MAXDIVIDER = 10

def factor(num):
    divisorsSet = {1}
    for divisor in range(2, num):
        if num%divisor == 0:
            divisorsSet.add(divisor)
    return divisorsSet

numberSets = list(map(factor, range(1, MAXDIVIDER + 1)))
print(numberSets)
resultSet = {1}
resultSet = resultSet.union(*numberSets)
result = 1
for prod in resultSet:
    result *= prod
print(factor(2520))
print(resultSet)
print(result)
