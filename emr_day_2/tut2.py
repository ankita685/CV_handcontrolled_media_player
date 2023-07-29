import numpy as np
f =np.ones([5,5])
f[1:4,1:4] =np.zeros((3,3))
f[2][2] =9
print(f)

a = np.array([1,2,3])
b=a
b[0] =8
print(a[0])

a = np.array([1,2,3])
b=a.copy()
b[0] = 7
print(a[0])

a = np.array([1,2,3])
b= np.array([4,5,6])
print(np.add(a,b))
print(np.multiply(a,b))
print(np.divide(a,b))
print(np.sqrt(a))


d = np.array([[1,2,3],[3,4,5]])
print(d)
print(d.T)
print(np.sum(d))
print(np.sum(d,axis =0))
print(np.sum(d,axis =1))