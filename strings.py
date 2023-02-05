# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
name="Ahmet";
age=37;

#Concatenate
print("My name is",name,"and Im",age);

#Arguments by Position
print("My name is {x} and Im {y}".format(x=name,y=age));

#F-Strings
print(f"My name is {name} and Im {age}");

#String Formatting



#String Methods
string="hello world";
#Capitalize
string.capitalize();
#All upper
string.upper();
#All lower
string.lower();
#Swap case
print(string.swapcase());
#Replace
string.replace("world","madam");
#Count
sub = 'h'
string.count(sub)
#Starts with
string.startswith('hello');
#Ends with
string.endswith('d');
#Split into a list
string.split();
#Find position
string.find('r')
#Is all alphanumeric
string.isalnum();
#Is all alphabetic
string.isalpha();
#Is all numeric
string.isnumeric();
