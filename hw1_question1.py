def trifeca(word):
    """
    Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
    """
    if len(word) < 1:
        return False
    else:
        letter = 0
        count = 0
        while letter < len(word)-1:
            if letter == len(word)-1:
                break
            elif word[letter] == word[letter + 1]:
                count += 1
            letter += 1
        if count >= 3:
            return True
        else:
            return False
        
print(trifeca('aawfpjrwwgn'))			
		