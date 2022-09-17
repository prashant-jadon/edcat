import requests
import pyrebase
import requests

config = {
    "apiKey" : "AIzaSyAetMmzyqpksGjdvXbYVAk5gWmEdH4GC1I",
    "authDomain" : "unseen1-1.firebaseapp.com",
    "databaseURL" : "https://unseen1-1-default-rtdb.firebaseio.com",
    "projectId" : "unseen1-1",
    "storageBucket" : "unseen1-1.appspot.com",
    "messagingSenderId" : "336843569987",
    "appId" : "1:336843569987:web:76be1bbee6a4e8098a8df6",
    "measurementId" : "G-REW7MW4FZB",
    "serviceAccount": "service_acc.json"
}

print("""
<!DOCTYPE html>
<html lang="en">
  
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content=
        "width=device-width, initial-scale=1.0">
    <title>navbar</title>
    <style>
        ul {
            list-style-type: none;
            margin-top : 10px ;
            padding-left : 20px;
            padding-right : 20px;
            border-radius : 25px;
            overflow: hidden;
           height : 80vh;
           overflow-y:scroll;
        }
  
        li {
            
               background-color: white;
    margin: 20px;
    
    align-content: center;
    color: black;
    padding: 10px;
    box-shadow: 5px 10px;
        }
  
        li a {
            display: block;
            color: black;
            text-align: center;
            padding: 14px 16px;
            text-decoration: none;
            
        }
  
        li a:hover {
            background-color: lightgreen;
            color: black;
        }
        work {
           text-align:center;
           font-weight:500;
           color: black;
        }
        body{
        background-color:#caecfd;
        }
        work h3{
             text-align: center;
        }
    </style>
</head>
  
<body>
   <div class ="work" ><h3> VIDEOS </h3> </div>
   
    <ul>
""")

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
files = storage.child("images").list_files()
for file in files:
    file1 = open('files_to_download.txt', 'r')
    Lines = file1.readlines()
    count = 0

    # Strips the newline character
    for line in Lines:
        count += 1
        temp = line.strip()
        name = line.replace("https://firebasestorage.googleapis.com/v0/b/unseen1-1.appspot.com/o/", "")
        nameofthefile = file.name
        z = storage.child(file.name).get_url(None)
        new_name = name.replace("%2F","%252F")
        new_name2 = new_name.replace("%20","%2520")
        new_name3 = new_name2.replace("?alt=media","%3Falt%3Dmedia%0A")
        #print(new_name3)


        print('<li><a href="http://192.168.234.196:8000/'+ new_name3 +".mp4"+ '"' + '>'+"Chapter"+'<li>')
print("""
</ul>
</body>
</html>
""")
