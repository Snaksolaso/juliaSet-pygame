import math

def lowHighExp(iter):
    return math.pow(iter, (iter/255))


def lowHighExpFast(iter):
    return math.pow(2,(iter - 247.01))

def highLowLog(iter):
    return math.log(iter + 1)/math.log((iter+1)/262) + 255


def highLowHighQuadratic(iter):
    return math.pow((iter - 127.5), 2)/63.75 

def lowHighLowQuadratic(iter):
    return -highLowHighQuadratic(iter) + 255


def highLowInverse(iter):
    return 255/(iter + 1)

def linDown(iter,slope):
    return (-slope)*iter + 255