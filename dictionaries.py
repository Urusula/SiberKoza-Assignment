# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

#Create dictionary
person={
    "name":"Ahmet",
    "surname":"Secen",
    "age":21
}

print(person)

#Get value
print(person["name"])

#Add value
person["phone"]="123456"

#Get keys
print(person.keys())

#Get items
print(person.items())

#Copy dict
person2 = person.copy()
person2['city'] = 'Boston'

#Remove item
del(person['age'])
person.pop('phone')

#Clear
person.clear()

#Get length
print(len(person2))

#List of dict
people = [
    {'name': 'Enes', 'age': 25},
    {'name': 'Ebrar', 'age': 22}
]










# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

