# Author: Zuriahn Yun
# Date: 2/18/2023
# Description: Sierpinski_test

import sierpinski

def check_equal(fn_name, expected, result):
    """ Print the outcome of a test. Prints either PASS or FAIL, based
        on whether expected == result, followed by fn_name (the name
        of the function being tested), followed by expected and result
        values. """
    if expected == result:
        outcome = "PASS"
    else:
        outcome = "FAIL"
        
    print(outcome, fn_name, expected, result)


def test_midpoint():
    """ Tests the midpoint function """
    result = sierpinski.midpoint((0, 0), (2, 2))
    expected = (1.0, 1.0)
    check_equal("midpoint", expected, result)
    
    result = sierpinski.midpoint((4, 4), (0, 0))
    expected = (2.0, 2.0)
    check_equal("midpoint", expected, result)
    
    result = sierpinski.midpoint((0, 4), (0, 0))
    expected = (0.0, 2.0)
    check_equal("midpoint", expected, result)
    
    result = sierpinski.midpoint((4, 0), (0, 0))
    expected = (2.0, 0.0)
    check_equal("midpoint", expected, result)
    
# write your function here to test one of your functions
# from sierpinski.py

def test_distance():
    #Testing Distance function
    result = sierpinski.distance((0,0),(20,20))
    expected = (28)
    check_equal("distance", expected, result)
    
    result = sierpinski.distance((0,0),(500,500))
    expected = (707)
    check_equal("distance",expected, result)

    result = sierpinski.distance((25,25),(400,800))
    expected = (860)
    check_equal("distance",expected,result)
    
    
if __name__ == "__main__":
    
    test_midpoint()
    test_distance()
    # put a call to your test function here
