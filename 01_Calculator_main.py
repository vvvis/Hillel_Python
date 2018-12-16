print ('''
	-------------------------------------
	|                                   |
	|   Welcome to basic calculator!    |
	|Please, provide your math operation|
	|                                   |
	-------------------------------------
	''')
while True:
	user_input1 = float(input('Operand1:'))
	user_input2 = float(input('Operand2:'))
	operator = input('Operator:')
	if user_input1 == 'exit':break
	if operator == "+":
		print (user_input1 + user_input2)
	elif operator == "-":
		print (user_input1 - user_input2)
	elif operator == "/":
		print (user_input1 / user_input2)
	elif operator == "*":
		print (user_input1 * user_input2)