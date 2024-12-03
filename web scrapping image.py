from urllib import request
url="http://olympus.realpython.org/profiles"
name=request.urlopen("http://olympus.realpython.org/profiles/dionysus")   # request to open image url
webpage_as_bytes=name.read()
profiles_html=webpage_as_bytes.decode("cp1252")
##profiles_html=webpage_as_bytes.decode("utf-8")
##print(profiles_html)

#----------code for finding absolute link in html----------------------------------------------------------------------------------------------------------------------

u=url.find('"',0)
st=u+1
ed=url.find("/profiles",st)
absolute_link=url[st:ed]
print(absolute_link)

#-----------code for finding ---------------------------------------------------------------------------------------------------------------------------------------

o=profiles_html.find('img src',0)
for j in range(profiles_html.count('img src')):
    startindex=o+1
    o=profiles_html.find('"',startindex)
    startindex=o+1
    endindex=profiles_html.find('"',startindex)
    i=profiles_html[startindex:endindex]
    print (i)
    o=profiles_html.find('img src',startindex)

    link=absolute_link+i
    print(link)
    profiles_html=profiles_html.replace(i,link)

#-----------code for downloading image---------------------------------------------------------------------------------------------------------------------------------

imgURL="http://olympus.realpython.org/static/dionysus.jpg"
webcon=request.urlopen(imgURL)
dionysusIMG=webcon.read()
a=type(dionysusIMG)
print (a)

imgfile=open("C:\\Users\\Ayesha S\\Desktop\\dionysusIMG.JPG","wb")
img=imgfile.write(dionysusIMG)
print(img)
imgfile.close()

imgURL="http://olympus.realpython.org/static/grapes.png"
webcon=request.urlopen(imgURL)
grapesIMG=webcon.read()
a=type(grapesIMG)
print (a)

imgfile=open("C:\\Users\\Ayesha S\\Desktop\\grapesIMG.JPG","wb")
img=imgfile.write(grapesIMG)
print(img)
imgfile.close()

#----------code for writing html file and saving it---------------------------------------------------------------------------------

name_of_file="C:\\Users\\Ayesha S\\Desktop\\olympus files.html"
f=open("C:\\Users\\Ayesha S\\Desktop\\olympus files.html","w")
fs=f.write(profiles_html)
f.close()
print (fs)
