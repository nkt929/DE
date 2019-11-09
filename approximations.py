def euler(ii):
    xi, hi = get_x_h(ii)
    yi = [y0] * ii
    for j in range(1, ii):
        yi[j] = yi[j - 1] + mainFunc(xi[j - 1], yi[j - 1]) * hi
    return yi


def impEuler(ii):
    xi, hi = get_x_h(ii)
    yi = [y0]*ii
    for j in range(1, ii):
        yi[j] = yi[j-1] + hi * mainFunc(xi[j-1] + hi / 2, yi[j - 1] + (hi / 2) * mainFunc(xi[j - 1], yi[j - 1]))
    return yi

def rungeKutta(ii):
    xi, hi = get_x_h(ii)
    yi = [y0]*ii
    for j in range(1, ii):
        k1 = mainFunc(xi[j-1], yi[j-1])
        k2 = mainFunc(xi[j-1] + hi / 2, yi[j-1] + hi * k1 / 2)
        k3 = mainFunc(xi[j-1] + hi / 2, yi[j-1] + hi * k2 / 2)
        k4 = mainFunc(xi[j-1] + hi, yi[j-1] + hi * k3)
        yi[j] = yi[j-1] + hi / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return yi