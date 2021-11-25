def canConstruct(ransomNote, magazine):
    firstHash = {}
    for i in range(len(magazine)):
        if magazine[i] not in firstHash:
            firstHash[magazine[i]] = 1
        else:
            firstHash[magazine[i]] += 1
    for letter in ransomNote:
        if letter not in firstHash:
            return False
        if firstHash[letter] <= 0:
            return False
        firstHash[letter] -= 1
    return True