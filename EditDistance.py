
# function to calculate edit distance between two strings
def min_edit_distance(s1, s2):
    m = len(s1)
    n = len(s2)

    # Initialize the distance matrix
    d = [[0 for j in range(n+1)] for i in range(m+1)]

    # Initialize the first row and column
    for i in range(1, m+1):
        d[i][0] = i
    for j in range(1, n+1):
        d[0][j] = j

    # Fill in the rest of the matrix
    for j in range(1, n+1):
        for i in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = min(d[i-1][j] + 1,  # Deletion
                              d[i][j-1] + 1,  # Insertion
                              d[i-1][j-1] + 2)  # Substitution

    # Return the minimum edit distance
    return d[m][n]


# function to find the closest match for a given string
def get_minimum_edit_distance_word(input_word, word_pool):
    min_distance = float('inf')
    min_word = None

    for word in word_pool:
        distance = min_edit_distance(input_word, word)
        if distance < min_distance:
            min_distance = distance
            min_word = word

    return min_word


def convert_to_lower(words):
    lower_words = []
    for word in words:
        lower_words.append(word.lower())

    return lower_words