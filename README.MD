                                                       IS211 Course Project
###############################################################################################################
# BOOK CATALOGUE APPLICATION 
This application allows users to log in and search books by either ISBN# or the Title then save the results to their personal book catalogue application. The root URL used for this app is http://127.0.0.1:5000/ and it is the website that launch an interactive web application. It utilizes Flask and SQLite3 to create a very interesting interface. The application is built to establish query against the google book api and display the results. The successful query will allow users to add books to their book store. Also, the users can delete/add books as they wish. 

## Requirements
- Python version 3               
- Flask==1.0.3           
- validators==0.13.0     
- requests==2.22.0       


## Setup Repo
```
Option one:
# git clone https://github.com/IS211_Course_Project
# cd IS211_Course_Project
# pipenv shell
# pip install -r requirements.txt
# python load_schema.py
# python app.py

or option two:
# virtualenv -p python3 /. 
# source bin/activate
# git clone https://github.com/IS211_Course_Project
# cd IS211_Course_Project
# pip install -r requirements.txt
# python load_schema.py
# python app.py

```
Note this application was tested in python3, so make sure you are running it on python version 3 or make the necessary changes to accomodate python version 2.


## Permitted users
```
_____________________
|username | password |
|____________________|
|admin 	  | password |
|____________________|
|user1    | myapp    |
|____________________|
|jojo	  | myapp    |
|____________________|
```









