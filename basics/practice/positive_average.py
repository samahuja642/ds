# Link :- https://www.codewars.com/kata/59f4a0acbee84576800000af/train/python
def count_pos(s1,s2):
    ct = 0
    for i in range(len(s1)):
        if(s1[i]==s2[i]):
            ct+=1
    return ct
def pos_average(s):
    temp = s.split(', ')
    count = 0
    length = len(temp[0])
    for i in range(len(temp)):
        for j in range(len(temp)):
            if i!=j:
                count += count_pos(temp[i],temp[j])
    n = (len(temp))*(len(temp)-1)/2
    count = count/2
    return (count/(n*length))*100
print(pos_average("6900690040, 4690606946, 9990494604"))