### Begin Ifs in Python:
##
## PgmID: run1part
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
    print ("*** Doesn't meet NASA/JPL Stds, WHY? ***")
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
    print ("*** Doesn't meet NASA/JPL Stds, WHY? ***")
    print()
    
def elseIf(x):
    print("Demo ELIF Demo***: ")
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
    if x < 0:
        print("with else elseif:", x)
        print("x is less than 0")
    elif x == 0:
        print("elif x is equal to zero")
    elif x > 0:
        print("final elif x is greater than a negative value not ZERO!")
    elif x < 1:
        print("final elif x is less than 1")
    elif x == 1:
        print("final elif x is equal to 1")
    else:
        print("otherwise, not a proper value of x?")
##        
    print("end of Demo***: ")
    print ("===> DOES meet NASA/JPL Stds, YES, but better!!! <===")
    print()         

##        
##       
### --- Professor Reed's test driver area --- ###
##
    
def testMyIfs(x):
### Part II ###   
    int(x)
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
    elIf2(x)        ### final test or otherwise ###
    print()

### Testing values and area follow: ##
##
print("[negative value test1:]")
x = -1
testMyIfs(x)
## neg value test
##
##print("[zero value test2:]")
##x = 0
##testMyIfs(x)
##print("[positive value test3:]")
##x = 1
##testMyIfs(x)
####
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
    
