% knowledge_base.pl

% Example knowledge for family relationships
parent(john, mary).
parent(mary, susan).
parent(susan, tom).

ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
