# Enter your code here. Read input from STDIN. Print output to STDOUT]


def slope(x, y):
    # Assume len(x) == len(y)
    n = len(x)
    compine = sumX = sumY = sumXX =0

    for i in range(len(x)):
        compine += x[i]*y[i]
        sumX += x[i]
        sumY += y[i]
        sumXX += x[i]*x[i]
    return ((len(x)*compine)-sumX*sumY)/((len(x)*sumXX)-sumX*sumX) 

l1 =  [15,  12,  8,   8,   7,   7,   7,   6,   5,   3]
l2 = [10,  25,  17,  11,  13,  17,  20,  13,  9,   15]

print(round(slope(l1, l2),3))

