# version code 565cc389e900+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

from vec import Vec
from GF2 import one
from itertools import *

## 1: (Problem 1) Vector Comprehension and Sum
def vec_select(veclist, k):
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_select([v1, v2, v3, v4], 'a') == [Vec(D,{'b': 1}), Vec(D,{'b': 2})]
    True
    '''
    #return [ v for v in veclist if v[k]==0 ]
    V_L = [ v for v in veclist if v[k]==0]
    for v in V_L:
        v.f = { x:y for (x,y) in v.f.items() if x!=k}
    return V_L
def vec_sum(veclist, D):
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_sum([v1, v2, v3, v4], D) == Vec(D, {'b': 13, 'a': 11})
    True
    '''
    S=Vec(D,{})
    for v in veclist:
        S += v
    #S.f={ x:y for (x,y) in S.f.items() if y!=0 }
    return S

def vec_select_sum(veclist, k, D):
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_select_sum([v1, v2, v3, v4], 'a', D) == Vec(D, {'b': 3})
    True
    '''
    return vec_sum(vec_select(veclist,k), D)


## 2: (Problem 2) Vector Dictionary
def scale_vecs(vecdict):
    '''
    >>> v1 = Vec({1,2,4}, {2: 9})
    >>> v2 = Vec({1,2,4}, {1: 1, 2: 2, 4: 8})
    >>> result = scale_vecs({3: v1, 5: v2})
    >>> len(result)
    2
    >>> [v in [Vec({1,2,4},{2: 3.0}), Vec({1,2,4},{1: 0.2, 2: 0.4, 4: 1.6})] for v in result]
    [True, True]
    '''
    #return [ Vec(v.D, { x:y/scale for (x,y) in v.f.items() }) for (scale, v) in vecdict.items() ]
    return [ 1/scale*v for (scale, v) in vecdict.items() ]


## 3: (Problem 3) Constructing span of given vectors over GF(2)
def GF2_span(D, S):
    '''
    >>> from GF2 import one
    >>> D = {'a', 'b', 'c'}
    >>> GF2_span(D, {Vec(D, {'a':one, 'c':one}), Vec(D, {'c':one})}) == {Vec({'a', 'b', 'c'},{}), Vec({'a', 'b', 'c'},{'a': one, 'c': one}), Vec({'a', 'b', 'c'},{'c': one}), Vec({'a', 'b', 'c'},{'a': one})}
    True
    >>> GF2_span(D, {Vec(D, {'a': one, 'b': one}), Vec(D, {'a':one}), Vec(D, {'b':one})}) == {Vec({'a', 'b', 'c'},{'a': one, 'b': one}), Vec({'a', 'b', 'c'},{'b': one}), Vec({'a', 'b', 'c'},{'a': one}), Vec({'a', 'b', 'c'},{})}
    True
    >>> S={Vec({0,1},{0:one}), Vec({0,1},{1:one})}
    >>> GF2_span({0,1}, S) == {Vec({0, 1},{0: one, 1: one}), Vec({0, 1},{1: one}), Vec({0, 1},{0: one}), Vec({0, 1},{})}
    True
    >>> S == {Vec({0, 1},{1: one}), Vec({0, 1},{0: one})}
    True
    '''
    Span =set()
    for Coef in list(product([0, one], repeat=len(S))):
        print([x for x in zip(Coef,S)])
        Span.add(vec_sum([x[0]*x[1]  for x in zip(Coef, S)], D))
    return Span


## 4: (Problem 4) Is it a vector space 1
# Answer with a boolean, please.
is_a_vector_space_1 = ...



## 5: (Problem 5) Is it a vector space 2
# Answer with a boolean, please.
is_a_vector_space_2 = ...



## 6: (Problem 6) Is it a vector space 3
# Answer with a boolean, please.
is_a_vector_space_3 = ...



## 7: (Problem 7) Is it a vector space 4
# Answer with a boolean, please.
is_a_vector_space_4a = ...
is_a_vector_space_4b = ...

D = {'a','b','c'}
v1 = Vec(D, {'a': 0})
v2 = Vec(D, {'a': 3, 'b': 0})
v3 = Vec(D, {        'b': 2})
v4 = Vec(D, {'a': 10, 'b': 10})
print(vec_select([v1, v2, v3, v4], 'a'))
print(vec_sum([v1, v2, v3, v4], D))
print(vec_sum([v1, v2, v3, v4], D) == Vec(D, {'b': 13, 'a': 11}))

print(vec_select_sum([v1, v2, v3, v4], 'a', D) == Vec(D, {'b': 3}))
result = scale_vecs({3: v1, 5: v2})
print(result)
v1 = Vec({1,2,4}, {2: 9})
v2 = Vec({1,2,4}, {1: 1, 2: 2, 4: 8})
result = scale_vecs({3: v1, 5: v2})
print(result)
print([v in [Vec({1,2,4},{2: 3.0}), Vec({1,2,4},{1: 0.2, 2: 0.4, 4: 1.6})] for v in result])
v1 = Vec({1,2,4},{} )
v2 = Vec({1,2,4},{}) 
result = scale_vecs({3: v1, 5: v2})
print(result)
S={Vec({0,1},{0:one}), Vec({0,1},{1:one})}
print(GF2_span({0,1}, S))

