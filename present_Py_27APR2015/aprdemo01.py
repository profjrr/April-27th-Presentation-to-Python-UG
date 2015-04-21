### Begin Ifs in Python:
##
### Python ifs presented by Professor Reed
### last updated (20-APR-2015)
### for Python 3.4+
### Featured Speaker -- Python User Group -- Apr. 2015
##
##
##import string

def simpleIf(x):
    print("Demo Simple IF Demo*: ")
    if x < 0:
        print("simple if test ran:", x)
        print("x is less than 0")
    print("end of Simple IF Demo*: ")
    print ("Doesn't meet NASA/JPL Stds")
    print()

def ifWithElse(x):
    ## What is wrong with this one??? ##
    print("Demo IF_WITH_ELSE only! Demo**: ")
    if x < 0:
        print("with else test ran:", x)
        print("x is less than 0")
    else:
        print("else x determines x is greater than a negative value")
    print("end of Demo**: ")
    print ("Doesn't meet NASA/JPL Stds")
    print()
    
def elseIf(x):
    print("Demo ELIF Demo***: ")
    if x < 0:
        print("with else elseif:", x)
        print("x is less than 0")
    elif x == 0:
        print("elseif x is equal to zero")
    else:
        print("elif final else x is greater than a negative value not ZERO!")
    print("end of Demo***: ")
    print ("===> DOES meet NASA/JPL Stds <===")
    print()     

##        
##       
### --- Professor Reed's test driver area --- ###
##
    
def testMyIfs():
### Part II ###   
##    x = -1
##    x = 0
    x = 1
    print()
    print("x is: ", x)
    ##        
    print()
    print("the value of x is: ", x)
    print()
    ##
    simpleIf(x)     ## first demo   -- simple if test
    ifWithElse(x)  ## second demo -- if/else test
    elseIf(x)       ## third demo   -- if/elif/else test
    print()

testMyIfs()
### note: the test driver area above is a replacement for main()
##    
### Professor Reed uses test cases instead of main()!
##if __name__ == '__main__':
##    main()    
    
