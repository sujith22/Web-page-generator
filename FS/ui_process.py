#!/usr/bin/python3
import cgi,cgitb
f = open("company.txt","w")
form = cgi.FieldStorage()

# Fetching all info
company_name = str(form.getvalue("company_name"))

home_para_body = str(form.getvalue("home_para_body"))
footer = str(form.getvalue("footer"))
about_para = str(form.getvalue("about_para"))
# services
service1 = str(form.getvalue("service_1"))
service1_desc = str(form.getvalue("service_1_desc"))
service2 = str(form.getvalue("service_2"))
service2_desc = str(form.getvalue("service_2_desc"))
service3 = str(form.getvalue("service_3"))
service3_desc = str(form.getvalue("service_3_desc"))
# services end
# contact us
street_name = str(form.getvalue("street_name"))
city_name = str(form.getvalue("city_name"))
state_name = str(form.getvalue("state_name"))
pin_code = str(form.getvalue("pin_code"))
address = str(form.getvalue("address"))
phone= str(form.getvalue("phone"))
mail = str(form.getvalue("mail"))
# social media
fb = str(form.getvalue("facebook_link"))
twitter = str(form.getvalue("twitter_link"))
gplus = str(form.getvalue("google_link"))
#End of fetching all info
#writing home
f.write("HOME###")
f.write("TITLE|"+company_name+"###")
f.write("PARA|WHAT WE DO!!!|"+home_para_body+"###")
f.write("FOOTER|"+footer+"###\n")
#writing home end
#writing about page
f.write("ABOUT###")
f.write("PARA|ABOUT US|"+about_para+"###\n")
#writing about page end
# services page
f.write("SERVICES###")
f.write("SERVICE1|"+service1+"|"+service1_desc+"###")
f.write("SERVICE2|"+service2+"|"+service2_desc+"###")
f.write("SERVICE3|"+service3+"|"+service3_desc+"###\n")

#writing contact us page
f.write("CONTACT###")
f.write("ADDRESS|"+street_name+"|"+city_name+"|"+state_name+"|"+pin_code+"###")
f.write("PHONE|"+phone+"###")
f.write("MAIL|"+mail+"###\n")
# contact us page ends
# social media
f.write("SOCIAL###")
if(fb!="None"):
    f.write("FB|"+fb+"###")
if(gplus!="None"):
    f.write("GPLUS|"+gplus+"###")
f.write("TWITTER|"+twitter+"###")

f.close()
# writing contact us page end
print("Content-type: text/html")
print()
full_html= '''<!DOCTYPE html>
  <html>
    <head>
      <!--Import Google Icon Font-->
      <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
      <link href="https://fonts.googleapis.com/css?family=Do+Hyeon|Gugi" rel="stylesheet">
      <!--Import materialize.css-->
       <!-- Compiled and minified CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-beta/css/materialize.min.css">

    <!-- Style -->
    <style>
        body{
            font-family: 'Gugi', cursive;   
            font-size:30px;
        }
       h1,h2,h3,h4{
            font-size:50px;
            font-family: 'Do Hyeon', sans-serif;
        }
        h1{
            font-size: 75px;
        }
    </style>
   
            <title>Success</title>

      <!--Let browser know website is optimized for mobile-->
      <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    </head>

    <body class="black">
        <div class="container">
            <h1 class="indigo-text text-darken-1 center-align"> Hurray<span class="blue-text text-darken-2">!!!! </h1>
                <h2 class="purple-text center-align">
                    Your File is ready and saved in <span class="red-text">"company.txt"</span>
                </h2>
            
                <div class="center-align">
                    <a class="btn waves-effect waves-light btn-large" href="http://localhost/cgi-bin/FS/page_view.py" target="_blank">Click here to view it
                    </a>
                    
                </div>
            </div>
            <hr>
            <hr>
            <div class=" container center-align">
                
                <h2 class="white-text">Click the following button to start processing it into html files</h2>
                <a class="waves-effect waves-light btn-large blue" href="http://localhost/cgi-bin/FS/process_page.py" target="_blank">Process it</a>
            </div>
        </div>
        <br>
        <hr>
        
      <!--JavaScript at end of body for optimized loading-->
       <!-- Compiled and minified JavaScript -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-beta/js/materialize.min.js"></script>
    </body>
  </html>
        '''
print(full_html)

# <a class="waves-effect waves-light btn-large red" href="http://localhost/cgi-bin/FS/editor.py" target="_blank">CLICK HERE TO EDIT IT</a>