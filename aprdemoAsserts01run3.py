### Begin Ifs in Python:
## Version H -- asserts -- run3
##
### Python ifs presented by Professor Reed
### last updated (26-APR-2015)
### for Python 3.4+
### Featured Speaker -- Python User Group -- Apr. 2015
##
##
##import string
### NOW WITH ASSERTS!!! ###
import pytest

def elIf2(x):
    print("**** Demo ELIF2 Demo ****: ")
##    assert(x <= 0), ("big tests of asserts") ## now asserting the right values!
    assert(x <= 1), ("big tests of asserts") ## now asserting the right values again!

    if x < 0:
        print("with else elseif:", x)
        print("x is less than 0")
    elif x == 0:
        print("elif x is equal to zero")
    elif x > 0 and x <= 1:
        print("final elif x is greater than a negative value not ZERO!")
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
    ##
##    simpleIf(x)     ## first demo   -- simple if test
##    ifWithElse(x)  ## second demo -- if/else test
##    elseIf(x)       ## third demo   -- if/elif/else test
    elIf2(x)        ### final test or otherwise ###
    print()

### Testing values and area follow: ##
##
##print("[zero value test2:]")    
####x = -1
##x = 0
##x = 999
##x = 1011
##testMyIfs(x)
##print("[zero value test2:]")
##x = 0
##testMyIfs(x)
print("[positive value test3:]")
x = 1
testMyIfs(x)
##
####
##print("[otherwise x invalid value TEST#4:]")
##x = 999
##print(x)
##testMyIfs(x)
##
### note: the test driver area above is a replacement for main()
##    
### Professor Reed uses test cases instead of main()!
##if __name__ == '__main__':
##    main()    
    
