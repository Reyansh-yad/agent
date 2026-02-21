% Gender facts
male(raj).
male(amit).
female(sita).
female(gita).

% Love facts
loves(raj, gita).
loves(amit, gita).
loves(sita, raj).

% Opposite gender rule
opposite_gender(X,Y) :- male(X), female(Y).
opposite_gender(X,Y) :- female(X), male(Y).

% Jealousy rule
jealous(X,Y) :-
    loves(X,Z),
    loves(Y,Z),
    opposite_gender(X,Y),
    X \= Y.
