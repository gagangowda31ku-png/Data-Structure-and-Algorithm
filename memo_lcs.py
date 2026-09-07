'''write a function to find the length of the longest
 common subsequence between two sequence'''


def lcs_memo(seq1 , seq2):
    memo = {}

    def recursive(ind1=0, ind2 = 0):
        key = (ind1 , ind2)
        if key in memo:
            return memo[key]

        elif ind1 == len(seq1) or ind2 == len(seq2):
            memo[key] =0

        elif seq1[ind1] == seq2[ind2]:
            memo[key] = 1 + recursive(ind1+1 , ind2+1)

        else:
            memo[key] = max(recursive(ind1+1 ,ind2), recursive(ind1 , ind2+1))
        return memo[key]

    return recursive(0,0)

seq1 = 'serendipitous'
seq2 = 'precipitation'
print(lcs_memo(seq1 , seq2))
