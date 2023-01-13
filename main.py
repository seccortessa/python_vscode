#  Don't change the code below 
two_digit_number = input("Type a two digit number: ")
#  Don't change the code above 

####################################
#Write your code below this line 👇
decena = int(int(two_digit_number) / 10)
unidad = int(two_digit_number) - 10*decena
print(unidad + decena)