import sys
import time

print(sys.argv)

if len(sys.argv) != 2:
    print("wrong number of arguments")
    sys.exit(1)

START = time.time()
exec("sys.argv[1]")
END = time.time()
print(START-END)
