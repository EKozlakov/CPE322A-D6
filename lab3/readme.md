# Lab 3A: Python Basics

## Numerical operations
Below is an example of some basic math functions python is capable of handling via the numpy library, as well how it can identify imaginary and real components of complex numbers.

- Variable assignment and description call  
  ![vass.jpg](imgs/vass.jpg)  
  
- Arithmetic operations  
  - Note: Two asterisks `**` indicate a superscript. Below, the variable `a` (3) has been raised to the power of 2, yielding 9.  
  ![basicmath.jpg](imgs/basicmath.jpg)  

- Complex number descriptions: Below a complex number with an imaginary compenent `2+3j` is set equal to the variable `y`. The following calls serve to identify the real and complex components of this number.  
  ![compmath.jpg](imgs/compmath.jpg)  

## Strings and binary data
The terminal images below show how simple string manipulations can be accomplished in python.  

 - Variable assignment, case manipulation (`.upper()` and `.lower()`), and character removal (`strip()`). All changes made were temporary and displayed immediately.  
    ![stringmanip.jpg](imgs/stringmanip.jpg)  
    
 - Displaying specifics characters and length count. `s[0]` calls for the first character in string variable, `s[6:]` calls for every character starting from the 6th position in the string variable, and `s[6:-1]` calls for every character between the 6th position and the length-1 position (in this case, since the string length is 12, the last character retrieved would be the 11th character.  
    ![charcount.jpg](imgs/charcount.jpg) 
    
 - Binary Encoding and Decoding of strings.  
    ![strbinary.jpg](imgs/strbinary.jpg)
    
 - Concatenation and `print()` formatting.  
    ![concat.jpg](imgs/concat.jpg)

## Tuples
Tuples listing examples.
  ![tuples.jpg](imgs/tuples.jpg)

## Lists  
List manipulation with python.  
  ![lists1.jpg](imgs/lists1.jpg)  
  ![lists2.jpg](imgs/lists2.jpg)  

## If-else statement  
  ![ifelse.jpg](imgs/ifelse.jpg)  
  
## If-not statement
  ![ifnot.jpg](imgs/ifnot.jpg)  

## For-loop statements
  Several examples utilizing previously made strings, lists, and dictionaries.
  ![forloop.jpg](imgs/forloop.jpg)  

## While-loop statements
  ![whileloop.jpg](imgs/whileloop.jpg)

## Break statement
  ![break.jpg](imgs/break.jpg)

## Continue statement
  ![continue.jpg](imgs/continue.jpg)  
  
## More Math
  ![moremath.jpg](imgs/moremath.jpg)
  
## Range function
  Usage `range([start],[stop],[step])`  
  ![range.jpg](imgs/range.jpg)
  
## Defining a few functions.
  ![dfuncs.jpg](imgs/dfuncs.jpg)  

## Keyword args
   ![kwargs.jpg](imgs/kwargsjpg.jpg)
   
## Variable Length Arguments
   ![varargs.jpg](imgs/varargsjpg.jpg)

## Using some modules
   ![modules.jpg](imgs/modules.jpg)

## File read-write
  ![readwrite.jpg](imgs/readwrite.jpg)

## Running some prewritten programs  
### 2example.py (corrected)
  Needed to add a few parentheses around the `print` statement, and change `raw_input()` to `input()`.  
  ![2example.jpg](imgs/2example.jpg)
  
### julian.py
  ![julian.jpg](imgs/julian.jpg)
  
### sun.py - New York, Beijing, and Moscow
  ![sun.jpg](imgs/sun.jpg)
  
### moon.py
  ![moon.jpg](imgs/moon.jpg)
  
### coordinates.py
  Tried a few things here and there with it.  
  ![coordinates.jpg](imgs/coordinates.jpg)
  
### cpu.py
  ![cpu.jpg](imgs/cpu.jpg)
  
### system_info.py
  For some reason, there was a fialure to read my cpu stats.
  ![systeminfo.jpg](imgs/systeminfo.jpg)
  
### socket server magic
  Left : Socket Server. Right : Socket Client.  
  ![socket.jpg](imgs/socket.jpg)
