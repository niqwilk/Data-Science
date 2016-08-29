from bs4 import BeautifulSoup

f = open("LehmanMath.html",'r')
soup = BeautifulSoup(f, 'html.parser')


# find all mailto (email) elements
mailtos = soup.select('a[href^=mailto]')

# prep variables for subsequent stages i process

emails = []



    
# Extract emails        
for i in mailtos:
    if i.string != None:
        emails.append(i.string.encode('utf-8').strip())
        print i.string.encode('utf-8').strip()

