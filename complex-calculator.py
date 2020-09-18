import cmath
import math

ans = []


def recZ(z):
    global ans
    x = complex(f"{cmath.rect(z[0], math.radians(z[1])):.2f}")
    ans.clear()
    ans.append(x)
    return ans


def rec(r, phi):
    global ans
    ans.clear()
    ans.append(complex(f"{cmath.rect(r, math.radians(phi)):.2f}"))
    return ans


def polZ(z):
    global ans
    x = float(f"{cmath.polar(z[0])[0]:.2f}")
    y = float(f"{math.degrees(cmath.polar(z[0])[1]):.2f}")
    ans.clear()
    ans.append(x)
    ans.append(y)
    return ans


def pol(r, phi):
    global ans
    ans.clear()
    ans.append(float(f"{cmath.polar(complex(r, phi))[0]:.2f}"))
    ans.append(float(f"{math.degrees(cmath.polar(complex(r, phi))[1]):.2f}"))
    return ans


def para(a, b):
    global ans
    ans.clear()
    ans.append((a * b) / (a + b))
    return ans
