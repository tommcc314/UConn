import math
from scipy import optimize

def const(x,a):
    return a

def lin(x, a, b):
    return a * x + b

def quad(x, a, b, c):
    return a * x * x + b * x + c
def fit_data(fitting, x_data, y_data):
    params, params_cov = optimize.curve_fit(fitting, x_data, y_data)
    #if constant, unpack one parameter
    if params.size == 1:
        a = params[0]

        # create yfit list
        y_fit = []
        for x in x_data:
            y_fit.append(const(x,a))

    # if linear, unpack two parameters
    elif params.size == 2:
        a = params[0]
        b = params[1]

        # create yfit list
        y_fit = []
        for x in x_data:
            y_fit.append(lin(x, a, b))

    # if quad, unpack three parameters
    elif params.size == 3:
        a = params[0]
        b = params[1]
        c = params[2]

        # create yfit list
        y_fit = []
        for x in x_data:
            y_fit.append(quad(x, a, b, c))
    else:
        sys.exit("Invalid function")
    #calculate RMS
    se = 0
    for (yf, yd) in zip(y_fit, y_data):
        se += (yd - yf) ** 2
    rms = math.sqrt(se / len(y_fit))

    #return everything
    return (params, rms, y_fit)
#testing my functions
if __name__ == "__main__":
    x = [i for i in range(5)]
    y = [i for i in range(5)]
    print(fit_data(const, x, y))
    print(fit_data(lin, x, y))
