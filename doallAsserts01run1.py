### Begin Ifs in Python:
## Version H -- asserts -- run1 -- clean run!
##
### Python ifs presented by Professor Reed
### last updated (27-APR-2015)
### for Python 3.4+
### Featured Speaker -- Python User Group -- Apr. 2015
##
##
##import string
### NOW WITH ASSERTS!!! ###
import pytest

def simpleIf(x):
    print("Demo Simple IF Demo*: ")
    print("x is:, ",x)
##    if __debug__:
##       if not x < 0: raise AssertionError("x is not less than zero")
##    assert(x < 0) ,("### x is not less than zero ###")
    if x < 0:
        print("simple if test ran:", x)
        print("x is less than 0")
    print("end of Simple IF Demo*: ")
    print ("*** Doesn't meet NASA/JPL Stds, WHY? ***")
    print()

def ifWithElse(x):
    ## What is wrong with this one??? ##
    print("Demo IF_WITH_ELSE only! Demo**: ")
##    assert(x < 999)
    assert(x < 0),("### x is not less than zero ###")
    if x < 0:
        print("with else test ran:", x)
        print("x is less than 0")
    else:
        print("else x determines x is greater than a negative value")
    print("end of Demo**: ")
    print ("*** Doesn't meet NASA/JPL Stds, WHY? ***")
    print()
    
def elseIf(x):
    print("Demo ELIF Demo***: ")
    assert(x < 0)
    if x < 0:
        print("with else elseif:", x)
        print("x is less than 0")
    elif x == 0:
        print("elif x is equal to zero")
    else:
        print("final else x is greater than a negative value not ZERO!")
    print("end of Demo***: ")
    print ("===> DOES meet NASA/JPL Stds, YES!!! <===")
    print()

def elIf2(x):
    print("**** Demo ELIF2 Demo ****: ")
    assert(x > 0) and (x <=200)
    if x < 0:
        print("with else elseif:", x)
        print("x is less than 0")
    elif x == 0:
        print("elif x is equal to zero")
    elif x > 0 and x <= 200:
        print("final elif x is greater than a negative value not ZERO and less or eq 200!")
    else:
        print("otherwise, not a proper value of x?")
    print("end of Demo***: ")
    print ("===> DOES meet NASA/JPL Stds, YES, but better!!! <===")
    print()         

##        
##       
### --- Professor Reed's test driver area --- ###
##
    
def testMyIfs(x):
### Part II ###   
##    int(x)
    print()
    print("x is: ", x)
    ##        
    print()
    print("the value of x is: ", x)
    print()
##    print("assert(x < 0) ,('### x is not less than zero ###')")
##    print("x is suppose to be neg!")
    print()
    ##
##    simpleIf(x)     ## first demo   -- simple if test
##    ifWithElse(x)  ## second demo -- if/else test
##    elseIf(x)       ## third demo   -- if/elif/else test
    elIf2(x)        ### final test or otherwise ###
    print()

### Testing values and area follow: ##
##
##print("[negative value test1:]")
##x = 1
####x = 0
####x = 999
####x = 1011
##testMyIfs(x)
##print("[zero value test2:]")
##x = 0
##testMyIfs(x)
##print("[positive value test3:]")
##x = 1
##testMyIfs(x)
####
####
print("[otherwise x invalid value TEST#4:]")
x = 999
##x = 200
print(x)
testMyIfs(x)
##
### note: the test driver area above is a replacement for main()
##    
### Professor Reed uses test cases instead of main()!
##if __name__ == '__main__':
##    main()    
    
