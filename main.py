
def make_simple_html(title, bodytext):
 html = """
 <!DOCTYPE html>
 <html>
 <head>
 <title>Page Title</title>
 </head>
 <body>

 <h1>%s</h1> 
 <p>%s</p>

 </body>
 </html> 
 """   %(title,bodytext)  #title from paramemter is referenced to %s

"""
 f = open("index.html", "w")
 f.write(html)
 f.close()

make_simple_html("New Title!", "This is content")
""" 
#=============================================
haiku1 = {
    "title" : "Jan",
    "poem" : """ content of poem1"""
}

haiku2 = {
    "title" : "Oct",
    "poem" : """ content of poem2"""
}

haiku3 = {
    "title" : "Nov",
    "poem" : """ content of poem3"""
}

haikus = [haiku1, haiku2, haiku3]
#=============================================================================
def make_head(title):
    return """ <head>
 <title>%s</title>
 </head> """% title

#=============================================================================
def make_haiku_page(haiku):
 head = make_head(haiku["title"]) 
 html = """
 <!DOCTYPE html>
 <html>
%s
 <body>

 <h1>%s</h1> 
 <p>%s</p>

 </body>
 </html> 
 """   %(head, haiku["title"],haiku["poem"])  #title from paramemter is referenced to %s

 #f = open("index.html", "w")
 f = open(haiku["title"] + ".html", "w") #create html file 
 f.write(html)
 f.close()

"""
#make_haiku_page(haiku1)

#generate a series of haku pages
for haiku in haikus:
    make_haiku_page(haiku)
"""
#===========================================================================
def poem_links(haikus):
    return """<li> <a href="Jan.html" > Jan </a> </li>"""

def poem_links2(haikus):
    list_code = ""
    for haiku in haikus:
        list_code += """  <li> <a href="%s.html" > %s </a> </li>  """ %(haiku["title"],haiku["title"])
    return list_code

#===========================================================================
def make_main_page():
 head = make_head("List of Haiku Poems")
 html = """
 <!DOCTYPE html>
 %s
 <body>

 <h1>List of Haikus</h1> 
 <ul> 
 <!--   <li>  <a href="Jan.html"> Jan </a>  </li>  -->
 %s
 </ul>

 </body>
 </html> 
 """ % ( head, poem_links2(haikus) )

 #f = open("index.html", "w")
 f = open("index.html", "w") #create html file 
 f.write(html)
 f.close()

#======================================================================
#main code
#start main page
make_main_page()

#generate a series of haku pages
for haiku in haikus:
    make_haiku_page(haiku)