# Link :- https://www.codewars.com/kata/5b049d57de4c7f6a6c0001d7/train/python
def apparently(string):
    ls = (string.split(' '))
    li = ls[:]
    var = 0
    for i in range(len(ls)):
        if ls[i]=='and' and (i+1==len(ls) or ls[i+1]!='apparently') or ls[i]=='but' and (i+1==len(ls) or ls[i+1]!='apparently'):
            li.insert(i+1+var,'apparently')
            var+=1
    string = ' '.join(li)
    return string


# def apparently2(string):
#     st = string[:]
#     var = 0
#     for i in range(len(string)):
#         if string[i:i+14:1]=='and apparently' or string[i:i+14:1]=='but apparently':
#             continue
#         elif string[i:i+5:1]==' and ' or string[i:i+5:1]==' but ':
#             st = st[:i+3+var:]+' apparently'+st[i+3+var::]
#             var+=11
#     return st
string = "apparently and and and"
print(apparently(string))
