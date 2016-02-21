#Write a program that print numbers from 1 to 100. BUT
#for multiples of three use "Fizz" instead of the number
#for multiples of five use "Buzz" instead of the number
#for numbers which are multibles of both three and five print "FizzBUzz"

#first print 1-100
for i in range(1,101):
	if i %3 ==0 and i%5==0:
		print "FizzBuzz"
	elif i %5 == 0:
		print "Buzz"
	elif i %3 ==0 :
		print "Fizz"
	else:
		print i
#one liner:
for i in range(1,101):print ("fizz"*(i%3==0)+"Buzz"*(i%5==0) or i)
