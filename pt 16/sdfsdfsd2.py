import re
result = re.sub(r'Python', 'Hello world', 'This is a Wiki page. Users with edit rights can edit it. You are therefore free to (in fact,encouraged to) add details of material that other Python users will find useful. It is not anadvertising page and is here to serve the whole Python community. Users who continually editpages to give their own materials (particularly commercial materials) prominence, or spam the')
print(result)

resultt = re.match(r'Python', 'This is a Wiki page. Users with edit rights can edit it. You are therefore free to (in fact,encouraged to) add details of material that other Python users will find useful. It is not anadvertising page and is here to serve the whole Python community. Users who continually editpages to give their own materials (particularly commercial materials) prominence, or spam the')
print(resultt)
