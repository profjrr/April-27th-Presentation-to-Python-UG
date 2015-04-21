#!/usr/bin/python
### Professor Reed: asserting Python assert statements:
## Premature exit of a module with a required return result!!!
## Assumption: code is locked and pre-tested (can run & go only!!!).
##

def KelvinToFahrenheit(KTemperature):
    if KTemperature <=0 : return ### ugly but works with no info???
    assert (KTemperature >= 0),"temp must NOT be Colder than absolute zero!"
    myFtemp = ((KTemperature-273)*1.8)+32
    return (myFtemp)

def testsKtoF():
    print("===test 1===")
    ktemp1 = 273
    print ("Ktemp1:", ktemp1, " Ftemp1:", KelvinToFahrenheit(ktemp1)) ### Zero degrees F
    print()
    print("===test 2===")
    ktemp2 = -5 ### negative value K input
    print ("Ktemp2:", ktemp2, " Ftemp:", KelvinToFahrenheit(ktemp2)) ## Invalid Data!!!
    print()
    print("===test 3===")
    ktemp3 = 505.78
    print ("Ktemp3:", ktemp3, " Ftemp3:", int(KelvinToFahrenheit(505.78))) ### we need this result!!! ###
    print()
    print("===test 4===")
    ktemp4 = -5 ### negative value K input
    print (KelvinToFahrenheit(ktemp4))
    print() ### end of testing for asserts KtoF

testsKtoF()

