f = open('photo.jpg', 'r+')
jpgdata = f.read()
f.close()

'''
3가지 에러 가능성
1. To make sure that the file gets closed whether an exception occurs or not, pack it into a with statement
If you want to read the file, pass in r
If you want to read and write the file, pass in r+
If you want to overwrite the file, pass in w
If you want to append to the file, pass in a

2.open does not allow explicit encoding specification in Python 2.x. However, the function io.open is available in both Python 2.x and 3.x (where it is an alias of open), and does the right thing.

3. you must rely on metadata (for example, in HTTP headers) to know the encoding. Increasingly, formats just define the encoding to be UTF-8.
'''

import io
with open('photo.jpg', 'rb') as inf:
    jpgdata = inf.read()

if jpgdata.startswith(b'\xff\xd8'):
    text = u'This is a JPEG file (%d bytes long)\n'
else:
    text = u'This is a random file (%d bytes long)\n'

with io.open('summary.txt', 'w', encoding='utf-8') as outf:
    outf.write(text % len(jpgdata))