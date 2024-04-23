def check_panagram(sentence):
    """
    Given a sentence 
    Return True if a sentence is a panagram, or False otherwise
    A panagram is a sentence consisting of all the letters of the English Alphabet
    """
    return len(set(sentence)) == 26

sentence = "thequickbrownfoxjumpsoverthelazydog"
print(check_panagram(sentence))
