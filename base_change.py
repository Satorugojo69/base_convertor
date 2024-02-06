fh = open('output.txt','w')

# convert base 2 to base 10
number = input("Enter the number in base 2: ")
fh.write("The number in base 2 is :" + str(number) + '\n')

answer = int(number, 2)
fh.write( "The number in base 10 is : "+ str(answer) + '\n')

#convert base 10 to base 2

a = int(input("Enter the number in base 10 :"))
fh.write( "The number in base 10 is : "+ str(a) + '\n')
b = bin(a)
fh.write("The number in base 2 is :" + b[2:] + '\n')

fh.close
