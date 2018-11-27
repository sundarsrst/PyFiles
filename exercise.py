Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> my_name = ' Sundar Shrestha'
>>> my_age = 35 # it is a lie
>>> my_height = 167 #inches
>>> my_weight = 180 #lbs
>>> my_eyes = 'black'
>>> my_teeth = 'white'
>>> my_hair = 'black'
>>> 
>>> print "lets talk about %s." % my_name
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("lets talk about %s." % my_name)?
>>> print ("lets talk about %s." % my_name)
lets talk about  Sundar Shrestha.
>>> print("lets talk about%s." my_name)
SyntaxError: invalid syntax
>>> 
>>> print("lets talk about%s." %smy_name)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print("lets talk about%s." %smy_name)
NameError: name 'smy_name' is not defined
>>> print("lets talk about%s." %my_name)
lets talk about Sundar Shrestha.
>>> print ("He's %d inches tall." % my_height)
He's 167 inches tall.
>>> print ("He's %d inches tall.")
He's %d inches tall.
>>> print ("He's %d inches tall." my_height)
SyntaxError: invalid syntax
>>> print ("He's %d inches tall." % my_height)
He's 167 inches tall.
>>> print ("If i add %d, %d, and %d I get %d." my_age, my_weight, my_age + my_height + my_weight)
SyntaxError: invalid syntax
>>> print ("If i add %d, %d, and %d I get %d." %(my_age, my_weight, my_age + my_height + my_weight))
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print ("If i add %d, %d, and %d I get %d." %(my_age, my_weight, my_age + my_height + my_weight))
TypeError: not enough arguments for format string
>>> print ("If i add %d, %d, and %d I get %d." % my_age, % my_weight, % my_age + % my_height + % my_weight)
SyntaxError: invalid syntax
>>> print ("If i add %d, %d, and %d I get %d.") % my_age, % my_weight, % my_age + % my_height + % my_weight
SyntaxError: invalid syntax
>>> print ("If i add %d, %d, and %d I get %d.") %( my_age,  my_weight,  my_age + my_height +  my_weight)
If i add %d, %d, and %d I get %d.
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print ("If i add %d, %d, and %d I get %d.") %( my_age,  my_weight,  my_age + my_height +  my_weight)
TypeError: unsupported operand type(s) for %: 'NoneType' and 'tuple'
>>> print "If I add %d, %d, and %d I get %d." % ( my_age, my_height, my_weight, my_age + my_height + my_weight)
SyntaxError: invalid syntax
>>> 
>>> print ("hes got %s eyes and %s hair." %(my_eyes, my_hair))
hes got black eyes and black hair.
>>> print ("If I add %d, %d, and %d I get %d." % (
18 my_age, my_height, my_weight, my_age + my_height + my_weight))
SyntaxError: invalid syntax
>>> print ("If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))
If I add 35, 167, and 180 I get 382.
>>> print ("hii")



    
