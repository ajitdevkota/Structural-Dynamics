#LOOP PREPARATION FOR PIECEWISE EXACT METHOD

import numpy as np

t = np.arange(0,1,0.2)
f = t+1
print ('t:{one} f:{two}'.format(one = t, two = f))
print ('t[0]={one} f[0]={two}'.format(one = t[0], two = f[0]))
print ()

def response(x, y):

    #Initial Conditions:
    u = 0
    v = 0


    nPoints = len(x)
    print('No. of points is {one}.'.format(one=nPoints))

    n = 0

    for j in range(nPoints): #1
        print ('t{a}={b}'.format(a=n, b=x[n]))
        n = n + 1

    print ()

    n = 0

    for k in t: #2: same as 1
        print ('t{a}={b}'.format(a=n, b=x[n]))
        n = n + 1

    print ()

    n = 0


    result =[]

    for n, k in enumerate(t): #3 same as 1 and 2
        #print ('t{a}={b}, t{c}={d}'.format(a=n, b=x[n], c=n+1, d=x[n+1])) # Basically x[n+1] doesn't exist for last array

        if (n<len(x)-1):
            print('t{a}={b}, t{c}={d}'.format(a=n, b=x[n], c=n+1, d=x[n+1])) # print(x[n], x[n+1])
        else:
            print('t{a}={b}, t{c}={d}'.format(a=n, b=x[n], c=n+1, d=0)) # x[n+1]=0

        if (n<len(x)-1): # if statement here just to avoid out of range error (fix later)
            current_operation = x[n] + x[n+1] + u + v
            print(current_operation)
            result.append(current_operation)

            #Update Initial Conditions:
            u = u + 1
            v = v + 1


        else:
            current_operation = x[n] + 0 + u + v
            print(current_operation)
            result.append(current_operation)
            
            #Update Initial Conditions:
            u = u + 1
            v = v + 1
         
    print()
    print('Result:::{}'.format(result))

    return t

result = response (t, f)
