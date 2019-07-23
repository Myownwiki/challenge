# challenge
This project "helloworld" has been  developed in python-django restframwork.
Deployed using docker and docker compose
DB is sqlites 
You can access the rest API through 

http://ip:8000/hello/users/?format=json for user listing and post request
http://ip.173:8000/hello/<username>/?format=json for listing one user and get, put and delete request using postman



For production
================
we will use Postgress/mysql RDS and Helmchart for packaging
We will use jenkins-file for building and deploying the project on kubernetes


