# The function ReducedForms(D) below computes all reduced binary quadratic forms of the negative discriminant D

from math import sqrt

def IsEven(m):
    return not m%2

def IsFundamental(D):
    if D%4 == 0 or D%4 ==1:
        return True
    else:
        return False

# I am curious: Are there more efficient versions of the following function?

def ListDivisors(m):               
    outl,outr = [],[]
    for i in range(1,int(sqrt(abs(m))+1)):
        if m%i==0:
            outl = outl + [i]
            number = abs(m//i)
            if number != i:
                outr = [number] + outr
    return outl + outr

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
        forms=ReducedForms(i)
        if len(forms)==1:
            print i, " Corresponding reduced form: ",forms[0]