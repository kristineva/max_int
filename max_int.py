num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
#num_int er ekki mínus tala
# ef num er stærra en max þá verður num að max
# max á að prentast út þegar mínus tala er stimpluð inn
max_int = 0
while num_int >= 0:
    if num_int > max_int:
        max_int = num_int
    num_int = int(input("Input a number: "))

Print("The maximum is", max_int)    # Do not change this line
