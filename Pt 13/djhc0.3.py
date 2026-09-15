import re

li = ['9723678262']
 
for val in li:
    if re.match(r'[8-9]{1}[0-9]{9}', val) and len(val) == 10:
            print('yes')
    else:
            print('no')
