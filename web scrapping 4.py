from urllib import request
url="https://moz.com/top500"
name=urlopen(Request(url,headers=("User-Agent"="/Mozilla/5.0")))      # request to open profiles url
webpage_as_bytes=name.read()


##u=url.find('"',0)
##st=u
##st+=1
##ed=url.find("/profiles",st)
##absolute_link=url[st:ed]
##print(absolute_link)



##profiles_html=webpage_as_bytes.decode("cp1252")
profiles_html=webpage_as_bytes.decode("utf-8")
print(profiles_html)

##startindex=0
o=profiles_html.find('href')       
for i in range (profiles_html.count('href')):
    startindex=o+1    
    o=profiles_html.find('"',startindex)   
    startindex=o+1    
    endindex=profiles_html.find('"',startindex)
    print (startindex,endindex)
    print(profiles_html[startindex:endindex])
    o=profiles_html.find('href',endindex)         
