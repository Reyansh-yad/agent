male(rajesh).
male(amit).
female(priya).
female(sita).

married(rajesh, sita).
married(amit, priya).

parent(ram, rajesh).
parent(ram, amit).

sibling(X,Y) :-
    parent(P,X),
    parent(P,Y),
    X \= Y.

brother_in_law(X,Y) :-
    male(X),
    married(X,Z),
    sibling(Z,Y).

sister_in_law(X,Y) :-
    female(X),
    married(X,Z),
    sibling(Z,Y).
