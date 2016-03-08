# Python Cheat Sheet


## General
----
Modules are added with:
```python
import moduleName
```
If statements are functions, they need indentation too
```python
if condition :
  statement
```
Statements can run over multiple lines with the use of a "\":
```python
myParams = { key1: value1, \
             key2: value2,\
             key3:value3 \
             }
```
## Variables
----
+ Variables declarations do not technically exist.
+ Python has local and global variables
+ Variables must be declared before use

### Assignment:
```python
myVariable = "this is an assignment"
```
### Assigning Multiple Values at Once:
```python
variable1 = ('a','b','c')
(x,y,z) = v # assign each element of v to a different variable, x = 'a', y = 'b', z = 'c'

```

## Functions
----
```python
def functionName(params) # creates a function
```
Functions have a built in attributes accessed like:
```python
__doc__ # will return the description
__name__ # will return the name of the function eg: __main__
```

## Strings
----
```python
""" shows that strings can go across
many lines """
```
### Formating Strings
Strings can be concatenated to other strings using the + but a string can not be added to another data type
```python
print "I am adding to " + "this string" # is happy and moves on
print "I am " + 25 +"years old" # fails to run str and int can not be added together
```
Place holders can be used to add variables into strings and perform type coercion
```python
fname = "deon"
sname = "pearson"
print "my name is %s %s" % (fname, sname) # outputs my name is deon pearson
```
### Formating Numbers

### String Splitting
.split(seperator, numberOfSplits)

```python
myStr = "fname = deon;sname = pearson;age = 25" with the ; as a seperator
myStr.split(";") # split the string on the ; outputting ["fname = deon", "sname = pearson", "age = 25"]
myStr.split(";", 1) # splits the string once then leaves the rest in the second element outputting ["fname = deo", "sname = pearson;age = 25"]
```

Numbers can be formated with decial values

| Formate  | Input    | Output  |
|----------|          |         |
| %f       | 50.1234  | 50.1234 |
| %.2f     | 50.1234  | 50.12   |
| %.2f     | 1.5      | 1.50    |

## Dictionaries
----
```python
dictionaryName = {key1:value1,key2:value2} # defines a dictionary
dictionaryName # prints the whole dictionary
dictionaryName[key] # prints a dictionary value
del dictionaryName[key] # deletes the key value pair
dictionaryName.clear # clears the dictionary
dictionaryName.items() # returns a list of tuples of each item in the dictionary
```

## Lists
----
```python
listName = {value1, value2,....} # defines a list
listName[element] #access an element in the list
listName[-1] # access elements from the end of the list and counts back
listName[x:y] # gets a subset from x till y excluding y
```
### List Functions:
```python
1. .append(item) # adds the element to the end of the list
2. .insert(element,item) # inserts the element into the list at the position
3. .extend(listName) # joins the new list to the old one
4. .append(objectName) # adds the object to the end of the list
5. len(listName) # returns the length of the list
6. listName.index(item) # returns the index number of the item
7. value in listName # returns true or false
8. .remove(item) # removes the first occurance of item
9. .pop() # pops the last element of the list and returns it
```

### List Operators:
```python
1. listName + otherList # adds the two lists together to form one list
2. listName += [newItem] # adds the new item to the list
3. listName = [value1, value2] + 3 # [value1, value2,value1, value2,value1, value2]
```
### Mapping Lists
A way of mapping a list into another list using a function on each element
```python
list = [1,9,8,4]
newList = [elem*2 for elem in list] # newList = [2,18,16,8]

d = {"fname": "deon", "sname": "pearson"}
[%s = %s % (a,b) for a, b in d.items()] # outputs ["fname = deon", "sname = pearson"]
```

### Joining Lists
You can not join non strings
```python
d = {"fname": "deon", "sname": "pearson"}
";".join (["%s = %s" % (a,b) for a, b in d.items()]) # outputs a string of "fname = deon;sname = pearson" with the ; as a seperator
```
## Tuples
----
A tuple is an immutable list and can not be changed once it is created
```python
tupleName = (value1, value2, value3,...) # creates a new tuple
```
Accessing and element from a tuple is done the same as a lilt:
```python
tupleName[element] # returns the item at that element
```
