"""
    Default Context Manager

with open('file.txt', 'w') as file:
    file.write('this is tested line')

file = open('file.txt', 'r')
try:
    data = file.read()
    print(data)
except Exception as e:
    print(e)
finally:
    file.close()
"""

"""
    -- Implementing a Context Manager as a Class --

class File(object):

    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()


with File('file.txt', 'w') as file:
    file.write('Hola!')
"""

"""
    -- Implementing a Context Manager as a Generator --

from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, 'w')
    try:
        yield f
    finally:
        f.close()


with open_file('file.txt') as f:
    f.write('hannah')
"""
