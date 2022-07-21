## Project description:
### 1-Introduction
So far, you have familiarized yourself with how Finite Automata works.
Now in this project implement a Finite Automata completely using your programming knowledge that fulfills all the required features.
### 2-Program input format
At first you are given an initial input which is actually a description of an NFA.
In the first line of input, a set is entered that contains the states of the machine and 
the first member of this set it is also the starting mode of the machine.
<br />
In the second line comes the alphabet of the language that the machine accepts.
In the third line, you will be given the set of final states of the machine in question.
In the fourth line, a positive integer is given, which represents the number of transfer rules of the desired machine
and then, in each of the next n lines, you will be given each transition rule.
<br />
For example, consider the following entry:
<br />
{q0, q1, q2, q3, q4}
<br />
{a,b}
<br />
{q1, q3}
<br />
6
<br />
q0, q1, a
<br />
q1, q2, b
<br />
q1, q3,
<br />
q3, q4, b
<br />
q2, q3, a
<br />
q4, q2, a
<br />
3
<br />
In the above input, the machine in question has 4 states, where q0 is the starting state, and q1 and q3 are also states
that are final states. The accepted language of this machine has the alphabet {b, a}. a, q1, q0.
It means that if the machine is in q0 state and sees a, it enters q1 state. If alphabetical of the language is not in these rules, it means λ.
<br />
The following figure represents the desired input machine:
<br />
![alt text](https://github.com/k1booshehri/FinitieAutomata/blob/main/Automata.png)
<br />
### 3-How to run the program
You must first create two classes, NFA and DFA, and the attributes and methods you need to write functions
If you have, implement in these classes. Then, in the Main class, take the input from the user and select the menu
Display functions to the user until the user enters Exit.
### 4-1-Functions that you must implement
Required functions for NFA class:
<br />
(a) Write a function called isAcceptByNFA that receives a string as input and
If the string is accepted in the machine, it will return True and otherwise it will return False.
<br />
(b) Write a function called createEquivalentDFA that creates the equivalent DFA of the described machine
returned as output.
<br />
(c) Write a function named findRegExp that returns the regular expression (equals
Returns the described machine as output.
<br />
(d) Write a function called showSchematicNFA which, when called, will display the NFA as
A schematic is displayed.
### 4-2-Required functions for DFA class:
(a) Write a function called isAcceptByDFA that receives a string as input and
If the string is accepted in DFA, it will return True value, otherwise it will return False value.
<br />
(b) Write a function called makeSimpleDFA that takes a DFA as input and
simplify it as much as possible and return the simplified DFA as output.
<br />
(c) Write a function called showSchematicDFA, which, when called, will display the DFA as
A schematic is displayed.
