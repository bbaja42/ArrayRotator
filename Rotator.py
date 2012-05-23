'''
Algorithm to rotate given array with n elements for x positions to the left
with following limitations
space = O(1)
time = O(n)

'''

def rotate_left(array, offset):
    """Rotate the array to the left for offset positions"""
    offset %= len(array)
    # Inverse whole array
    inverse(array, 0, len(array) - 1)
    separator = len(array) - offset - 1
    # Inverse left part
    inverse(array, 0, separator)
    # Inverse right part
    inverse(array, separator + 1, len(array) - 1)


def inverse(array, start, end):
    #print "Called with:", start,end
    """Inverse the given array between start and end parameters"""
    middle = (end + start + 1) / 2
    counter = 0
    while start + counter < middle:
        array[start + counter], array[end - counter] = array[end - counter], array[start + counter]
        counter += 1
        

       
from array import array

test_array_odd = array('l', [1, 2, 3, 4, 5])
test_array_even = array('l', [1, 2, 3, 4, 5, 6])


def test_inverse():
    print "Inverse method testing"
    
    # Testing no change
    sample = array('l', [1, 2, 3, 4, 5])
    inverse(sample, 0, 0)
    assert sample == array('l', [1, 2, 3, 4, 5])
    
    # Testing no change
    sample = array('l', [1, 2, 3, 4, 5])
    inverse(sample, 4, 4)
    assert sample == array('l', [1, 2, 3, 4, 5])
    
    # Testing 2 elements switch
    sample = array('l', [1, 2, 3, 4, 5])
    inverse(sample, 3, 4)
    assert sample == array('l', [1, 2, 3, 5, 4])
    
    # Testing odd size inverse
    sample = array('l', [1, 2, 3, 4, 5])
    inverse(sample, 0, 4)
    assert sample == array('l', [5, 4, 3, 2, 1])
    
    # Testing even size inverse
    sample = array('l', [1, 2, 3, 4, 5, 6])
    inverse(sample, 0, 5)
    assert sample == array('l', [6, 5, 4, 3, 2, 1])

def test_rotation_left():
    print "Rotation method testing"
    
    # Testing no change
    sample = array('l', [1, 2, 3, 4, 5])
    rotate_left(sample, 0)
    assert sample == array('l', [1, 2, 3, 4, 5])
    
    # Testing 1 shift
    sample = array('l', [1, 2, 3, 4, 5])
    rotate_left(sample, 1)
    assert sample == array('l', [2, 3, 4, 5, 1])
    
    # Testing shift for 2 elements
    sample = array('l', [1, 2, 3, 4, 5])
    rotate_left(sample, 2)
    assert sample == array('l', [3, 4, 5, 1, 2])
    
    # Testing shift for 2 elements even sample
    sample = array('l', [1, 2, 3, 4, 5, 6])
    rotate_left(sample, 2)
    assert sample == array('l', [3, 4, 5, 6, 1, 2])
    
    # Testing shift for n elements
    sample = array('l', [1, 2, 3, 4, 5])
    rotate_left(sample, 5)
    assert sample == array('l', [1, 2, 3, 4, 5])
    
    
test_inverse()
test_rotation_left()
