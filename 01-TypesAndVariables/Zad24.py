#Square root calculation

import math
x = 170 * 0.032808
z = math.modf(x)
print("Mam 170 cm wzrostu, tj. " + format(int(x)) + " stóp i " + format(int(z[0] * 10)) + " cali")