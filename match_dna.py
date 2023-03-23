#Author:        Leul Adane
#Date:          October 5, 2021
#Purpose:       This program takes two DNA inputs and examines if they match with their complementary base; if not, it saves it as a mutation and then outputs the match, mutation, and its RNA complement.

import sys
len_str = 0
dna_sequence = input().upper()              # the .upper method conevrts all elemnts to uppercase.
dna_sequence2=input().upper()
dna = dna_sequence + dna_sequence2
dna = list(dna.split())
match = 0
mutuation = 0


if len(dna_sequence) == len(dna_sequence2):
  len_str = len(dna_sequence)              
elif len(dna_sequence) > len(dna_sequence2):
  len_str = len(dna_sequence2)
else:
  len_str = len(dna_sequence)

for i in dna_sequence:
    if (i == 'A') or (i == 'T') or (i == 'G') or (i =='C') or (i =='U'):
        continue
    
    else:
        sys.exit("Not DNA base")

for i in dna_sequence2:
    if (i == 'A') or (i == 'T') or (i == 'G') or (i =='C') or (i =='U'):
        continue
    
    else:
        sys.exit("You did not enter a DNA base")                                    #it terminates the program because the user did not input a DNA base

for i in range(len_str):
    if (dna_sequence[i] =='C') and (dna_sequence2[i]=='G'):
        match +=1                                                   #if the above condition is right, then it adds 1 to the match
    elif (dna_sequence[i]=='G') and (dna_sequence2[i]=='C'):
        match = match + 1 
    elif (dna_sequence[i]=='T') and (dna_sequence2[i]=='A'):
        match +=1
    elif (dna_sequence[i]=='A') and (dna_sequence2[i]=='T'):
        match +=1 
    else:
        mutuation += 1
        
print("match: " ,match)
print("mutuation: " ,mutuation)

rna_base = ''

index = 0
for i in range(len(dna_sequence)):                 
    if dna_sequence[index] == 'A':
        rna_base += 'U'                         #if the above condition is right it will add 'U' to the rna_base
        index += 1
        continue
    elif dna_sequence[index] == 'T':
        rna_base += 'A'
        index += 1
        continue
    elif dna_sequence[index] == 'G':
        rna_base += 'C'
        index += 1
        continue
    elif dna_sequence[index] == 'C':
        rna_base += 'G'
        index += 1
        continue
print('RNA Strand =', rna_base)

