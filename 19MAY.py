
#P11
'''''''''''''''''''''''''''''
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

#print("Grouped list:", grouped_list)

final_list = []

for group in grouped_list:
    count = len(group)
    if count == 1:
        final_list.append(group[0])
    else:
        final_list.append([group[0], count])

print("Final list:", final_list)
'''''''''''''''''''''''''''''''''''

#P12
'''''''''''''''''''''''''''
nested_list = eval(input("Enter a nested list: "))

decoded_list = []
flat_list = []
#first flattening the list

for sublist in nested_list:
    flat_list.extend(sublist)

#print("Flattened list:", flat_list)

for ele in flat_list:
    if isinstance(ele, int) == True:
        pos = flat_list.index(ele)
       # print("Position of", ele, "is", pos)
        for i in range(ele-1):
            decoded_list.append(flat_list[pos-1])
    else:
        decoded_list.append(ele)

print("Decoded list:", decoded_list)
'''''''''''''''''''''

#P13
'''''''''''''''''''''''''''''
#no grouping of consecutive elements, just counting the frequency of each element in the list
input_list = input("Enter elements of list separated by space: ").split()
final_list = []
count=1
i=0
for i in range(len(input_list)-1):
    ele = input_list[i]
    if ele == input_list[i+1]:
        count+=1
    else:
        if count > 1:
            final_list.append((count, ele))
        else:
            final_list.append(ele)
        count = 1

if count > 1:
    final_list.append((count, input_list[-1]))
else:
    final_list.append(input_list[-1])


print("Final list:", final_list)
        
'''''''''''''''''''''

#P14
'''''''''''''''''''''
input_list = input("Enter elements of list separated by space: ").split()

double_list = []

i=0
while i<len(input_list):
    ele=input_list[i]
    double_list.append(ele)
    double_list.append(ele)
    i += 1

print("Double list:", double_list)
'''''''''''''''''
        
#P15
''''''''''''''''''''''
input_list = input("Enter elements of list separated by space: ").split()
num = int(input("Enter the number of times to repeat element: "))
final_list = []

i=0
while i<len(input_list):
    ele=input_list[i]
    for j in range(num):
        final_list.append(ele)
    i += 1

print("Double list:", final_list)
'''''''''''''''''''''''

#P16
''''''''''''''''''''''
input_list = input("Enter elements of list separated by space: ").split()
num = int(input("Enter the position to remove: "))
final_list = []
l=len(input_list)
for i in range(l):
    if (i+1)%num != 0:
        final_list.append(input_list[i])

print("Final list:", final_list)
'''''''''''''''''''''''

#P17
'''''''''''''''''''''''''''''''''''
input_list = input("Enter elements of list separated by space: ").split()
end = int(input("Enter the position to split: "))
first_part = []
second_part = []
combined_list = []
for i in range(len(input_list)):
    if i < end:
        first_part.append(input_list[i])
    else:
        second_part.append(input_list[i])

combined_list.append(first_part)
combined_list.append(second_part)

print("Combined list:", combined_list)
'''''''''''''''''''''''''''''''''''''''''''''''''''''

#P18

'''''''''''''''''''''''''''''''''''
input_list = input("Enter elements of list separated by space: ").split()
i = int(input("Enter I (start limit): "))
k = int(input("Enter K (end limit): "))

sliced_list = []
for ele in range(i-1,k):
    sliced_list.append(input_list[ele])

print("Sliced list:", sliced_list)
'''''''''''''''''''''''''''''''''''''''''''''''''''''
