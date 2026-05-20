#P01
''''''''''''''''''''''
input_list = input("Enter elements of list separated by space: ").split()
l=len(input_list)
print("Last element of list", input_list[l-1])
'''''''''''''''''''''

#P02
''''''''''''''''''''''
input_list = input("Enter elements of list separated by space: ").split()
box = int(input("Enter group size: "))
print("Last group of list", input_list[-box:])
'''''''''''''''''''''

#P03
''''''''''''''''''''''
input_list = input("Enter elements of list separated by space: ").split()
k = int(input("Enter kth element to find: "))
flag = 0
for i in range(len(input_list)):
    if i == k-1:
        flag = 1
        print("kth element of list is", input_list[i])

if flag == 0:
    print("Element not found")
'''''''''''''''''''''

#P04
''''''''''''''''''''''
input_list = input("Enter elements of list separated by space: ").split()
l=len(input_list)
print("Length of list", l)
'''''''''''''''''''''

#P05
''''''''''''''''''''''
input_list = input("Enter elements of list separated by space: ").split()
l=len(input_list)
print("reversed List")
for i in range(l-1, -1, -1):
    print(input_list[i])
'''''''''''''''''''''

#P06
''''''''''''''''''''''
input_list = input("Enter elements of list separated by space: ").split()
l=len(input_list)
start = 0
end = l-1
flag = 1
while start != l:
    if input_list[start] != input_list[end]:
        flag = 0
        break
    start += 1
    end -= 1

if flag == 0:
    print("List is not palindrome")
else:    print("List is palindrome")
'''''''''''''''''''''

#P07

''''''''''''''''''''''
nested_list = eval(input("Enter a nested list: "))

def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))  # recursion
        else:
            flat_list.append(item)
    return flat_list

print("Flattened list:", flatten(nested_list))
'''''''''''''''''''''

#P08
'''''''''''''''''''''''
input_list = input("Enter elements of list separated by space: ").split()

i=0
while i < len(input_list)-1:
    if input_list[i] == input_list[i+1]:
        input_list.pop(i)
    else:       i += 1

print("List after removing consecutive duplicates:", input_list)
'''''''''''''''''''''''

#P09
'''''''''''''''''''''
input_list = input("Enter elements of list separated by space: ").split()
grouped_list = []
i=0
while i < len(input_list):   
    ele = input_list[i]
    bubble = []

    while i < len(input_list) and input_list[i] == ele:
        bubble.append(input_list[i])
        i += 1   

    grouped_list.append(bubble)


print("Grouped list:", grouped_list)
'''''''''''''''''''''

''''''''''''''''''''''
#Remove duplicate elements in list manually without using set() function
input_list = input("Enter elements of list separated by space: ").split()
copy_list = input_list.copy()
nondup_list = []

for ele in copy_list:
    if ele not in nondup_list:
        nondup_list.append(ele)
print("List after removing duplicates:", nondup_list)
'''''''''''''''''''''

'''''''''''''''''''''''''''
#P10

input_list = input("Enter elements of list separated by space: ").split()
grouped_list = []
i=0
while i < len(input_list):   
    ele = input_list[i]
    bubble = []

    while i < len(input_list) and input_list[i] == ele:
        bubble.append(input_list[i])
        i += 1   

    grouped_list.append(bubble)

print("Grouped list:", grouped_list)

final_list = []

for group in grouped_list:
    count = len(group)
    final_list.append([group[0], count])
    
print("Final list:", final_list)

'''''''''''''''''''''''''''''