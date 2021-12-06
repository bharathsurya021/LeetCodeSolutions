def subString(s):
    start = 0
    end = 0
    max_len = 0  #end-start+1
    mydict = {}
    for i in range(len(s)):
        if s[i] not in mydict:
            mydict[s[i]] = i
        else:
            # check if start of substring is less than current value of the char in dictionary before assigning occurrence of char
            # example in  'hello' start=0 but when l on index 3 occur we update start to 3+1 so that next substring starts from char 'O'
            if start < mydict[s[i]] + 1:
                start = mydict[s[i]] + 1
            mydict[s[i]] = i
        length = end - start + 1  # length includes end of string so the +1 in the eqn
        if length > max_len:
            max_len = length
        end += 1  # updating traverse status of string s
    return max_len


print(subString('hello'))