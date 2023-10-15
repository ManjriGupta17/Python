fruits = ["Apple","Mango","Grapes","Banana"]#create a list
print(fruits)#print a list

print(type(fruits))#check type of list

print(len(fruits))#check length of list

#checking if item is present in the list
if "Banana" in fruits:
    print("Banana is the part of list")
##checking if item is present in the list
if "Kiwi" not in fruits:
    print("Kiwi is not the part of list")

#indexxing in list
print(fruits[1])#Mango
print(fruits[-3])

print(fruits[1:3])
print(fruits[-3:-1])

#adding elements to a list
fruits.append("Kiwi")
print(fruits)

fruits.insert(2,"Cherry")
print(fruits)

more_fruits = ["Watermelon","Papaya"]
fruits.extend(more_fruits)
print(fruits)


#removing elements from the list
fruits.remove("Banana")
print(fruits)

fruits.pop(3)
print(fruits)

#changing and updating itms in a list
fruits[1] = "Orange"
print(fruits)

fruits[1:3] = ["Pineapple"]
print(fruits)

#sorting a list
fruits.sort()#ascending 
fruits.sort(reverse=True)#descending
print(fruits)

#reverse
fruits.reverse()
print(fruits)

#LIST COMPREHENSION
new_fruits = [fruit for fruit in fruits if "a" in fruit]
print(new_fruits)

#copy a list
new_fruits = fruits.copy()
print(new_fruits)

new_fruits = fruits + new_fruits 
print(new_fruits)

#Nested lists
fruits.insert(2, ["Cucumber","Coconut"])
print(fruits)
print(fruits[2][1])