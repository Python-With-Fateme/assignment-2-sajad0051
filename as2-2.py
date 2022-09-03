a=float(input('enter your add?'))
b=float(input('enter your add?'))
num=input('amalgar enter (total(j) vs tafrigh(ta) vs zarb(z) vs taghsim(ta) vs tvan(tv)) ?')
if num=='j':
    print(a+b)
elif num=='tf':
    print(a-b)
elif num=='z':
    print(a*b)
elif num=='ta':
    print(a/b)
elif num=='tv':
    print(a**b)