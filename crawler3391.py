# a

import urllib2
import bs4

f = open("/Users/tl/Development/CS3391/TODO.html", 'w+')
sid = ""
request1 = urllib2.Request("http://acm.cs.cityu.edu.hk/oj2/index.php/u/" + sid)
request2 = urllib2.Request("http://acm.cs.cityu.edu.hk/oj2/index.php/u/53062882")
response1 = urllib2.urlopen(request1)
response2 = urllib2.urlopen(request2)
soup1 = bs4.BeautifulSoup(response1, 'lxml')
soup2 = bs4.BeautifulSoup(response2, 'lxml')

list_a = []
list_b = []
for a in soup1.findAll('tr'):
    if (a.has_attr('class') and ('verdict-handle-AC' in a['class']) and ('submission-purpose-1' in a['class'])):
        for b in a.findAll('a'):
            if ('/p/' in b['href']):
                list_a.append(b['href']);

for a in soup2.findAll('tr'):
    if (a.has_attr('class') and ('verdict-handle-AC' in a['class']) and ('submission-purpose-1' in a['class'])):
        for b in a.findAll('a'):
            if ('/p/' in b['href']):
                list_b.append(b['href']);

set_a = set(list_a)
set_b = set(list_b)
list_todo = list(set_a - set_b)

f.write('<html>\n')
f.write('<body>\n')
f.write("<h2> total number: " + str(len(list_todo)) + " <h2>")
list_todo.sort()
for i in list_todo:
    z = i.split('/')
    t = z[len(z) - 1]
    f.write("<p> <a href='http://acm.cs.cityu.edu.hk/" + i + "'> Problem number: " + t + "</a> </p> \n")
f.write('</body>\n')
f.write('</html>\n')