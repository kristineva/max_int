n = int(input("Enter the length of the sequence: ")) # Do not change this line
#næsta tala í röðinni er

first_number = 0
second_number = 1
third_number = 2
main_number = 0
num = 1

while num <= n:
    if num == 1:
        print(1)
        num += 1
    elif num == 2:
        print(2)
        num += 1
    elif num > 2 and num <= n:
        main_number = first_number + second_number + third_number
        print(main_number)
        first_number = second_number
        second_number = third_number
        third_number = main_number
        num += 1


 