list=[1,2,3,4,5,1,3,5,7,9,2] #craeting list
print(list)
print("length of the list is : ",len(list)) #len(list) prints number  of elements in the list
print("-----------------------------------------------------")
list.append(9) #using append function we can add an element at last position
print("printing list by appending 9 using append function")
print(list) #printing list by appending 9 using append function
print("length of the list is : ",len(list))
print("-----------------------------------------------------")
list.insert(2,4)
print(list)
print("length of the list is : ",len(list))
print("-----------------------------------------------------")
list2=[10,12,14,15]
print(list2)
print("length of the list is : ",len(list2))
print("-----------------------------------------------------")
list.extend(list2)
print(list)
print("length of the list is : ",len(list)) #len(list) prints number  of elements in the list
print("-----------------------------------------------------")
print("using sum function adding all individual elements in the list ")
print("sum of list is {} and sum of list 2 is {}".format(sum(list),sum(list2)))
print("-----------------------------------------------------")
print("-----------------------------------------------------")
print("count occurence of particular element in the list")
print(list.count(1))#count occurence of particular element in the list
print("-----------------------------------------------------")
print("length of the list")
print(len(list))
print("-----------------------------------------------------")
print(list.index(1))#first occurence of element in the list
print("-----------------------------------------------------")
print(min(list))
print(max(list))
print("-----------------------------------------------------")
print(sorted(list))
print("-----------------------------------------------------")

print(list[::-1])
print("-----------------------------------------------------")
print(list.remove(1))
