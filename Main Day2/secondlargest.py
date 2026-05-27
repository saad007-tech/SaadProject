number=[10,20,30,40,80]
second_largest=number[0]
largest=number[0]
for num in number:
    if num > largest:
        second_largest = largest
        largest=num
    elif num !=largest and num > second_largest:
        second_largest = num 
print("largest number is:", largest)
print("second largest number is:", second_largest)