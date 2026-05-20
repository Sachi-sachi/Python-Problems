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

