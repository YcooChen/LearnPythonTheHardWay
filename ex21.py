def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACT %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLY %d * %d" % (a, b)
	return a * b
	
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
	
print "Lets do some math with just functions!"

a = float(raw_input("a = ?"))
b = float(raw_input("b = ?"))
c = float(raw_input("c = ?"))
d = float(raw_input("d = ?"))

age = add(a, 5)
height = subtract(b, 4)
weight = multiply(c, 2)
iq = divide(d, 2)

print "Age: %d, Height: %d, Weight: %d, Iq: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"