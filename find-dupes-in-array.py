# it's not code plagarism if you change the variable names

def findDuplicatesInArray(array):
    array.sort()
    print("sorted list:", array, "\n\n")
    for i in range(1, len(array)):
        if array[i] == array[i - 1]:
            print(array[i])

input_string = input('enter the array of numbers: ')
user_list = input_string.split()
print('list:', user_list)
for i in range(len(user_list)):
    user_list[i] = int(user_list[i])

findDuplicatesInArray(user_list)