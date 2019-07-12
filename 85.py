number = int(input())
flag = number%2
if flag == 0:
    print(number, "is an even number")
elif flag == 1:
    print(number, "is an odd number")
else:
    print("Error, Invalid input")
