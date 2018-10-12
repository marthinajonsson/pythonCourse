import sys
import unittest

def suffix(n):
	if n == 2:
		return "nd"
	elif n == 3:
		return "rd"
	elif n == 4 or n == 5 or (n >= 11 and n <= 13):
		return "th"
	elif n == 21 or n == 1:
		return "st"
	elif n == 22:
		return "nd"

class test(unittest.TestCase):
    def test_suffix(self):
        self.assertEqual(suffix(1), "st")


script_name = sys.argv[0]
arguments = sys.argv[1:]

USAGE = "Usage: {0} <number>".format(script_name)

if len(arguments) == 0 or len(arguments) > 1:
    print(USAGE)
elif arguments[0] == "test":
    if __name__ == '__main__':
        unittest.main()
else:
    number = int(arguments[0])
    suffix = suffix(number)
    print("{0}{1}".format(number, suffix))
