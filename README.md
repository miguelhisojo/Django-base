# Django user management

Today app deployment must be fast and simple. Having aplications that we can actually reuse to start new projects is necessary, since time is money.
This repository is aim to be a base for any user based application, containing the basics of any application, it is aimed to be flexible to
allow any developer to start creating any application on top of it.

This repository contains the basics of any django app
  - User registration
  - User Login/Logout
  - User Profile
  
 # How to use this repository 

## Clone this repository in your terminal.

 git clone https://github.com/miguelhisojo/Django_App_Base.git
 
## Create a MySQL configuration file
  
 The application uses MySQL engine, a config file has been created separately, for the development environment, but for production,
 is better to set environment variables.
 
 MySQL conf file structure:
  
# file_mysql.cnf  </br>
[client]</br>
database = *your_database_name*</br>
user = *your_user_name*</br>
password = *your_password*</br>
host = *localhost*</br>
port = *3306*</br>

## Create tables 
 python manage.py makemigrations
 python manage.py migrate

## Test it

  python manage.py runserver
  
  click on Register and create a user account on your database



# You are all set!

## Sart builing your apps

To create a new app you only need to start it with django

- python manage.py startapp **your_app_name**

