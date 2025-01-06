import sys

if len(sys.argv) < 2:
    print("Provide at least one argument")
    sys.exit(1)

sorted_args = sorted(sys.argv[1:], key=len)
shortest = sorted_args[0]

print("The shortest argument is:", shortest)
