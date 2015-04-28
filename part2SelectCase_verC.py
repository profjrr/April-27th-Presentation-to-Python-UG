##Select_Case Demo2 verC
##
### Begin switch-case in Python:Switch-case in Python (lighting approx. 5mins)
### There isn't one!!!
###
### Sooooooooo create the following pattern with Ifs 
###(ref: Lighting Talk on Ifs)!

### More than likely violates the JPL Institutional Coding Standard

### Professor Reed -- updated (21-APR-2015) for 3.4+
### Recipe 410692 -- my version C for comparing "simple ifs"
###

import string

print("Presently Python does NOT provide a Select/Case statement.")
print("The following demo attempts to emulate this program construct pattern")
print('by building a "switch class!"')
print("Why Doesn't NASA/JPL permit this???")
print()
##
# This class provides the functionality we want. You only need to look at
# this if you want to know how this works. It only needs to be defined
# once, no need to muck around with its internals.
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
   
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False

####################################
# Rewrite of CASE/Switch logic engine
# Updated and corrected by Professor Reed (24-APR-2015).
####################################

def case_x(x): 
    for case in switch(x):
        if case(-1):
            print("[Test case no.1: ]")
            print("x is a negative value of: ", x)
            break
        if case(0):
            print("[Test case no.2: ]")
            print("x is a value of zero: ",x)
            break
        if case(1):
            print("[Test case no.3: ]")
            print("x is a postive value of: ",x)
            break
        if case(): # default, could also just omit condition or 'if True'
            print("[TEST default x is something else!]")
            print("x is a strange value of: ", x)
            print("sometimes called 'otherwise'")
            # No need to break here, it'll stop anyway          
    print()
    

### Professor Reed's test case for Case/Select pseudo-statement in Python
### for Python 3.4+
###
##def main():
## main() is commented out here above!!!
#
def testCaseSelects():
## run1 ###
    x = -1 
    case_x(x)
    print("### end of test case 1 ###")
    print()
    
## run2 ###
    x = 0 
    case_x(x)
    print("### end of test case 2 ###")
    print()
    
## run3 ###
    x = +1 
    case_x(x)    
    print("### end of test case 3 ###")
    print()

## runDefaultCase ###

    x = 9
    case_x(x)    
    print("### end of 'default test case' default ###")
    print()    
 

### Professor Reed uses test cases instead of main()!
##if __name__ == '__main__':
##    main()
##
### run-it directly and automatically!
##
testCaseSelects()


