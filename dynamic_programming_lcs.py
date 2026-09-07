'''write a function to find the length of the longest 
common subsequence between two sequence'''

def lcs_dp(seq1 , seq2):
    n1 , n2 = len(seq1) , len(seq2)

    table = [[0 for y in range(n2+1)] for x in range(n1+1)]

    for i in range(n1):
        for j in range(n2):
            if seq1[i] == seq2[j]:
                table[i+1][j+1] = 1 + table[i][j]

            else:
                table[i+1][j+1] = max(table[i+1][j] , table[i][j+1])

    return table[-1][-1]

seq1 = 'serendipitous'
seq2 = 'precipitation'
print(lcs_dp(seq1 , seq2))
