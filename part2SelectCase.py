##Select_Case Demo1
##
### Begin switch-case in Python:Switch-case in Python (lighting approx. 5mins)
### There isn't one!!!
###
### Sooooooooo create the following pattern with Ifs 
###(ref: Lighting Talk on Ifs)!

### More than likely violates the JPL Institutional Coding Standard

### Professor Reed -- updated (10-DEC-2014) for 3.4+
### Recipe 410692 -- my version D
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


# The following example is pretty much the exact use-case of a dictionary,
# but is included for its simplicity. Note that you can include statements
# in each suite. Updated and corrected by Professor Reed (10-DEC-2014).
def case_c1(c1):
##    c1 = 'ten'
    print("[Test case no.1: ]")
    print("c1 is a value of: ")
    for case in switch(c1):
        if case('one'):
            print(1)
            break
        if case('two'):
            print(2)
            break
        if case('ten'):
            print(10)
            break
        if case('eleven'):
            print(11)
            break
        if case(): # default, could also just omit condition or 'if True'
            print("default c1 is something else!")
            # No need to break here, it'll stop anyway
            
    print()
    
# break is used here to look as much like the real thing as possible, but
# elif is generally just as good and more concise.
# Empty suites are considered syntax errors, so intentional fall-throughs
# should contain 'pass'.
### Updated and corrected by Professor Reed (10-DEC-2014).

def case_c2(c2):
##    c2 = 'z'
    print("[Test case no.2: ]")
    print("c2 is: ", c2)

    for case in switch(c2):
        if case('a'): pass # only necessary if the rest of the suite is empty
        if case('b'): pass
        # ...
        if case('y'): pass
        if case('z'):
            print("c2 is lowercase!")
            break
        if case('A'): pass
        # ...
        if case('Z'):
            print("c2 is UPPERCASE!")
            break
        if case(): # default
            print("I default to dunno what c2 was!")
           
    print()
   
# As suggested by Pierre Quentel, you can even expand upon the
# functionality of the classic 'case' statement by matching multiple
# cases in a single shot. This greatly benefits operations such as the
# uppercase/lowercase example above:
### Updated and corrected by Professor Reed (10-DEC-2014).
def case_c3(c3):
##    c3 = 'A'
    print("[Test case no.3: ]")
    print("c3 is: ", c3)

    for case in switch(c3):
        if case(*string.ascii_lowercase):
    ##    if case(*string.lowercase): # note the * for unpacking as arguments
            print("c3 is lowercase!")
            break
        if case(*string.ascii_uppercase):
            print("c3 is UPPERCASE!")
            break
        if case('!', '?', '.'): # normal argument passing style also applies
            print("c3 is a sentence terminator!")
            break
        if case(): # default
            print("I default to dunno what c3 was!")
         
    print()

### Professor Reed's test case for Case/Select pseudo-statement in Python
### for Python 3.4+
###
##def main():
## main() is commented out here above!!!
#
def testCaseSelects():
## run1 ###
    c11 = 'ten' ## test case#1 -- supply a literal 'ten'
    ## and then print(10)
    c12 = 'z'   ## test case#2 -- supply a lowercase 'z'
    ## and then print c2 is lowercase!
    c13 = 'A'   ## test case#3 -- supply an UPPERCASE 'A'
    ## and then print c3 is UPPERCASE!
    ##
## run2 ###   
    c21 = 'zero' # default exercised!!!
    c22 = '%' # default exercised!!!
    c23 = '%' # default exercised!!!
    ##
## run3 ###
    c31 = 'one'
    c32 = 'X'
    c33 = 'y'
    
    case_c1(c11)
    case_c2(c12)
    case_c3(c13)
    print("### end of test case 1 ###")
    print()

    case_c1(c21)
    case_c2(c22)
    case_c3(c23)
    print("### end of test case 2 ###")
    print()

    case_c1(c31)
    case_c2(c32)
    case_c3(c33)
    print("### end of test case 3 ###")  
    print()

### Professor Reed uses test cases instead of main()!
##if __name__ == '__main__':
##    main()
##
### run-it directly and automatically!
##
testCaseSelects()


