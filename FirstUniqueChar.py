def unique(string):
    hashset = {}
    for i in range(len(string)):
        if string[i] not in hashset:
            hashset[string[i]] = 1
        else:
            hashset[string[i]] += 1
    for i in range(len(string)):
        if hashset[string[i]] == 1:
            return i
    return -1


string = 'leetcode'
print(unique(string))
