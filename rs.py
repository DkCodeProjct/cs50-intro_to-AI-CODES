#rs == sum of squard residual
 
#d / d intercept rs = 
#(~ rs = -2*1.4 - (0 + 0.64 * 0.5) + -2*1.9 - (0 + 0.64 * 2.3) + -2*3.2 - (0 + 0.64 * 2.9)
#~ print('rs', rs)



yVal = [1.4, 1.9, 3.2]
xVal = [0.5, 2.3, 2.9]
slope = 0.64
intercept = 0
residual = 0
for y, x in zip(yVal, xVal):
    residual += -2 * (y - (intercept + slope * x))

print(round(residual, 2))