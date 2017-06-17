# lab03_test.py
# PUT YOUR NAME AND NETID HERE
# PUT THE DATE YOU LAST CHANGED THIS FILE HERE
# Skeleton by Walker M. White (wmw2), Lillian Lee (LJL2), Feb 2017


"""(Skeleton of) tests for lab03.py"""

import cornelltest      # For assert_equals and assert_true
import lab03   # This is what we are testing


def test_replace_first():
    """Test procedure for repeat_first"""
    print 'Testing the function replace_first'
    
    print "\tTesting crane, a-> o"    
    result = lab03.replace_first('crane','a','o')
    cornelltest.assert_equals('crone', result)

    # YOU NEED TO ADD MORE TEST CASES
    
###########
### SCRIPT CODE (Call test procedures here)
###########

def test_first_in_double_quotes():
    """Test procedure for first_in_double_quotes"""
    print 'Testing the function first_in_double_quotes'
    
    print '\tTesting \'A \"B C\" D\''
    result = lab03.first_in_double_quotes('A "B C" D')
    cornelltest.assert_equals('B C', result)
    
    # YOU NEED TO ADD MORE TEST CASES
    


test_replace_first()
# test_first_in_double_quotes()
print 'Module lab03: all tests passed'