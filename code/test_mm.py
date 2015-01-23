import mat_mult as mm
from nose.tools import assert_equal, assert_raises
import nose

def test_silly():
	'''A trivial test of mat_mult.'''
	assert mm.mat_mult([[0]],[[0]])==[[0]], 'Two 1x1 zeros'

def test_minimal():
	'''Test trivial with 1s'''
	assert_equal(mm.mat_mult([[1]],[[1]]),[[1]], 'Two 1x1 with ones')

def test_less_minimal():
	'''Test 2x2, 2x1, real numbers'''
	m1 = [[1,2],[3,4]]
	m2 = [[5],[6]]
	assert_equal(mm.mat_mult(m1,m2),[[17], [39]], '2x2 * 2x1, ints')

def test_conform():
	'''Test that it raises the correct value error'''
	## NOTE slightly different syntax (error, function, args)
	assert_raises(ValueError, mm.mat_mult,[[0]],[[1,1],[1,1]])

if __name__ == '__main__':
	nose.runmodule(argv=['nose','--verbose'])
## UNFINISHED -- would like to test with random matrices
## from numpy.random import random_integers,seed
## seed(101)
## def rand_matrix(m,n):
    
    
    

