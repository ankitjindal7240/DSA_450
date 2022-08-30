def middle(self, A, B, C):
    if A < B:
        return B if B < C else max(A, C)
    return A if A < C else max(B, C)
