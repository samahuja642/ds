# Link :- https://www.codewars.com/kata/541c8630095125aba6000c00/train/python
def digital_root(n):
    if n<10:
        return n
    sum = 0
    while n>0:
        sum += (int)(n%10)
        n = n//10
    return digital_root(sum)
print(digital_root(18))