


%facts:
% likes(Customer,F/M)

gen_flavors([],[]).
gen_flavors([N|Rest],[N/malted,N/unmalted|Flavors]):-
	gen_flavors(Rest,Flavors).

one_batch(F,Batches):-
	(member(F/malted,Batches),
	 not(member(F/unmalted,Batches)))
	 ;(member(F/unmalted,Batches),
	 not(member(F/malted,Batches))
	   ).

make_one_batch(F,Batches,NewBatch):-
	(select(F/malted,Batches,NewBatch),
	 member(F/unmalted,NewBatch))
	;(select(F/unmalted,Batches,NewBatch),
	  member(F/malted,NewBatch)).	 

range(N,Range):-
	findall(F,between(1,N,F),Range).

likes(3,2/malted).
likes(2,5/malted).
likes(1,3/unmalted).
likes(1,4/malted).


c_likes(NCustomers,CLike):-
	findall(C/B,(between(1,NCustomers,C),likes(C,B)),CLike).

min_batch(N,NCustomers,Batches):-
	range(N,F),
	gen_flavors(F,Flavors),
	c_likes(NCustomers,CLikes).

%for each customer at least one milk shake he likes
at_least_one([],_).
at_least_one([H|T],CLikes):-
	

%% Test predicates for the defined list predicates
%:- begin_tests(milktests).

%test(one_batch,[nondet]):-
%	one_batch(2/malted,[1/malted,3/unmalted,2/malted,5/malted]).
%test(one_batch,[nondet,fail]):-
%	one_batch(2/malted,[1/malted,2/unmalted,2/malted,5/malted]).
%test(one_batch,[nondet,fail]):-
%	one_batch(_/_,[]).

%:- end_tests(milktests).
