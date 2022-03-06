import random
r = random.randint(1, 100)
count = 0
while True:
	count = count +1
	guess = input ('please input a guess number: ')
	guess = int(guess)
	if guess == r:
		print ('Correct!')
		print ('This is', count, 'times')
		break
	elif guess > r:
		print ('Your guess is larger than random')
	elif guess < r:
		print ('Your guess is smaller than random')
	print ('This is', count, 'times')





