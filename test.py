


from pickle import FALSE, TRUE


def solution(S):
    n=len(S)
    if n&1:
        return FALSE
    
    for i in range(int(n/2)):
        if S[i]!='a' or S[n-i-1]!='b':
            return FALSE
    
    for i in range(n):
        if (S[i] != 'a'):
            break

    if (i * 2 != n):
        return False
    for j in range(i, n):
        if (S[j] != 'b'):
            return False

    return TRUE        
           
if __name__ == "__main__":
    S = "aabbb"
    