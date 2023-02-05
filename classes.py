# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:

  # Constructor
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
    
    # Adding Encapsulation of variables... Encapsulation is the concept of making the variables non-accessible or accessible upto some extent from the child classes
    self._private = 1000 # Encapsulated variables are declares with '_' in the constructor.

  def greeting(self):
      return f'My name is {self.name} and I am {self.age}'

  def has_birthday(self):
      self.age += 1
 
 #function for encap variable
  def print_encap(self):
      print(self._private)

# Extend class
class Customer(User):
  # Constructor
  def __init__(self, name, email, age):
      User.__init__(self, name, email, age) #Called proper parent class constructor to make this as proper child inehriting all methods.
      self.name = name
      self.email = email
      self.age = age
      self.balance = 0

  def set_balance(self, balance):
      self.balance = balance

  def greeting(self):
      return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

#  Init user object
Ahmet = User('Ahmet Secen', 'ahmedsecen@gmail.com', 37)
# Init customer object
Esat = Customer('Esat Yilmaz', 'esatyilmaz@gmail.com', 25)

Esat.set_balance(500)
print(Esat.greeting())

Ahmet.has_birthday()
print(Ahmet.greeting())

#Encapsulation -->
Ahmet.print_encap()
Ahmet._private = 800 #Changing for brad
Ahmet.print_encap()

# Method inherited from parent
Esat.print_encap() #Changing the variable for brad doesn't affect janets variable --> Encapsulation
Esat._private = 600
Esat.print_encap()

#Similary changing janet's doesn't affect brad's variable.
Ahmet.print_encap()

