#   TO STORE SENSITIVE INFORMATIONS LIKE PASSWORDS, APIKEYS, TOKENS WE USE ENV VARIABLES IN PYTHON
#   BY USING ENV VARIABLES, WE CAN IMPROVE SECUTITY WITHOIUT EXPOSING(HARDCODING) SENSITIEV VALUES
#   TO VIEW ENV IN THE SYSTEM     --> env
#   TO USE ENV VARIABLES IN CODE  --> import os
#   TO INVOKE ENV VARS IN CODE    --> os.getenv("password")
#   Before that we need to export those values to invoke them
#   $env:username = "admin"
#   $env:password = "vmadmin@1234"
#   $env:apikey = "kjfbsjhfbsjefhilerhgiuerhgiler"
#   By default by using export command, we can export in LINUX
#   export DB_USERNAME="admin"
#   By default by using set command, we can export in WINDOWS
#   set DB_USERNAME=admin

import os   # By using os module, we can invoke env variables in the code

db_username = os.getenv("username")
db_password = os.getenv("password")
db_apikey   = os.getenv("apikey")

print(db_username)
print(db_password)
print(db_apikey)

