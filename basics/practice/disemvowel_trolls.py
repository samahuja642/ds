# Link :- https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python
def disemvowel(string_):
    newstring = ""
    for i in string_:
        if i!='a' and i!='A' and i!='e' and i!='E' and i!='i' and i!='I' and i!='o' and i!='O' and i!='u' and i!='U':
            newstring += i
    return newstring