# Python Cheat Sheet

## General
Modules are added with:
```python
import moduleName
```

## Functions
```python
def functionName (params) # creates a function
```
Functions have a built in attributes accessed like:
```python
__doc__ # will return the description
__name__ #will return the name of the function eg: __main__
```

## Strings
```python
""" shows that strings can go across
many lines """
```
## Dictionaries
```python
dictionaryName = {key1:value1,key2:value2} # defines a dictionary
dictionaryName # prints the whole dictionary
dictionaryName[key] # prints a dictionary value
del dictionaryName[key] # deletes the key value pair
dictionaryName.clear # clears the dictionary
```

## Lists

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

## Tuples
A tuple is an immutable list and can not be changed once it is created
```python
tupleName = (value1, value2, value3,...) # creates a new tuple
```
Accessing and element from a tuple is done the same as a lilst:
```python
tupleName[element] # returns the item at that element
```
