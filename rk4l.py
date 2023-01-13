import numpy as np


def extrapolate(U, U0, t, tn, condition):
    results = []
    domain = np.arange(0, t, tn)
    y0 = U0

    for i in domain:
            if condition(y0, i) == True:
                results.append(y0)

                k1 = U(y0, i)
                k2 = U(y0 + k1 * tn / 2, i + tn / 2)
                k3 = U(y0 + k2 *tn / 2, i + tn /2)
                k4 = U(y0 + k3 * tn, i + tn)

                y0 = y0 + (k1 + 2*k2 + 2*k3 + k4) * (tn/6)

            else:
                break

    return results, domain
