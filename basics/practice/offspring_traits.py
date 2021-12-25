# Link :- https://www.codewars.com/kata/5b011461de4c7f8d78000052/train/python
def all_same(bears):
    return bears[0]==bears[1]
def bear_fur(bears):
    if 'black' in bears and 'white' in bears:
        return 'grey'
    elif 'black' in bears and 'brown' in bears:
        return 'dark brown'
    elif 'brown' in bears and 'white' in bears:
        return 'light brown'
    elif all_same(bears):
        return bears[0]
    else:
        return 'unknown'