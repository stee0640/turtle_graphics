from math import radians, degrees, cos, acos, sqrt

def beregn_trekant(a, b, drej1):
    c = sqrt(a * a + b * b - 2 * a * b * cos(radians(180 - drej1)))
    drej2 = 180 - degrees(acos((b * b + c * c - a * a) / (2 * b * c)))
    return c, drej2