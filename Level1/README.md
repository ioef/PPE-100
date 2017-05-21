Questions 

q1:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
Hints: 
Consider use range(#begin, #end) method

q2:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

q3:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
Consider use dict()

q4:
Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

q5:
class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters

q6:
Write a method which can calculate the area of a circle
Hints: Using the ** Operator

q7:
Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.
Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
And add document for your own function
    
Hints:
    The built-in document method is __doc__


q8:
    Define a class, which have a class parameter and have a same instance parameter.

Hints: Define a instance parameter, need add it in __init__ method
    You can init a object with construct parameter or set the value later

q9:
Define a function that can convert a integer into a string and print it in console.

Hints: Use str() to convert a number to string.

q10:
Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.
Hints: Use int() to convert a string to integer.

q11:
Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.

Hints:

Use len() function to get the length of a string

q12:
Define a function which can generate a dictionary where the keys are the numbers 1 to 20 and the values correlated to these keys are the reversed sequence.
["1":20, "2":19, "3","18" etc. etc.]


q13:
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list

q14:
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list

q15:
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line. 

Hints: Use [n1:n2] notation to get a slice from a tuple.

q16:
Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10). 

Hints: Use "for" to iterate the tuple. Use tuple() to generate a tuple from a list.

q17:
Print a unicode string "hello world".

Hints:
Use u'strings' format to define unicode string.

q18:
Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

Hints:
Use unicode() function to convert.


q19:
Write a program to compute:
f(n)=f(n-1)+100 when n>0
and f(0)=1 with a given n input by console (n>0).

Example:
If the following n is given as input to the program:
5

Then, the output of the program should be:
500

q20:
The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.

Example:
If the following n is given as input to the program:
7

Then, the output of the program should be:
0,1,1,2,3,5,8,13


Hints:
We can define recursive function in Python.
Use list comprehension to generate a list from an existing list.
Use string.join() to join a list of strings.

q21:
Print the ordinal values of the characters consisting a given string.
For example if we print the ordinal values of the string "Hello World"
the Result should be like the following:
The ordinal value of character H is 72
The ordinal value of character e is 101
The ordinal value of character l is 108
The ordinal value of character l is 108
The ordinal value of character o is 111

As bonus you may also print the hex and the binary values.


