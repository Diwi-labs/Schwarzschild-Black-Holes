import rk4l
import numpy as np
import unittest

def df(x, t):
    return -1*np.sin(t)

def temp_con(r, t):
    if t >= 6.28:
        return False
    else:
        return True

r, d = rk4l.extrapolate(df, 1, 6.2801, 0.0001, temp_con)
print(r[-1])

class Testrk4l(unittest.TestCase):

    def test_trig(self):
        result, domain = rk4l.extrapolate(df, 1, 6.2801, 0.0001, temp_con)
        self.assertTrue(abs(result[-1] - np.cos(6.28)) < 0.0001)


if __name__ == '__main__':
    unittest.main()