import string

letters = list(string.ascii_lowercase)
others = list(string.digits + string.punctuation)

def atbash(string):
    newstring = ""
    for char in string:
        if char in letters:
            for i in [i for i,x in enumerate(letters) if x == char]:
                newchar = letters[25-i]
                newstring += newchar
        else:
            for i in [i for i,x in enumerate(others) if x == char]:
                newchar = others[41-i]
                newstring += newchar
    print(newstring)
    
atbash("test")
