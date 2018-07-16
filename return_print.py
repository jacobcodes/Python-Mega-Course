def converter(original_unit, coefficient=0.3048):
	return original_unit * coefficient

print(converter(10, 0.62))

## weather function
def convert_celsius(c):
	f = c * 9/5 + 32
	return f

## 
def string_length(mystring):
	if type(mystring) == int:
		return "Sorry, integers don't have length"
	If type(mystring) == float:
		return "Sorry, floats don't have length"
	else:
		return len(mystring)
## 

