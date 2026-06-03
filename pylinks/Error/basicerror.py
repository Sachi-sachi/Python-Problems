import os
print(os.getcwd())


try:
    file = open("code.txt", "r")

except FileNotFoundError:
    print("File not found :((")
    exit()


content= file.read() + "\n"
word = ""
for ch in content:
    if ch!=" " and ch!="\n":
        word=word+ch
    else:
        if word=="int":
            print(f"{word} is a keyword")
        else :
            print(f"{word} is a Valid variable name")
        word=""





