file = open("text.py", "w")

file.write("This is a line of text.\n")
file.close()

# creating a list

list1= ["apple", "banana", "cherry"]
print(list1)

#converting list to json
import json

json_string = json.dumps(list1)
print(json_string)