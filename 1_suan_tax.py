def taxes():
	while True:
		weekly_salary = input("Please enter your weekly salary (integer): ")
		try:
			weekly_salary = int(weekly_salary) #for more accuracy replace int() by float()
			break
		except:
			print('Please enter a valid number.')

	if weekly_salary < 10 and weekly_salary >= 0:
		print(f"You owe 0$\nYour balance is {weekly_salary}$")

	elif weekly_salary >= 10:
		taxed_money = weekly_salary - 10
		owed_money = 0.25 * taxed_money
		after_tax = weekly_salary - owed_money
		print(f'You owe: {round(owed_money)}$\nYour balance is: {round(after_tax)}$') #for more accuracy remove the round()

	else:
		print("How is your salary negative?")
		#taxes() i commented this in case if you wanted the user to re-input smth if they were in debt

taxes()