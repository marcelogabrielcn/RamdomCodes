def fdx(var):
    f = (2 * (var ** 2)) - (5 * var) + 2
    return f


def deriv(var):
    d = 4 * var - 5
    return d


def xk1(var, a, b):
    xk = var - (a / b)
    return xk


def erro(a, b):
    e = a - b
    return e


x = 100
erro_Objetivo = 10 ** -7
erro_Atual = x
c = 0

print("K\t\t\tXk\t\t\t\t\t\t\tf(Xk)\t\t\t\t\t\tf'(Xk)\t\t\t\t\t\tXk+1\t\t\t\t\t\tErro")
while erro_Atual > erro_Objetivo:
    if c == 0:
        print(f"{c}\t\t\t%.14f\t\t\t%.14f\t\t%.14f\t\t\t%.14f\t\t\t%.14f" %
              (x, fdx(x), deriv(x), xk1(x, fdx(x), deriv(x)), abs(erro(xk1(x, fdx(x), deriv(x)), x))))
    else:
        print(f"{c}\t\t\t%.14f\t\t\t%.14f\t\t\t%.14f\t\t\t%.14f\t\t\t%.14f" %
          (x, fdx(x), deriv(x), xk1(x, fdx(x), deriv(x)), abs(erro(xk1(x, fdx(x), deriv(x)), x))))
    c += 1
    x = xk1(x, fdx(x), deriv(x))
    erro_Atual = abs(erro(xk1(x, fdx(x), deriv(x)), x))

print(f"{c}\t\t\t%.14f\t\t\t%.14f\t\t\t%.14f\t\t\t%.14f\t\t\t%.14f" %
          (x, fdx(x), deriv(x), xk1(x, fdx(x), deriv(x)), abs(erro(xk1(x, fdx(x), deriv(x)), x))))

print(f"\nForam necessárias {c+1} iterações para achar o erro aceitável.")

