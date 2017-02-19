import sys
import time

print(sys.argv)

if len(sys.argv) != 2:
    print("wrong number of arguments")
    sys.exit(1)

with open(sys.argv[1]) as inputstr:
    DATA = inputstr.read()

START = time.time()
exec(DATA)
END = time.time()
print(START-END)
