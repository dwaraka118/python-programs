from array import *
vals = array('i',[-1,5,7,70,89])
print(vals)
print(vals.buffer_info())
vals.reverse()
print(vals)
for i in range(len(vals)):
    print(vals[i])
