#!/usr/bin/env python3
import sys
import math
import os


def usage(exit_code=0):
    progname = os.path.basename(sys.argv[0])
    print(
        f'usage: {progname} sumX sumY sum(xSquare) sum(ySquare) sumXY n')
    sys.exit(exit_code)


def findSXX(xi, x2, n):
    return (x2 - (pow(xi, 2) / n))


def findSYY(yi, y2, n):
    return (y2 - (pow(yi, 2) / n))


def findSXY(xy, xi, yi, n):
    return (xy - ((xi*yi) / n))


def findB1(sxy, sxx):
    return sxy/sxx


def findB0(yBar, b1, xBar):
    return yBar - b1*xBar


def findSSE(syy, b1, sxy):
    return syy-(b1*sxy)


def findRSq(sse, sst):
    return (1 - (sse/sst))


def findEstStd(sse, sxx, n):
    return (math.sqrt(abs(sse/(n-2))))/math.sqrt(abs(sxx))


def main():

    if (sys.argv[1] == "-h"):
        usage(0)

    xi = float(sys.argv[1])
    yi = float(sys.argv[2])
    x2 = float(sys.argv[3])
    y2 = float(sys.argv[4])
    xy = float(sys.argv[5])
    n = float(sys.argv[6])

    sxx = findSXX(xi, x2, n)
    syy = findSYY(yi, y2, n)
    sxy = findSXY(xy, xi, yi, n)

    b1 = findB1(sxy, sxx)
    b0 = findB0(yi/n, b1, xi/n)

    sse = findSSE(syy, b1, sxy)

    rSQ = findRSq(sse, syy)

    eSTD = findEstStd(sse, sxx, n)

    print(f'Sxx = {sxx:.4f}')
    print(f'Syy = {syy:.4f}')
    print(f'Sxy = {sxy:.4f}')
    print('\n')
    print(f'yHat = {b0:.4f} + {b1:.4f}x')
    print(f'SSE = {sse:.4f}')
    print(f'R = {math.sqrt(rSQ):.4f}')
    print(f'R Squared = {rSQ:.4f}')
    print('\n')
    print(f'estimated standard deviation = {eSTD:.4f}')


# Main Execution
if __name__ == '__main__':
    main()
