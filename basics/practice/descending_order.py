# Link :- https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python
num = int(input("Enter a Number : "))
def descending_order(num):
    digits = []
    while num > 0:
        digits.append((int)(num%10))
        num = num//10
    mul = 1
    digits.sort()
    for i in digits:
        num += (int)(i*mul)
        mul *= 10
    return num
def do2(num):
    digits = str(num)
    digits = list(digits)
    digits.sort()
    digits.reverse()
    digits = ''.join(digits)
    return int(digits)
print("Greatest Number:" ,do2(num))