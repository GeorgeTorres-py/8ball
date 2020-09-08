import sys, random

ans = True

while ans:
	question = input('Ask the magic ball anything: ')

	answers = random.randint(-1, 10)

	if question == '':
		sys.exit()

	elif answers == 1:
		print('Most Definitly!')

	elif answers == 2:
		print('Highly Doubtful!')

	elif answers == 3:
		print('Absolutly')

	elif answers == 4:
		print('Absolutly Not!')

	elif answers == 5:
		print('Maybe')

	elif answers == 6:
		print('Not Probable')

	elif answers == 7:
		print('It\'s Likly!')

	elif answers == 8:
		print('You should ask again')

	elif answers == 9:
		print('Dont count on it')

	elif answers == 10:
		print('I\'d bet on it!')
