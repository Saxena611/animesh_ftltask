# BACKEND TEST - FULLTHROTTLE LABS

_DATABASE    - SQLite , DEPLOYMENT  - HEROKU_

Design implemented a django application with User and ActivityPeriod model , wrote custom management command for populating dummy data into the model and created an API to serve the same data in the required format.

## Custom Management Command :

### insert_user

- The command takes exactly one argument as total number of user needs to be created .
- The command returns the random user string created with output message as User "<RANDOM STRING>" Created !.
- Sample Command : python manage.py insert_user 1

### insert_activity
- The command takes 2 argument as input i.e. user_id and number of random activity to be logged .
- The command populates dummy activity for the user which is based on a simple logic i.e. start_time becomes system time and end time is one hour added to system time.
- Sample Command : python manage.py insert_activity vqTblDpDbmqj 2
- Output : Random "<USER-STRING>" activity logged !.


## Model Description:

### User :
- Overriding existing user model with adding columns real_name and tz.

### ActivityPeriod:
- User as Foreign Key with user.id as reference and on_delete.CASCADE.
- session_date as Datefield (format : YYYY-MM-DD).
- start_time and end_time as TimeField (format : HH:MM:SS).
- session_date,start_time,end_time with constraints such as auto_now_add=False,auto_now=False so that framework does not adds corresponding system time into database.

## View & Request :

### Post
_https://animesh-ftltask.herokuapp.com/api/loguseractivity/_

> Input : {"id_list" : ["W012A3CDE", "W07QCRPA4"]}

{% hint style="info" %}
Field : id_list 
Description: The id of user whose session activity log needs to be retrieved.
Requried : True
{% endhint %}


- The post method api retrives the session from the ActivityPeriod model for the provided user.
- The api handles in case the user is not found in database. Also , does basic validation in case no user_id is provided in input.
- Basic validation handling input provided as proper JSON. 
