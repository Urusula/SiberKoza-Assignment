# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

#Create Tuple
fruits=("Elma","Armut","Ayva")
print(fruits)

#Get Value
print(fruits[1])

#You cannot change the value as we do in lists
#fruits[0]="Cilek"

#Delete tuple
#del fruits

#Get length
print(len(fruits))



# A Set is a collection which is unordered and unindexed. No duplicate members.
#Ýkinci kez ayný eleman eklenemiyor.

#Create set
fruits_ats = {'Elma', 'Armut', 'Ayva'}

#Check the set
print('Elma' in fruits_set)

#Add to set
fruits_ats.add('Cilek')

#Remove from set
fruits_ats.remove('Ayva')

#Add duplicate
fruits_ats.add('Elma')

#Clear set
fruits_ats.clear()

#Delete
del fruits_set

print(fruits_set)

