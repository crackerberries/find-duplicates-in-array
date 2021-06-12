# it's not code plagarism if you change the variable names

def findDuplicatesInArray(array):
    array.sort()
    print(array, "\n\n")
    for i in range(1, len(array)):
        if array[i] == array[i - 1]:
            print(array[i])


findDuplicatesInArray([2, 4, 3, 5, 6, 5, 7, 9, 8])