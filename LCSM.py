def common_substring(strings):
    first_string = strings[0]
    for p in range(len(first_string), 0, -1):
        for x in range(len(first_string) - p + 1):
            substring = first_string[x:x + p]
            if all(substring in i for i in strings):
                return substring
    return ""
            
dna_strings = [
    "GATTACA", "TAGACCA", "ATACA"
]
print(common_substring(dna_strings))