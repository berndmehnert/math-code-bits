# The function ReducedForms(D) below computes all 'reduced' positive definite binary quadratic forms of the negative discriminant D

from math import sqrt

def IsEven(m):
    return not m%2

# Lets compute quickly a list of divisors of a number m

def ListDivisors(m):               
    outl,outr = [],[]
    for i in range(1,int(sqrt(abs(m)) + 1)):
        if m%i==0:
            outl = outl + [i]
            number = abs(m//i)
            if number != i:
                outr = [number] + outr
    return outl + outr

# Is m squarefree?

def IsSquarefree(m):
    if abs(m) == 1:
        return True
    listdiv = ListDivisors(m) 
    listdiv = listdiv[1:len(listdiv)] # Throw away 1 as a divisor
    counter = 0
    while listdiv[counter] <= sqrt(abs(m)):
        if m%listdiv[counter]**2 == 0:
            return False
        counter += 1
    return True

# Is D a fundamental discrimminant?

def IsFundamental(D):
    if D%4 == 0:
        if IsSquarefree(D//4):
            return True
        else:
            return False
    else: 
        if D%4 == 1:
            if IsSquarefree(D):
                return True
            else:
                return False
        else:
            return False

# The algorithm used in the main function goes back to C.F. Gauss. It is beautifully explained f.e. in the book "A Brief Guide to Algebraic Number Theory" by H.P.F. Swinnerton-Dyer

def ReducedForms(D):
    out = []
    if IsFundamental(D) and D<0:
        root=int(sqrt(-D/3))
        b_array = range(-root,root+1)
        for b in b_array:
            if IsEven(b-D):
                number=(b**2-D)//4
                listdiv=ListDivisors(number)
                for a in listdiv:
                    c = number//a
                    if a==c:
                        if b>=0:
                            out = out + [[a,b,c]]
                    else:
                        if c>=a and a>=b and b>-a:
                            out = out + [[a,b,c]]
    return out

# Let us now plot out a famous list of discriminants. It was conjectured by Gauss and later proven that the list is complete in the sense that there are no other discriminants 
# for which we have exactly one reduced form.

for i in range(-1000,0):
    if IsFundamental(i):
        if len(ReducedForms(i)) == 1:
            print i
