#!/usr/bin/env python
'''
Create a derivative calculation script.
You should issue the degree of the polynomial function, the factors and the script
shall return the first derivative. 
'''

polyDeg = int(input('Provide the degree of the Polynomial Function (e.g. 4 for x^4):'))

p =[]
for i in range(polyDeg, -1, -1):
    coeff=int(input('Factor of X^'+ str(i) + ':'))
    p.insert(0,coeff)




funDegree = len(p)-1
print "The polynominal function you have provided is of Degree %s" %funDegree

origFunc=""
for i in range(funDegree,-1,-1):
    if i == 0:
        origFunc += str(p[i]) 
    elif i == 1:
        origFunc += str(p[i]) +'x'+ '+'
    else:
        origFunc += str(p[i]) + "x^%s"%i +'+'

print "The function you have provided is:%s"%origFunc

result = []
for i in range(0,len(p)):
    derivative = p[i] * i
    result.insert(0,derivative)


result.reverse()
   
finalRes = []
for i in range(len(result)-1,-1,-1):
    if i==0:
        res = 0 
    elif i==1:
        res = '%s'%result[i]
    elif i==2:
        res = "%sx"%result[i]
    else:
        res = '%sx^%s'%(result[i],i-1)
    
    finalRes.append(res)


finalStr=""
max = len(finalRes)-1

for func in finalRes:
    if finalRes.index(func) < max:
        if finalRes.index(func) == max-1:
            finalStr += str(func)
        else:
            finalStr += str(func) + '+' 

print "The derivative of the function you have provided is %s"%finalStr

