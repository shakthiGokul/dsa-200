def isValidSubsequence(array, sequence):
    seqIdx = 0
    for  num in array:
        if seqIdx <= len(sequence) and num == sequence[seqIdx]:
            seqIdx += 1
        if seqIdx == len(sequence):
            break    
    return len(sequence)  == seqIdx        
