sentence = "This is a sample sentence to extract words from."

word=""
for ch in sentence:
    if ch != " " and ch != "\n":
        word = word +ch
    else:
            print(word)
            word = "" 