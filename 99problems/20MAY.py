#P19
'''''''''''''''''''''''''''
input_list = input("Enter elements of list separated by space: ").split()
num = int(input("Enter the number of positions to rotate (- for left, unsigned for right): "))
first_part = []
second_part = []
combined_list = []
N=num
num=abs(num)

if N > 0:
    for i in range(len(input_list)):
            if i < num:
                 first_part.append(input_list[i])
            else:
                 second_part.append(input_list[i])

    combined_list.append(second_part)
    combined_list.append(first_part)
    
elif N < 0:
    for i in range(len(input_list)):
            if i < len(input_list) - num:
                 first_part.append(input_list[i])
            else:
                 second_part.append(input_list[i])

    combined_list.append(second_part)
    combined_list.append(first_part)
elif N == 0:
     combined_list.append(input_list)

for i in combined_list:
    for j in i:
        print(j, end=" ")
'''''''''''''''''''''''''''

#P20
'''''''''''''''''''''''''''
input_list = input("Enter elements of list separated by space: ").split()
pos = int(input("Enter the position to remove element: "))

for i in range(len(input_list)):
    if i == (pos-1):
        input_list.pop(i)
        break

for i in input_list:
    print(i, end=" ")
'''''''''''''''''''''''''''

#P21
'''''''''''''''''''''''''''
input_list = input("Enter elements of list separated by space: ").split()
pos = int(input("Enter the position to insert element: "))
final_list = []

for i in range(len(input_list)):
    final_list.append(input_list[i])
    if i == (pos-2):
        ele = input("Enter the element to insert: ")
        final_list.append(ele)

for i in final_list:
    print(i, end=" ")
'''''''''''''''''''''''''''

#P22
'''''''''''''''''''''''''''
a=int(input("Enter first limit: "))
b=int(input("Enter second limit: "))

if a > b:
    for i in range(a, b + 1, -1):
        print(i, end=" ")
elif a < b:
    for i in range(a, b + 1):
        print(i, end=" ")
'''''''''''''''''''''''''''

#P23
'''''''''''''''''''''''''''
import random

input_list = input("Enter elements of list separated by space: ").split()
num= int(input("Enter the number of random elements to select: "))
final_list = []
n= random.randint(0, len(input_list)-num)
i=0
while i < num:
    print(input_list[n+i], end=" ")
    i+=1
   
 '''''''''''''''''''''''''''

#P24
'''''''''''''''''''''''''''
import random
M=int(input("Give maximum limit: "))
num=int(input("Enter number of random elements to generate: "))

rand_list=[]
for i in range(num):
    rand_list.append(random.randint(1, M))

print(rand_list)

'''''''''''''''''''''''''''

#P25
'''''''''''''''''''''''''''
#i couldnt solve this on my own so i looked up the solution and implemented it here
input_list = input("Enter elements of list separated by space: ").split()

def generate_permutations(input_list):
    if len(input_list) == 0:
        return [[]]

    result = []
    for i in range(len(input_list)):
        current = input_list[i]
        remaining = input_list[:i] + input_list[i+1:]

        for p in generate_permutations(remaining):
            result.append([current] + p)

    return result


print(generate_permutations(input_list))
'''''''''''''''''''''''''''



