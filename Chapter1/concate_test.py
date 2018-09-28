"""
learn difference of concate and append
"""


def list_concatenate(caps):
    print('before concatenate, in func, id =', id(caps))
    caps = caps + ['END']
    print('After concatenate, in func, id =', id(caps))
    print(caps)


def list_append(caps):
    print('before append, in func, id =', id(caps))
    caps.append('END')
    print('After append, in func, id =', id(caps))
    print(caps)


capB = capA = ['F', 'F', 'B']
print('the id of capA is ', id(capA))
list_concatenate(capA)
print(capA)
print('the id of capB is ', id(capB))
list_append(capB)
print(capB)

"""
"""""""OUT PUT""""""""
the id of capA is  4638679560
before concatenate, in func, id = 4638679560
After concatenate, in func, id = 4639744776
['F', 'F', 'B', 'END']
['F', 'F', 'B']
the id of capB is  4638679560
before append, in func, id = 4638679560
After append, in func, id = 4638679560
['F', 'F', 'B', 'END']
['F', 'F', 'B', 'END']
"""
