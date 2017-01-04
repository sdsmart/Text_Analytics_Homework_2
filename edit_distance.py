# Name: Stephen Smart
# ID: 113851356

# Dynamic implementation of calculating edit distance between two strings
def distance(s1, s2):
    # Returning the trivial edit distance if one of the strings is empty
    if len(s1) == 0:
        return len(s2)
    elif len(s2) == 0:
        return len(s1)

    # Creating empty table (using a dictionary)
    table = {}

    # Filling first column
    for i in range(len(s1) + 1):
        table[i, 0] = i

    # Filling first row
    for j in range(len(s2) + 1):
        table[0, j] = j

    # Iterating through the table
    for j in range(1,len(s2) + 1):
        for i in range(1,len(s1) + 1):

            # Calculating costs for deletion, insertion, and change
            delete = table[i-1, j] + 1
            insert = table[i, j-1] + 1
            # The index of the current char in the string is actually
            # one char to the left of i / j due to the first row / col
            # in the table reserved for the empty string
            if s1[i-1] == s2[j-1]:
                change = table[i-1, j-1]
            else:
                change = table[i-1, j-1] + 1                

            # Setting current table value to be the min of the cost of
            # deletion, insertion, and change
            table[i, j] = min(delete, insert, change)

    # Returning result (bottom right element of table)
    return table[len(s1), len(s2)]
