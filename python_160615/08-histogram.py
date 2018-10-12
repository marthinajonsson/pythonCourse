import sys

def histogram(L):
    if L == []:
        return []
    m = max(L)
    if m <= 0:
        m = 1
    def normalize(v):
        return int(v * 60 // m)

    return map(normalize, L)

def assertEqual(first, second, msg=""):
    if first != second:
        msg += "\n{0!r} != {1!r}".format(first, second)
        raise AssertionError(msg)

def testHistogram():
    assertEqual(list(histogram([1])), [60])
    assertEqual(list(histogram([1, 2, 3])), [20, 40, 60])
    assertEqual(list(histogram([])), [])
    assertEqual(list(histogram([0])), [0])

    print("All tests passed successfully.")

script_name = sys.argv[0]
arguments = sys.argv[1:]

USAGE = "Usage: {0} <list of values>".format(script_name)

if len(arguments) == 0:
    print(USAGE)
elif arguments[0] == "test":
    testHistogram()
else:
    values = list(map(float, arguments))
    for v, count in zip(values, histogram(values)):
        print("{0:10.2f} | {1}".format(v, "*" * count))