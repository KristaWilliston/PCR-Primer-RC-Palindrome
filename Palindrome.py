# Write a program to test whether a PCR primer is a reverse complement
# palindrome.
#       Such a primer might fold and self-hybridize!
#       Test the program on at least the following primers:
#           TTGAGTAGACGCGTCTACTCAA
#           TTGAGTAGACGTCGTCTACTCAA
#           ATATATATATATATAT
#           ATCTATATATATGTAT
# palindrome = sequence that reads the same backward as forward

primer1 = 'TTGAGTAGACGCGTCTACTCAA'
primer2 = 'TTGAGTAGACGTCGTCTACTCAA'
primer3 = 'ATATATATATATATAT'
primer4 = 'ATCTATATATATGTAT'
# primer from HW3Q1
#HERC2 = 'TCGCCTCGACTCCAAATGG'
#HERC2reverse = 'TCTTTGTTCCACTTGGTTCGAC'

def complement(nuc):
    nucleotides = 'ACGT'
    complements = 'TGCA'
    i = nucleotides.find(nuc)
    if i >= 0:
        comp = complements[i]
    else:
        comp = nuc
    return comp

def reverseComplement(seq):
    seq = seq.upper()
    newseq = ""
    for nuc in seq:
        newseq = complement(nuc) + newseq
    return newseq

# check to see the reverse complements of the primers
# print("Reverse complement:", reverseComplement(primer1))
# print("Reverse complement:", reverseComplement(primer2))
# print("Reverse complement:", reverseComplement(primer3))
# print("Reverse complement:", reverseComplement(primer4))

# function to check if the primers are palindromes or not
def palindrome(seq):
    length = len(seq)//2 #divide length of sequence by 2
    if len(seq) % 2 == 0: #if the divided sequence is even, find the palindrome
        if seq[0:length] == reverseComplement(seq[length:]):
            return True
        else:
            return False
    else:                #if the divided sequence is odd, start from 1 position after the middle and exclude the very middle position
        if seq[0:length] == reverseComplement(seq[length+1:]):
            return True

print("Primer is palindrome", palindrome(primer1))
print("Primer is palindrome", palindrome(primer2))
print("Primer is palindrome", palindrome(primer3))
print("Primer is palindrome", palindrome(primer4))
#print("Primer is palindrome", palindrome(HERC2))
#print("Primer is palindrome", palindrome(HERC2reverse))
