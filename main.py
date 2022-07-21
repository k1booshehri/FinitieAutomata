'''
P1_input_example.pdf:

{q0,q1,q2,q3,q4,q5,q6}
{a,b}
9
q0,q1,a
q1,q1,b
q1,q2,
q2,q3,a
q3,q2,a
q3,q4,b
q2,q5,b
q5,q6,a
q6,q1,b
{q1,q3,q6}

'''

import Tools


NFA = Tools.CreateNFA()
NFA.DrawNFA()



string=""
print(NFA.IsAcceptByNFA(string))
string="abb"
print(NFA.IsAcceptByNFA(string))
string="abaa"
print(NFA.IsAcceptByNFA(string))
string="abab"
print(NFA.IsAcceptByNFA(string))
string="aaaaaa"
print(NFA.IsAcceptByNFA(string))



DFA = NFA.CreateEqeulvantDFA()
DFA.DrawDFA()



string=""
print(DFA.IsAcceptByDFA(string))
string="abb"
print(DFA.IsAcceptByDFA(string))
string="abaa"
print(DFA.IsAcceptByDFA(string))
string="abab"
print(DFA.IsAcceptByDFA(string))
string="aaaaaa"
print(DFA.IsAcceptByDFA(string))


SDFA = DFA.MakeSimpleDFA()
SDFA.DrawSDFA()


GNFA = Tools.GNFA(NFA)
print(Tools.FindRejex(GNFA))

'''
DFA Simplification.pdf:

{q0,q1,q2,q3,q4,q5}
{0,1}
12
q0,q3,0
q3,q0,0
q3,q4,1
q0,q1,1
q4,q5,1
q1,q2,0
q1,q5,1
q4,q2,0
q2,q5,1
q2,q2,0
q5,q5,0
q5,q5,1
{q1,q4,q2}

'''