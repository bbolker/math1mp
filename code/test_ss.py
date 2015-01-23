import silly_string as ss
from nose.tools import assert_equal, assert_raises
import nose

def test_silly():
	'''A trivial test of silly_string'''
	assert ss.silly_string("")=="", 'empty string'

def test_silly2():
	'''A slightly less trivial test'''
	assert_equal(ss.silly_string("abc"), 'cab')

if __name__ == '__main__':
	nose.runmodule(argv=['nose','--verbose'])

    
    
    

