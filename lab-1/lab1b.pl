loves(vanu,ria).
loves(madan,ria).
loves(pumpkin,honey_bunny).
loves(honey_bunny,pumpkin).

jealous(X,Y):- loves(X,Z), loves(Y,Z), X\=Y.

