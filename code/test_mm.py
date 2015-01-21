import mat_mult as mm
from nose.tools import assert_equal, assert_raises

def silly_test():
    assert mm.mat_mult([[0]],[[0]])==[[0]]

def minimal_tests():
    ## assert_equal(mm.mat_mult([[0]],[[0]]),[[2]],"test zero")
    assert_equal(mm.mat_mult([[0]],[[0]]),[[0]],"test one")
    assert_equal(mm.mat_mult([[1]],[[1]]),[[1]])

def less_minimal_test():    
    m1 = [[1,2],[3,4]]
    m2 = [[5],[6]]
    assert_equal(mm.mat_mult(m1,m2),[[17], [39]])

def test_conform():
   ## assert_raises(ValueError, mm.mat_mult, [[0]],[[0]])
   assert_raises(ValueError, mm.mat_mult,[[0]],[[1,1],[1,1]])

## UNFINISHED -- would like to test with random matrices
## from numpy.random import random_integers,seed
## seed(101)
## def rand_matrix(m,n):
    
    
    

