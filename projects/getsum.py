def getsum(n):
    summing = 0
    for digit in str(n):
        summing += int(digit)
    return summing

n = 12345
print(getsum(n))