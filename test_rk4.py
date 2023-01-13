import unittest
import numpy as np
import rk4l


# testing our RK4 module on a trig function to check sufficient accuracy
# important to test over trig functions as the mathimatics we wish to model will have
# negative and positive accelerations at different points

def temp_condition(r, t):
    return True

def function_goes_above_1(r, t):
    if r <= 0.0:
        return False
    else:
        return True

def f(x, i):
    return -1*np.sin(x)

class TestRK4(unittest.TestCase):

    def test_trig(self):
        result, domain = rk4l.extrapolate(f, 1, 6.28, 0.0001, temp_condition)

        self.assertTrue( abs(result[-1] - np.cos(6.28) < 0.001))

    # Need to check that we can end the program if some limit is met,
    # in our case if the ray goes into the blackhole or if it goes out to infinity

    def test_limit(self):
        result, domain = rk4l.extrapolate(f, 1, 6.28, 0.0001, function_goes_above_1)
        print(len(result))
        self.assertTrue(abs(result[-1] - 1) < 0.01)

if __name__ == "__main__":
    unittest.main()
