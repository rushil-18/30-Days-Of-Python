#List is a data structure in python where it can store multiple data types. 
#can be created by list() function or []
#mutable - can be changed 

empty_list = list()

first_list = ["rushil", 19, 50000, 'banana', 'oats']
#indexing - 0,1,2,3....

print(first_list[0]) # rushil 
print(first_list[0:2]) #rushil, 19 (n-1) happens
print(first_list[0:]) #first to last 
print(first_list[0:4:1] 

#insert, append, extend, remove, pop , reverse , sort , index
appended = first_list.append('single')
inserted = first_list.insert(0,"moota")
removed = first_list.remove('moota)
poped = first_list.pop()
poped = first_list
second_list = ["hi", "hello" "welcome"]
extended = first_list.extend(second_list)
sorted = first_list.sort() # alphabatically and numerically - ascending
first_list.sort(reverse = True) 

#function for sort - sorted()
sorted =sorted(first_list)
#finding methods 
print("art" in first_list) #false 
print(first_list.index('rushil'))

for i in first_list :
    print(i) #ittered list 

for index, lists in enumerate(first_list, start= 1):
    print(index, lists)
    
joined = '-'.join(first_list) # "rushil"-19-50000


