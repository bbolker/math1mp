import roman3 as rr
from nose.tools import assert_equal, assert_raises
import nose

def test_easy():
    """Single values"""
    vals = ["I","V","X","L","C","D","M"]
    ans = [1,5,10,50,100,500,1000]
    for i in range(len(vals)):
        assert_equal(rr.roman_to_int(vals[i]),ans[i], 'simple example')

def test_combined():
    """Simple cases without subtraction rule"""
    vals = ["III","VI","XII","MDCCLXVI"]
    ans = [3,6,12,1766]
    for i in range(len(vals)):
        assert_equal(rr.roman_to_int(vals[i]),ans[i], 'medium example')

def test_subtraction():
    """Simple subtraction rule"""
    vals = ["IV","IX","XL","XC","CD","CM"]
    ans = [4,9,40,90,400,900]
    for i in range(len(vals)):
        assert_equal(rr.roman_to_int(vals[i]),ans[i], 'subtraction')


def test_complex():
    """Subtraction rule plus extras"""
    vals = ["XIV","MCMXCIX","CDXVIII"]
    ans = [14,1999,418]
    for i in range(len(vals)):
        assert_equal(rr.roman_to_int(vals[i]),ans[i], 'subtraction 2')


def test_weird():
    """Odd/illegal numbers"""
    ## these are illegal, but might work this way
    vals = ["IXX","VX"]
    ans = [19,5]
    for i in range(len(vals)):
        assert_equal(rr.roman_to_int(vals[i]),ans[i], 'weird')

if __name__ == '__main__':
	nose.runmodule(argv=['nose','--verbose'])
