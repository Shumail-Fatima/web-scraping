#---------code to read and save the html file-----------------------------------

from urllib import request
name=request.urlopen("http://olympus.realpython.org/profiles")
webpage_as_bytes=name.read()
profiles_html=webpage_as_bytes.decode("cp1252")
print(profiles_html)
name_of_file="C:\\Users\\Ayesha S\\Desktop\\olympus files.html"
f=open("C:\\Users\\Ayesha S\\Desktop\\olympus files.html","w")
fs=f.write(profiles_html)
f.close()
print (fs)


