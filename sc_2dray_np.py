import numpy as np
import rk4plus1
import rk4l



class ray:

    def __init__(self, r, b, t ,show_path = False):
        self.r0 = r
        self.rdot = -(np.sqrt((1/b) ** 2 + (1/r) ** 2 - (1/r) ** 3))
        self.b = b
        self.path = []
        self.dpath = []
        self.t = t
        #number of revolutions and fidelity of method
        self.domain = np.arange(0, t[0], t[1])
        self.show_path = show_path

    def ic(self, u, t):
        return -(np.sqrt((1 / self.b) ** 2 + (u) ** 2 - (u) ** 3))

    def udd(self, u, t):
        return 1.5*(u)**2 - u

    def ud(self, u, t):
        return self.path[-1]


    def solve(self):
        self.path.append(1/self.r0)
        self.dpath.append(self.ud(1/self.r0, 0))

        #print(self.path)
        #print(self.dpath)
        #print(self.domain)


        if self.show_path:
            for i in self.domain:
                self.path




#r = ray(20, 27/16, (12.6, 0.0001), True)
#r.solve()

