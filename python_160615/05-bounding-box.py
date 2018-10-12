import unittest

def boundingBox(points):
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]

    left = min(xs)
    top = max(ys)
    right = max(xs)
    bottom = min(ys)

    return left, top, right, bottom

class test(unittest.TestCase):
    def test_bunding_box(self):
        polygon = [(0, 4), (3, 2), (2, -2), (-2, -2), (-3, 2)]
  
        left, top, right, bottom = boundingBox(polygon)

        self.assertEqual(left, -3)
        self.assertEqual(top, 4)
        self.assertEqual(right, 3)
        self.assertEqual(bottom, -2)

if __name__ == '__main__':
   unittest.main()