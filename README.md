# TurboGym - a Flask app using Python and connecting to a relational database using PostgreSQL. 

INSTRUCTIONS >>
---------------
-----------------------------------------
** FROM APP ROOT DIRECTORY (turbo_gym) **
-----------------------------------------

CREATE THE DATABSE:
-------------------
in Terminal: 

createdb turbo_gym



CONNECT THE .sql FILE TO THE DATABASE USING PostgreSQL
-----------------------------------------------------
in Terminal: 

psql -d turbo_gym -f db/turbo_gym.sql



SEED THE DATABASE USING THE console.py FILE
-------------------------------------------
in Terminal"

python3 console.py


OPEN THE APP USING FLASK
------------------------
in Terminal:

flask run


>> open localhost:5000 in your browser to view website
(you can also cmd+click the link provided by flask after using 'flask run' command. 
