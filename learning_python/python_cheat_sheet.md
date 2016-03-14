# Python Cheat Sheet


## General
----
Modules are added with:
```python
import moduleName
```
If statements are functions, they need indentation too
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
Mathematical Operators
|Operator	|Action		|
|---------------|---------------|
|"+, *, /, -"	|Standard Ops	|
|%		|Modulus	|
|**		|To the power	|
|"+=, /=, *=, -=|num = num op num|


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
## Boolean Logic
----
### Equality:
```python
print 1 == 1 # true
print 1 is 1 # true
temp = "hello world"
print temp is "hello" # true
print temp == "hello" # true
```

### Inequality:
```python
print 1 is not 1 # false
print 1 is not 2 # true
print 1 != 2 # true
print not (1 is 2) # true
```
### Rest:
+ ">, <"
+ ">=, <="

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
Functions are not limited by the input types
```python
def printSomething(x)
  print "the input is %s" % (x,)

printSomething("hello")
printSomething(100)
```
All the above will print happily
## Strings
----
```python
""" shows that strings can go across
many lines """
```
### Formating Strings
Strings can be concatenated to other strings using the + but a string can not be added to another data type
Numbers can be added to strings using type casting
```python
print "I am adding to " + "this string" # is happy and moves on
print "I am " + 25 + "years old" # fails to run str and int can not be added together
print "I am " + str(25) + "years old" # will run
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

### Slicing Strings
```python
temp = "this is a string"
print temp[:4] # prints "this"
firstBit = temp[:4] # assigns "this" to firstBit
```
### More String Operators
+ .find(item) - finds the first instance of a the occurance of item

Numbers can be formated with decial values

| Formate  | Input    | Output  |
|----------|          |         |
| %f       | 50.1234  | 50.1234 |
| %.2f     | 50.1234  | 50.12   |
| %.2f     | 1.5      | 1.50    |

## Statements
----

### If Statements
```python
if condition :
  statement
```
### For Loops
```python
for item in list:
  statement
```
### While Loop
```python
count = 0
while (count < x)
  statement
 count += 1
```
### The in operator
```python
print "hello" in [1, 3, 4, "hello", 100] # prints true
```

### With Statement
When there is two operations that need to execute together
```python
with open('filename') as name:
  Statement
```

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
10. range(start, end) # generates a list of integers from start to end
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
## File Handling
 ```python
 open(name, mode, buffering)
 ```
 + name is the file name to open
 + mode indicates how the file will opened
    + 'r' read from a file
    + 'w' write to a file
 + sets the desired buffer size
    + 0 means no buffering
    + +n buffers to a size n
    + -n use the system default
