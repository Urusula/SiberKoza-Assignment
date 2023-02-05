# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

#Create function
def sayhello(name):
    print("Hello",name)

sayhello("Ahmet")

#Return values
def sum(num1,num2):
    total=num1+num2
    return total

print(sum(5,2))


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getsum=lambda num1,num2:num1+num2
print(getsum(6,2))


