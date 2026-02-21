fib(0,0).
fib(1,1).

fib(N,F) :-
    N > 1,
    N1 is N-1,
    N2 is N-2,
    fib(N1,F1),
    fib(N2,F2),
    F is F1 + F2.

print_fib(N) :-
    print_fib(0,N).

print_fib(N,N1) :-
    N =< N1,
    fib(N,F),
    write(F), write(' '),
    N2 is N+1,
    print_fib(N2,N1).

print_fib(N,N1) :-
    N > N1.
