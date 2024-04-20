Simple web project on Flask framework with PostgreSQL and Docker Compose

How to start?

1) Open terminal(cmd) and go to the folder with the command "cd" for example:cd C:\Users\Username\Downloads\project
2) Build images for docker compose with the command:docker-compose -f docker-compose.yml build
3) Up containers with the command:docker-compose -f docker-compose.yml up -d
4) When all services will start go to your browser and follow the link:http://localhost
5) If you want open pgadmin follow the link:http://localhost/pg
   login = root@dev.ru; password = postgres
   register new server with random name and establish a connection with these parameters:
   Host name/address = db; Maintenance database = flask_dbname; User name = postgres; Password = postgres;

   All these settings are in the file "docker-compose.yml"
7) Have fun!
