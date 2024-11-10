
##List

##How do you create a list in Python?

#Put [] brackets around it.

print([1,2,3,4,5,6])

##How do you add an element to the end of a list?

#use .append in code.

i = ["python","java","c"]
i.append("c++")
print(i)

##How do you insert an element at a specific position in a list?

#Use insert function

i.insert(3,"scratch")

print(i)

##How do you remove an element from a list by its value?

# Using remove() function

i.remove("c")

print(i)

##How do you remove an element from a list by its index?

#Use remove() finction, using [] to state the index of a variable

i.remove(i[1])

print(i)



##How do you find the length of a list?

# Using the len() function

print(len(i))

##How can you check if an item exists in a list?

#use count() and a if statement to identify 

if i.count("java") == 0:
    print("Does not exist")
else:
    print("Exists")



##How do you sort a list in ascending order?

# using the sort() function

j = [87,90,96,7,47]

print(sorted(j))
    
##How do you reverse a list?

#use reverse() function

j.reverse()

print(j)
##What is list comprehension? Give an example.

# Uses a shorter code when you want a new list from a previous list
geos= ["UK", "India", "SriLanka", "Senegal", "Egypt"]
graphy= [i for i in geos if "a" in i]
print(graphy)

##How do you create a string in Python?

#Put "" around it. Input from user is also automatically a string

ssring = "hello world"


##How do you access the first character of a string?

#Use [] to enter index 0 nd

print(ssring[0])

##How do you find the length of a string?

#Use len() function

print(len(ssring))
##How can you check if a substring exists within a string?

subsstring = "bruh"

if subsstring in ssring:
    print("Exists")
else:
    print("Does not exist")

##How do you convert a string to uppercase?

#Use s.upper function toreturn string in uppercase

capssring = ssring.upper()

print(capssring)


#level 2

##1. **Shopping List Manager**: Write a program to manage a shopping list. Allow the user to add items, remove items, and view the list.

shop = []
ans = ""

stop = "stop"
while ans != stop:
    ans = input("Pick a option: A to add item, R to remove item, V to view shopping list: ")
    if ans == "A":
        Ashop = input("What item do you want to add? ")
        shop.append(Ashop)
    if ans == "R":
        Rshop = input("What item do you want to remove? ")
        shop.remove(Rshop)
    if ans == "V":
        for i in shop:
            print("•", i)
    

##2. **Find Common Elements**: Given two lists, find the common elements and return them in a new list.

flist = [2,3,"hh",25,"hs"]
slist = [4,"hh",64,3,8]
newlist= []
for i in flist:
    if i in slist:
        newlist.append(i)

print(newlist)

            
##3. **List Deduplication**: Write a function that takes a list and returns a new list with duplicates removed.

duplist = [5,7,"ok",5,9,"ok", "ok", 7]
duplistnew = []
for i in duplist:
    numc = duplist.count(i)
    if numc > 1:
       while duplist.count(i) != 1:
           duplist.remove(i)

print(duplist)
        
        
    

##4. **List Reversal without Built-in Functions**: Reverse a list without using the `reverse()` method.

r = ["ghg","gfchgjh","dfgh", 1, 5, 4]
print(r[::-1])


##5. **Remove All Occurrences**: Write a function that removes all occurrences of a given value from a list

k = ["1","2","3","4","6","leg bye","bye","no ball","wide","dot ball", "1", "1","1","1"]

for i in k:
    if k.count(i) > 1:
        while k.count(i) != 1:
            k.remove(i)

print(k)

##6. **Password Strength Checker**: Write a program to check if a password is strong. A strong password has at least 8 characters, contains both uppercase and lowercase letters, and has at least one number.

def password_checker():
    passw = input("Type your password")
    pscr = 0
    pscr = int(pscr)
    if len(passw) > 8:
         pscr += 1

    if passw.isalnum():
        pscr += 1
    if any (True for i in passw if i.isupper()) and any (True for i in passw if i.islower()):
        
        pscr += 1

    if pscr == 3:
        print("You have a strong password.")
    else:
        print("Try to strengthen your password. ")


    print(pscr)
##    
#7. **Palindrome Checker**: Write a function that checks if a given string is a palindrome (reads the same forwards and backwards).

plstring = input("Type: ")

if plstring == plstring[::-1]:
    print(plstring, " is a palindrome.")
else:
    print(plstring, "is not a palindrome.")
