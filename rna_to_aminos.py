#Author:            November 2, 2021
#Date:              Leul Adane
#Purpose:           This program takes a mRNA string as an input and outputs a string of amino acids.  


def get_encode_protein(mRNA):
    
    codon_dic = {
		'UUU': 'Phe', 'CUU': 'Leu', 'AUU': 'Ile', 'GUU': 'Val',
		'UUC': 'Phe', 'CUC': 'Leu', 'AUC': 'Ile', 'GUC': 'Val',
                'UUA': 'Leu', 'CUA': 'Leu', 'AUA': 'Ile', 'GUA': 'Val',
                'UUG': 'Leu', 'CUG': 'Leu', 'AUG': 'Met', 'GUG': 'Val',
                
                'UCU': 'Ser', 'CCU': 'Pro', 'ACU': 'Thr', 'GCU': 'Ala',
                'UCC': 'Ser', 'CCC': 'Pro', 'ACC': 'Thr', 'GCC': 'Ala',
                'UCA': 'Ser', 'CCA': 'Pro', 'ACA': 'Thr', 'GCA': 'Ala',
                'UCG': 'Ser', 'CCG': 'Pro', 'ACG': 'Thr', 'GCG': 'Ala',

                'UAU': 'Tyr', 'CAU': 'His', 'AAU': 'Asn', 'GAU': 'Asp',
                'UAC': 'Tyr', 'CAC': 'His', 'AAC': 'Asn', 'GAC': 'Asp',
                'UAA': 'Stop', 'CAA': 'Gin', 'AAA': 'Lys', 'GAA': 'Glu',
                'UAG': 'Stop', 'CAG': 'Gin', 'AAG': 'Lys', 'GAG': 'Glu',

                'UGU': 'Cys', 'CGU': 'Arg', 'AGU': 'Ser', 'GGU': 'Gly',
                'UGC': 'Cys', 'CGC': 'Arg', 'AGC': 'Ser', 'GGC': 'Gly',
                'UGA': 'Stop', 'CGA': 'Arg', 'AGA': 'Arg', 'GGA': 'Gly',
                'UGG': 'Trp', 'CGG': 'Arg', 'AGG': 'Arg', 'GGG': 'Gly',
                }
   
    
    codon_dic_set = set(codon_dic)     # converts the dictionary to set
    inter = set(mRNA).intersection(codon_dic_set)     #both mrNA and Dic are set, the intersection method outputs the value that are both in DIC and mRNA 
    list(inter)                                       #converts back to list, becuase list is ordered (Using a set might mess up the position)
    list(mRNA)                                        #converts back to list, becuase list is ordered (Using a set might mess up the position)
    protein = ''
    codon_count = 0
    for i in mRNA:
    
        if i in inter:
          
          if codon_count < (len(mRNA)-1):
              protein += (codon_dic[i] + ' - ')
              codon_count +=1
          else:
              protein += codon_dic[i]
    return protein

def slice(strg, num=3):             #this function slice the string into 3
    return [ strg[start:start+num] for start in range(0, len(strg), num)]        # takes in the string from the mrna input and slice is with the given value of number
                           #the end is always greater than the start by num, and start is in range the length of the string with stride value of num

#############################################################################

mRNA = input('Enter mRNA ').upper()                          #takes in input for the mRNA and converts it into Upper case letter


sliced_mrna = slice(mRNA)         #paasing the input to the slice function


protein = get_encode_protein((sliced_mrna))

print(protein)
        





