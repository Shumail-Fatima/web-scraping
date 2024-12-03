from urllib import request
url="http://olympus.realpython.org/profiles"
name=request.urlopen(url)      # request to open profiles url
webpage_as_bytes=name.read()
##profiles_html=webpage_as_bytes.decode("cp1252")
profiles_html=webpage_as_bytes.decode("utf-8")
print(profiles_html)

#----------code for finding absolute link in html----------------------------------------------------------------------------------------------------------------------

u=url.find('"',0)
st=u+1
ed=url.find("/profiles",st)
domain=url[st:ed]
print("domain=",domain,"\n")

#------------code for finding the href links in html-------------------------------------------------------------------------------------------------------------------

##startindex=0
o=profiles_html.find('href')        #finds index from where first href is present in code
for i in range (profiles_html.count('href')):       # start a loop for all href in code. (profiles_html.count('href')) counts all the href present in the code.
    startindex=o+1    # this index indicates from where to start reading the code in next line
    o=profiles_html.find('"',startindex)    # to find where '"' starts
    startindex=o+1     # from where '"' starts
    endindex=profiles_html.find('"',startindex)        # to find from startindex where '"' ends after being found at startindex
    ##print (startindex,endindex)           # prints index of where '"' starts and ends
    print("refrence link=",profiles_html[startindex:endindex])          # prints the code written in b/w the start and end of '"', (prints the href link)
    absolute_link=domain+profiles_html[startindex:endindex]
    print ("absolute link=",absolute_link,"\n")
    o=profiles_html.find('href',endindex)         # finds the next href written in code



