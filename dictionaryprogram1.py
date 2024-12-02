emp = {'id':100 , 'name':'ram' , 'salary':10000, 'designation': 'Assistant Engineer'}
e1 = emp.copy()
print(e1)
e1.update({'age':24})
print(e1)
print(e1.keys())
print(e1.values())
print(e1.items())
print(e1.get('designation'))
s=[1,2,3]
print(e1.fromkeys(s,'a'))

