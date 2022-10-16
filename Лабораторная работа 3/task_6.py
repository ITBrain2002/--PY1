list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
k=list_numbers[0]
c=0
for i in range(len(list_numbers)):
    if k<= list_numbers[i]:
        k=list_numbers[i]
        c=i
list_numbers[c], list_numbers[-1] = list_numbers[-1] , list_numbers[c]

print(list_numbers)
