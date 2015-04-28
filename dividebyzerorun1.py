### ProfJRR tests to prevent divide by zero with asserts!
##
## PgmID: dividebyzerorun1.py
##
def divide(x, y):
    assert (y!=0), ("### assert found zero ###!")
    try:
        result = x / y
    except ZeroDivisionError:
        print ("division by zero--not good!")
    else:
        print ("result is", result)
    finally:
        print ("executing finally clause")

## MyTestArea: ##
divide(2,1)        
##divide(1,0) ## divide by 0 bad stuff!
