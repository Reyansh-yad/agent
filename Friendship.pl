friend(a,b).
friend(b,c).
friend(c,d).
friend(d,e).

% Direct friend
connected(X,Y) :- friend(X,Y).

% Recursive friend
connected(X,Y) :-
    friend(X,Z),
    connected(Z,Y).
