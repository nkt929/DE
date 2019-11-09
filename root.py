
x_max = par3_var.get()
h = 0.1
x0 = par1_var.get()
y0 = par2_var.get()
i = int((x_max - x0) // h + 1)

x = [x0]*i
c1 = (y0 + np.log(x0)) / (np.log(x0)**2)
for jk in range(1, i):
    x[jk] = x[jk-1] + h

def get_x_h(ii):
    xi = [x0]*ii
    hi = (x_max-x0)/(ii-1)
    for j in range(1, ii):
        xi[j] = xi[j - 1] + hi
    return xi, hi

def exactSol(xi):
    yi = [y0]*len(xi)
    for j in range(len(xi)):
        yi[j] = -np.log(xi[j]) + c1*np.log(xi[j])**2
    return yi

def mainFunc(xi, yi):
    if xi > 0:
        return 1 / xi + (2 * yi) / (xi * np.log(xi))
    else:
        return 0