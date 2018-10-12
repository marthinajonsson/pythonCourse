import sys
import unittest

# First thing I made pass:

def add_time(h, m, d):
    time = h * 60 + m + d
    return (int(time / 60) % 24, time % 60)

class test(unittest.TestCase):
    def test_add_time(self):
        self.assertEquals(add_time(16, 34, 12), (16, 47))
        self.assertEquals(add_time(21, 50, 11), (22, 1))
        self.assertEquals(add_time(23, 40, 35), (00, 15))

def run_tests():
    unittest.main()

script_name = sys.argv[0]
arguments = sys.argv[1:]

USAGE = "Usage: {0} <hh:mm> <delta>".format(script_name)

if arguments == ["test"]:
    run_tests()
elif len(arguments) == 2:
    old_time, delta = arguments
    hour = int(old_time[0:2])
    minute = int(old_time[3:5])
    delta = int(delta)
    new_time = add_time(hour, minute, delta)
    print("{0:02d}:{1:02d}".format(new_time[0], new_time[1]))
else:
    print(USAGE)
