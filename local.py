def localErrorEuler(xi, yi):
    local = [0]
    for xN, yN in (zip(xi, yi)):
        yNext = stepEuler(xN, yN)
        local.append(abs(yNext - (-np.log(xN + h) + c1 * np.log(xN + h) ** 2)))
    return local[:-1]


def localErrorImpEuler(xi, yi):
    local = [0]
    for xN, yN in (zip(xi, yi)):
        yNext = stepImpEuler(xN, yN)
        local.append(abs(yNext - (-np.log(xN + h) + c1 * np.log(xN + h) ** 2)))
    return local[:-1]


def localErrorRungeKutta(xi, yi):
    local = [0]
    for xN, yN in (zip(xi, yi)):
        yNext = stepRungeKutta(xN, yN)
        local.append(abs(yNext - (-np.log(xN + h) + c1 * np.log(xN + h) ** 2)))
    return local[:-1]

 def stepEuler(xi, yi):
        yNext = yi + mainFunc(xi, yi) * h
        return yNext

def stepImpEuler(xi, yi):
    yNext = yi + h * mainFunc(xi + h / 2, yi + (h / 2) * mainFunc(xi, yi))
    return yNext

def stepRungeKutta(xi, yi):
    k1 = mainFunc(xi, yi)
    k2 = mainFunc(xi + h / 2, yi + h * k1 / 2)
    k3 = mainFunc(xi + h / 2, yi + h * k2 / 2)
    k4 = mainFunc(xi + h, yi + h * k3)
    yNext = yi + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return yNext