% Facts
male(rajesh).
male(amit).
male(karan).
female(sita).
female(priya).

parent(rajesh, amit).
parent(sita, amit).
parent(rajesh, priya).
parent(sita, priya).
parent(priya, karan).

% Rules
sibling(X,Y) :-
    parent(P,X),
    parent(P,Y),
    X \= Y.

nephew(X,Y) :-
    male(X),
    parent(P,X),
    sibling(P,Y).

cousin(X,Y) :-
    parent(P1,X),
    parent(P2,Y),
    sibling(P1,P2).
