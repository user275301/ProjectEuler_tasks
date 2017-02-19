maxdivider = 20

def task5(maxdivider):
	num = 11
	test = 1
	while test != 0:
		test = 0
		for div in range(1,maxdivider):
			test += num%div
		num += 1
	return num - 1

print(task5(maxdivider))