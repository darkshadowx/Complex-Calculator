# Complex Calculator Version 0.0.8 in Python Developed by Asif Mahmud

import cmath
import math

ans = []


def recZ(z):
    global ans
    print(z)
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
    if isinstance(z, complex):
        x = float(f"{cmath.polar(z)[0]:.2f}")
        y = float(f"{math.degrees(cmath.polar(z)[1]):.2f}")
    else:
        x = float(f"{cmath.polar(z[0])[0]:.2f}")
        y = float(f"{math.degrees(cmath.polar(z[0])[1]):.2f}")

    ans.clear()
    ans.append(x)
    ans.append(y)
    return ans


def pol(r, phi):
    global ans
    ans.clear()
    if isinstance(phi, complex):
        ans.append(float(f"{cmath.polar(r + phi)[0]:.2f}"))
        ans.append(float(f"{math.degrees(cmath.polar(r + phi)[1]):.2f}"))
    else:
        ans.append(float(f"{cmath.polar(complex(r, phi))[0]:.2f}"))
        ans.append(float(f"{math.degrees(cmath.polar(complex(r, phi))[1]):.2f}"))

    return ans


def para(a, b):
    global ans
    ans.clear()
    ans.append((a * b) / (a + b))
    return ans
