# Link :- https://www.codewars.com/kata/5500d54c2ebe0a8e8a0003fd/train/python
def mygcd(x, y):
    if x==0:
        return y
    return mygcd(y%x,x)