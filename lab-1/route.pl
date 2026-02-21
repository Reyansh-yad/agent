edge(a,b).
edge(b,c).
edge(c,d).
edge(d,e).

route(X,Y,[X,Y]) :- edge(X,Y).
route(X,Y,[X|T]) :-
    edge(X,Z),
    route(Z,Y,T).
