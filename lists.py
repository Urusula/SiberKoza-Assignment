# A List is a collection which is ordered and changeable. Allows duplicate members.

#Create
numbers=[1,2,3,4,5]
numbers2=list((11,22,33,44,55))
fruits=["Elma","Armut","Portakal"]

print(numbers,numbers2)

#Get value
print(fruits[0])

#Get length
print(len(fruits))

#Append to list
fruits.append("Cilek")
print(fruits[3])

#Remove from list
fruits.remove("Elma")#Ýsmine göre siliyor
print(fruits)
fruits.pop(2)#Indextekini siliyor

#Insert into list
fruits.insert(0,"Watermelon")
print(fruits)

#Reverse list
fruits.reverse()
print(fruits)

#Sort list
fruits.sort()
print(fruits)

#Reverse sort
fruits.sort(reverse=True)
print(fruits)