### Begin Ifs in Python:
##
### Python ifs presented by Professor Reed
### last updated (11-DEC-2014)
### for Python 3.4+
### Lighting Talks -- Python User Group -- Feb. 2015 Meeting
##
## ID: lightIFdemos.py -- demo
##
import string

def simpleIf(x):
    print("Trial 01: ")
    if x < 0:
        print("simple if test ran:", x)
    print("end of Trial 01: ")
    print()

def ifWithElse(x):
    print("Trial 02: ")
    if x < 0:
        print("with else test ran:", x)
    else:
        print("else x determines x is greater than a negative value")
    print("end of Trial 02: ")
    print()
    
def elseIf(x):
    print("Trial 03: ")
    if x < 0:
        print("with else elseif:", x)
    elif x == 0:
        print("elseif x is equal to zero")
    else:
        print("elseif final else x is greater than a negative value")
    print("end of Trial 03: ")
    print()    

def simpleifalpha(x):
    print("Trial 04: ")
    if str.isalpha(x):
        print("simple if alpha test ran:", x)    
    print("end of Trial 04: ")
    print()
    
def simpleifnumeric(x):
    print("Trial 05: ")
    if str.isnumeric(x):
        print("simple if numeric test ran: ", x)
    print("end of Trial 05: ")
    print()    
       
def lowercasecheck(x):
    print("Trial 06: ")
    if str.islower(x):
        print("if lowercase found: ", x)
    else:
        print("x is not lowercase: ", x)
    print("end of Trial 06: ")
    print()
    
def caseChkelif(x):
    print("Trial 07: ")
    if str.islower(x):
        print("if case chk found lowercase: ", x)
    elif str.isupper(x):
        print("x is UPPERCASE by case chk: ", x)
    else:
        print("x is something other: ", x)
    print("end of Trial 07: ")
    print()        
##        
##       
### --- Professor Reed's test driver area --- ###
##        
def testMyIfs():
##    
### Part I ###
    ### comment out the current demo ###
    ### un-comment the next demo ###
###    
    x = 'c' ## x is assigned lower case 'c' value -- demo 1
##    x = 'C' ## x is assigned upper case 'C' value -- demo 2
##    x = '22' ## x is assigned a value of 22 -- demo 3
##    
## end of demos from Feb. 23rd meeting 2015    
##    
### Part II ### -- future demos
##    x =  22 ## x is assigned a numeric value of 22 -- demo 4
##    x = -22 ## neg x is assigned value of -22 -- demo 5
##    
##    x = -1   ## demo 6
##    x = 0    ## demo 7 
##    x = 1    ## demo 8
##    print()
##    print("x is: ", x)
##        
    print()
    print("the value of x is: ", x)
    print()
    ##
##    simpleIf(x)
##    ifWithElse(x)
    simpleifalpha(x)
    simpleifnumeric(x)
    lowercasecheck(x)
    caseChkelif(x)
    print()

### note: the test driver area above is a replacement for main()
##    
### Professor Reed uses test cases instead of main()!
##if __name__ == '__main__':
##    main()
testMyIfs()

    
    
