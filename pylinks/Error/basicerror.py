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

   # else:
       # print(f"{word} is a Valid variable name")

#Brsainstorming how to detect semicolon is given after if condition or 
# if a == b:
# if a == b 
# if a == b'
# if : a == b
# if a: #valid
# if a := b
# if a := b:
#can't jump cursor to end of line becus a print statement in same line of condition is valid

def check_semicolon(line, pos):
    line = line.strip()

    if line.startswith("if"):
        if ":" not in line:
            print(f"Missing ':' in line number {pos}")
        
        else: #check where if : is given after condition and not just anywhere in the line
            condition = line.split(":")
            condition = condition[0].strip()
            if condition == "if":
                print(f"Incomplete condition in line number {pos}")
            

content= file.read() + "\n"
line = ""
word = ""

file.seek(0)
content= file.read() + "\n"
linenumber=0
#extract line
for l in content:
    if l!="\n":
        line=line+l
    
    else:
        if line!="":
            linenumber+=1
            check_semicolon(line, linenumber)
            #extract word from line
            words=line.split(" ")
            for w in words:
                check_word(w)
        line=""
        