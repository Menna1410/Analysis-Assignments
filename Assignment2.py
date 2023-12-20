def sequence_alignment(x, y, scoring_matrix):
    n = len(x)
    m = len(y)

    dpMatrix = [[0] * (m + 1) for _ in range(n + 1)]

    i = 1
    while i <= n:
        j = 1
        while j <= m:
            match = dpMatrix[i - 1][j - 1] + scoring_matrix[x[i - 1]][y[j - 1]]
            delete = dpMatrix[i - 1][j] + scoring_matrix[x[i - 1]]["-"]
            insert = dpMatrix[i][j - 1] + scoring_matrix["-"][y[j - 1]]

            dpMatrix[i][j] = max(match, delete, insert)

            j += 1
        i += 1

    alignedX = ""
    alignedY = ""
    i, j = n, m
    while i > 0 or j > 0:
        if i > 0 and j > 0 and dpMatrix[i][j] == dpMatrix[i - 1][j - 1] + scoring_matrix[x[i - 1]][y[j - 1]]:
            alignedX = x[i - 1] + alignedX
            alignedY = y[j - 1] + alignedY
            i -= 1
            j -= 1
        elif i > 0 and dpMatrix[i][j] == dpMatrix[i - 1][j] + scoring_matrix[x[i - 1]]["-"]:
            alignedX = x[i - 1] + alignedX
            alignedY = "-" + alignedY
            i -= 1
        else:
            alignedX = "-" + alignedX
            alignedY = y[j - 1] + alignedY
            j -= 1

    return alignedX, alignedY, dpMatrix[n][m]

x = "TCCCAGTTATGTCAGGGGACACGAGCATGCAGAGAC"
y = "AATTGCCGCCGTCGTTTTCAGCAGTTATGTCAGATC"

scoring_matrix = {
    'A': {'A': 1, 'G': -0.8, 'T': -0.2, 'C': -2.3, '-': -0.6},
    'G': {'A': -0.8, 'G': 1, 'T': -1.1, 'C': -0.7, '-': -1.5},
    'T': {'A': -0.2, 'G': -1.1, 'T': 1, 'C': -0.5, '-': -0.9},
    'C': {'A': -2.3, 'G': -0.7, 'T': -0.5, 'C': 1, '-': -1},
    '-': {'A': -0.6, 'G': -1.5, 'T': -0.9, 'C': -1, '-': float('-inf')}
}

result = sequence_alignment(x, y, scoring_matrix)

alignedX, alignedY, score = result
print(f"Aligned X: {alignedX}")
print(f"Aligned Y: {alignedY}")
print(f"Alignment Score: {score}")
