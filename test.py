import sys
import unittest
import random


arguments = sys.argv[1:]


old_time, delta = arguments
hour = int(old_time[0:2])
minute = int(old_time[3:5])
delta = int(delta)


def run_tests():
    assert add_time(16,34,12) == (16,46)

def add_time(h,m,d):
    time = h * 60 + m + d
    return (int(time/60)%24, time%60)


new_time = add_time(hour, minute, delta)
print (hour)
print (minute)
print(delta)

if arguments == ["test"]:
    run_tests()



a = [3, 4, 1]
a.sort()
print (a)

print(list(range(3,11)))

print ("{:02d}:{:02d}".format(new_time[0], new_time[1]))

colors = ["red", "yellow", "blue", "green"]
favorite = colors[random.randrange(len(colors))]
print ("my favourite color: ", favorite)

stack = []
stack.append("one")
stack.append("seccond")
print(stack.pop())

stack.append("another2")
print (stack.pop())

wanted = 7
found_index = -1
l = [4, 8, 7, 2, 9, 7]

def find_first(wanted, l):
   for i, e in enumerate(l):
      if e == wanted:
         return i


print(find_first(7, l))
print ([4,8,7,2,9,7].index(7))

#Class TimeTests(unittest.TestCase):
 #   def test_addition(self):
  #      self.assertEquals(add_time(23, 40, 35), (00, 15))

#if __name__ == '__main__':
 #   unittest.main()



