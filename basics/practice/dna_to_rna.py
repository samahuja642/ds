# Link :- https://www.codewars.com/kata/5556282156230d0e5e000089/train/python
def dna_to_rna(dna):
    string = ''
    for i in dna:
        if i=='T':
            string += 'U'
        else:
            string += i
    return string