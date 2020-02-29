def caculator():
	
	a = input("Hello Human:  ")
	b = input("What is your name:  ")
	c = input("Hello " + b + " ,how are you?  ")
	if c == "bad":
		d = input("What is wrong? ")
		print("Sorry for what happeneed")
		e = input("Can I cheer you up?  ")
		if e == "Yes":
			print(d)
		elif e == "No":
			print("I hope it does not happen next time.")
		
		
	elif c == "good":
		print("That is awsome")
		print("Let me make it better")
		
		
	elif c == "ok":
		print("That is good to hear")
		print("Let me make it better.")	

	d = input("I can do: A.addition B.subtraction C.multiplication D.division:  ")

	

	if d == "A":
		i = int(input("Please enter your first number:  "))
		j = int(input("Please input your second number:  "))
		k = i + j
		y = str(k) 
		print("Your answer is " + y)
		lx` = input("Do you want to try again:  ")
		if l == "Yes":
			print(d)
		elif l ==  "No":
			print("Bye")



	elif d == "B":  
		m = int(input("Please enter your first number: "))
		n = int(input("Please enter your second number: "))
		o = m - n
		z = str(o)
		print("Your answer is " + z)
		p = input("Do you want to try again:  ")
		if p == "Yes":
			print(d)
		elif p ==  "No":
			print("Bye")



	elif d == "C":
		q = int(input("Please enter your first number: "))
		r = int(input("Please enter your second number: "))
		s = q * r
		str1 = str(s)
		print("Your answer is " + str1)
		t = input("Do you want to try again:  ")
		if t == "Yes":
			print(d)
		elif t ==  "No":
			print("Bye")





	elif d == "D":
		u = int(input("Please enter your first number: "))
		v = int(input("Please enter your second number: "))
		w = u / v
		str2 = str(w)
		print("Your answer is " + str2)
		x = input("Do you want to try again:  ")
		if x == "Yes":
			print(d)
		elif x ==  "No":
			print("Bye")

caculator()



