## Poor's Man Twitter implementation by Johnny Fang

#### requirements
Build a "Poor Man's Twitter" application in a single web page. The page consists of 2 pieces of functionality on the URL '/'.

1) The ability for any visitor to tweet. A tweet consists of a 50 character text input, a datetime that automatically records the time of a message and a name. Visible form fields for a tweet are the tweet and the name, which must be aligned horizontally to one another.
The ability to display all tweets (unpaginated) in a table . Show the time of the tweet, the message and the name. Sort the table using only the time and name columns.

2) The tweet form should appear at the top of the page. The tweets table should appear underneath the form. The process of adding a tweet must be asynchronous.

No login is required in order to tweet.

#### Stack
* Python 3
* Django 3.0+ (backend)
* Django Rest Framework
* Vue
* Bootstrap  / JQuery
* SQLite (Django default settings)

#### Run
 # Create a virtual environment to isolate our package dependencies locally   
`python3 -m venv env`   
`source env/bin/activate`  # On Windows use   `env\Scripts\activate`   

 # install dependencies   
`pip install -r requirements`

 # run migrations   
`python manage.py migrate`  

 # run dev server   
`python manage.py runserver 8000`

#### Tests
 # run all tests   
`pytest ` 

 # launching pytest for specific test(s)   
`pytest twitter_app/tests/test_models.py`
