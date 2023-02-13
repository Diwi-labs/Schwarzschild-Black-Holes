def run(U, i, y0, tn):
    k1 = U(y0, i, tn)
    k2 = U(y0 + k1 * tn / 2, i + tn / 2)
    k3 = U(y0 + k2 * tn / 2, i + tn / 2)
    k4 = U(y0 + k3 * tn, i + tn)

    return y0 + (k1 + 2 * k2 + 2 * k3 + k4) * (tn / 6)