import string

def encode(s, sub):
    sub = fill(sub, len(s))
    alph = string.ascii_letters + string.punctuation + " "
    n = ""
    for i in range(0, len(s)):
        x = alph.index(s[i]) + alph.index(sub[i])
        if x >= len(alph):
            x = x - len(alph)
        n += alph[x]
    return n


def decode(s, sub):
    sub = fill(sub, len(s))
    alph = string.ascii_letters + string.punctuation + " "
    n = ""
    for i in range(0, len(s)):
        x = alph.index(s[i]) - alph.index(sub[i])
        if x >= len(alph):
            x = x - len(alph)
        n += alph[x]
    return n

    
def fill(s, l):
    c = 0
    while len(s) != l: 
        if len(s) > l:
            s = s[:-1]
            
        if len(s) < l:
            s += s[c]
            
        c += 1
    return s

print(encode("harry!", "te"))
print(decode("AeKvR%", "te"))
