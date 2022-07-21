# FinitieAutomata
## Project description:
### 1-Introduction
So far, you have familiarized yourself with how Finite Automata works.
Now in this project implement a Finite Automata completely using your programming knowledgethat fulfills all the required features.
### 2-program input format
At first you are given an initial input which is actually a description of an NFA.
In the first line of input, a set is entered that contains the states of the machine and 
the first member of this set it is also the starting mode of the machine.
In the second line comes the alphabet of the language that the machine accepts.
In the third line, you will be given the set of final states of the machine in question.
In the fourth line, a positive integer is given, which represents the number of transfer rules of the desired machine
and then, in each of the next n lines, you will be given each transition rule.
For example, consider the following entry:
{q0, q1, q2, q3, q4}
{a,b}
{q1, q3}
6
q0, q1, a
q1, q2, b
q1, q3,
q3, q4, b
q2, q3, a
q4, q2, a
3
In the above input, the machine in question has 4 states, where q0 is the starting state, and q1 and q3 are also states
They are final states. The accepted language of this machine has the alphabet {b, a}. a, q1, q0 to this
It means that if the car is in q0 state and sees a, it enters q1 state. If alphabetical
If the language is not in these rules, it means λ.
The following figure represents the desired input machine:
### 3-How to run the program
You must first create two classes, NFA and DFA, and the attributes and methods you need to write functions
If you have, implement in these classes. Then, in the Main class, take the input from the user and select the menu
Display functions to the user until the user enters Exit.
### 4-1-Functions that you must implement
Required functions for NFA class:
(a) Write a function called isAcceptByNFA that receives a string as input and
If the string is accepted in the machine, it will return True and otherwise it will return False.
(b) Write a function called createEquivalentDFA that creates the equivalent DFA of the described machine
returned as output.
(c) Write a function named findRegExp that returns the regular expression (equals
Returns the described machine as output.
(d) Write a function called showSchematicNFA which, when called, will display the NFA as
A schematic is displayed.
### 4-2-Required functions for DFA class:
(a) Write a function called isAcceptByDFA that receives a string as input and
If the string is accepted in DFA, it will return True value, otherwise it will return False value.
(b) Write a function called makeSimpleDFA that takes a DFA as input and
simplify it as much as possible and return the simplified DFA as output.
(c) Write a function called showSchematicDFA, which, when called, will display the DFA as
A schematic is displayed.
