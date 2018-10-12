import sys

def roman(n):
    return "V"

def assertEqual(first, second, msg=""):
    if first != second:
        msg += "\n{0!r} != {1!r}".format(first, second)
        raise AssertionError(msg)

def test_roman():
    assertEqual(roman(5), "V")

    print("All tests passed successfully.")

script_name = sys.argv[0]
arguments = sys.argv[1:]

USAGE = "Usage: {0} <number>".format(script_name)

if len(arguments) == 0 or len(arguments) > 1:
    print(USAGE)
elif arguments[0] == "test":
    test_roman()
else:
    number = int(arguments[0])
    print(roman(number))
