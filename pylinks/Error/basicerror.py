import os
print(os.getcwd())


try:
    file = open("code.txt", "r")
    datatypes = open("datatypes.txt", "r")
    keywords = open("keywords.txt", "r")

except FileNotFoundError:
    print("File not found :((")
    exit()

def check_datatypes(word):
    datatypes.seek(0)
    for dt in datatypes:
        if word==dt.strip():
            return True
    return False

def check_keywords(word):
    keywords.seek(0)
    for kw in keywords:
        if word==kw.strip():
            return True
    return False


def check_word(word):
    flag = check_datatypes(word)
    flag2 = check_keywords(word)
    if flag == True:
        print(f"{word} is a datatype so you cannot use it as a variable name")

    elif flag2 == True:
        print(f"{word} is a keyword so you cannot use it as a variable name")

    else:
        print(f"{word} is a Valid variable name")

#Brsainstorming how to detect semicolon is given after if condition or 
# if a == b:
# if a == b 
# if a == b'
#can't jump cursor to end of line becus a print statement in same line of condition is valid


content= file.read() + "\n"
word = ""

for ch in content:
    if ch!=" " and ch!="\n":
        word=word+ch
    else:
        check_word(word)
        word=""
