import string, random

teststr = """According to a research team at Cambridge University, it doesn't matter in what order the letters in a word are, 
the only important thing is that the first and last letter be in the right place. 
The rest can be a total mess and you can still read it without a problem.
This is because the human mind does not read every letter by itself, but the word as a whole. 
Such a condition is appropriately called Typoglycemia."""

def typog(test):
    test = test.replace("\n", "").replace(".", " ").replace(",", " ")
    for word in test.split(" "):
        if len(word) > 3:
            middle = list(word[1:-1])
            random.shuffle(middle)
            print(word[0] + "".join(middle) + word[-1], end=" ")
        else:
            print(word,end=" ")
            

typog(teststr)
