# Enter your code here. Read input from STDIN. Print output to STDOUT

def coefficients(x, y):
    # Assume len(x) == len(y)
    
    compine = sumX = sumY = sumXX =0

    for i in range(len(x)):
        compine += x[i]*y[i]
        sumX += x[i]
        sumY += y[i]
        sumXX += x[i]*x[i]
    D = ((len(x)*sumXX)-sumX*sumX) 
    beta = ((len(x)*compine)-sumX*sumY)/D
    alpha = (sumXX*sumY - sumX*compine)/D

    return alpha,beta

P =  [15,  12,  8,   8,   7,   7,   7,   6,   5,   3]
H = [10,  25,  17,  11,  13,  17,  20,  13,  9,   15]

a , b = coefficients(P,H)

print(round(b*10+a,1))


