#list comprehension

# [expression for item in iterable if condition]
#expression → what you want to store in the list
#item → each element from the iterable (like list, range, string)
#condition (optional) → filter items


result = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
print(result)

matrix = [[i * j for j in range(3)] for i in range(3)]
print(matrix)

letters = [char.upper() for char in "python"]
print(letters)

#"For each item → apply something → optionally filter → store result in a list"