BACKEND TEST - FULLTHROTTLE LABS

DATABASE    - SQLite
DEPLOYMENT  - HEROKU

Design implemented a django application with User and ActivityPeriod model , wrote custom management command for populating dummy data into the model and created an API to serve the same data in the required format.

Custom Management Command :

insert_user

1. The command takes exactly one argument as total number of user needs to be created .
2. The command returns the random user string created with output message as User "<RANDOM STRING>" Created !.
3. Sample Command : python manage.py insert_user 1


insert_activity

1. The command takes 2 argument as input i.e. user_id and number of random activity to be logged .
2. The command populates dummy activity for the user which is based on a simple logic i.e. start_time becomes system time and end time is one hour added to system time.
3. Sample Command : python manage.py insert_activity vqTblDpDbmqj 2
4. Output : Random "<USER-STRING>" activity logged !.


Model Description:


