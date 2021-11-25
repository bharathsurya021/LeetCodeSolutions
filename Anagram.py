def isAnagram(s, t):
    if len(s) != len(t):
        return False
    dict = {}
    dict1 = {}
    for i in range(len(s)):
        dict[s[i]] = 1 + dict.get(s[i], 0)
        dict1[t[i]] = 1 + dict1.get(t[i], 0)
    for letter in dict:
        if dict[letter] != dict1.get(letter):
            return False
    return True
