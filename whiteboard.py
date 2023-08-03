# ---------- Keep Hydrated ----------
# Nathan loves cycling. Because Nathan knows it is important to stay hydrated, he drinks 0.5 liters of water per hour of cycling. You get given the time in hours and you need to return the number of liters Nathan will drink, rounded to the smallest value.
# EXAMPLES:
# liters(2), --> 1
# liters(1.4) --> 0
# liters(12.3) --> 6
# liters(0.82) --> 0
import math

def litersDrank(hours):
    return math.floor(hours//2)

print(litersDrank(2))

hydration = lambda hours: int(hours//2)

print(hydration(2))