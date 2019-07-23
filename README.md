# Challenge
This project "helloworld" has been  developed in python-django restframwork.
Deployed using docker and docker compose
DB is sqlites 
You can access the rest API through 

http://ip:8000/hello/users/?format=json for user Listing and POST request
http://ip.173:8000/hello/<username>/?format=json for Listing one user and GET, PUT and Delete request using postman
  Post method will be 
  
  http://ip:8000/hello/users/?format=json
  
  Body will be { "username" : "<username>" ,
                  "user_dob" : "<date>"  
               }
  
  
  Validation (For POST method)
  -----------
  1. validation has been added on name (only Alphabets are allowed)
  2. User Dob should be before today's date
  
  Message (GET method)
  -------
  1.If user_dob is today it will print "Today is your Birthday, Happy Birthday !"
  2. ortherwise it will print your Birthday will be in next "deltas " days



For production
================
we will use Postgress/mysql RDS and Helmchart for packaging
We will use jenkins-file for building and deploying the project on kubernetes


