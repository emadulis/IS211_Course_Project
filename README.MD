                                                       IS211 Course Project
#############################################################################################################################################################

# BOOK CATALOGUE APPLICATION 
This application allows users with access only to log in and search books by either ISBN# or the Title then save the results to their personal book catalogue application. The root URL used for this app is http://127.0.0.1:5000/ and it is the website that launch an interactive web application. It utilizes Flask and SQLite3 to create a very interesting application. The application is built to establish query against the google book api and display the results. Once user successfuly query the book they wanted to add to their book store they will have an option to add the item into their book store. Also, the users can delete thier book from the app if they no longer own it or need it. 

## Requirements.txt
   astroid==2.2.5
   autopep8==1.4.4
   certifi==2019.3.9
   chardet==3.0.4
   Click==7.0
   decorator==4.4.0
   Flask==1.0.3
   idna==2.8
   isort==4.3.20
   itsdangerous==1.1.0
   Jinja2==2.10.1
   lazy-object-proxy==1.4.1
   MarkupSafe==1.1.1
   mccabe==0.6.1
   pycodestyle==2.5.0
   pylint==2.3.1
   requests==2.22.0
   six==1.12.0
   typed-ast==1.3.5
   urllib3==1.25.2
   validators==0.13.0
   Werkzeug==0.15.4
   wrapt==1.11.1

## Setup Repo
```
virtualenv -p python3 /.
source bin/activate
git clone https://github.com/IS211_Course_Project
cd IS211_Course_Project
pip install -r requirements.txt
python app.py
```
Note this application was tested in python3, so make sure you are running it on python version 3 or make the necessary changes to run in on python version 2


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









