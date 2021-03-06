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

**Request**

| Field  | Description | Required |
| ------------- | ------------- | ------------- |
| id_list  | The id of user whose session activity log needs to be retrieved  | True  |

> Input : {"id_list" : ["W012A3CDE", "W07QCRPA4"]}

- The post method api retrives the session from the ActivityPeriod model for the provided user.
- The api handles in case the user is not found in database. Also , does basic validation in case no user_id is provided in input.
- Basic validation handling input provided as proper JSON.

**Response**
| Status Code  | Message | Reason |
| ------------- | ------------- | ------------- |
| 200  | Required Json | Data fetch success  |

 Sample Output :
 
 ![Oops ! img not found ](https://user-images.githubusercontent.com/29275475/107840996-48b5b500-6ddd-11eb-990a-47dff0688c5b.png)
 
Output Json:
> {
    "ok": "True",
    "members": [
        {
            "id": "W012A3CDE",
            "real_name": "Egon Spengler",
            "tz": "America/Los_Angeles",
            "activity_periods": [
                {
                    "start_time": "Feb 01 2020 01:33PM",
                    "end_time": "Feb 01 2020 01:54PM"
                },
                {
                    "start_time": "Mar 01 2020 11:11AM",
                    "end_time": "Mar 01 2020 02:00PM"
                },
                {
                    "start_time": "Mar 16 2020 05:33PM",
                    "end_time": "Mar 16 2020 08:02PM"
                }
            ]
        }
    ]
}

### ALLOWED GET
_https://animesh-ftltask.herokuapp.com/api/loguseractivity/_

**Response**
| Status Code  | Message | data |
| ------------- | ------------- | ------------- |
| 200  | data | all data from model   |

>  [ {
        "user": "NIoGZO8ddfCg",
        "start_time": "16:49:54",
        "end_time": "16:49:55"
    },
    {
        "user": "mICzwbjH3b10",
        "start_time": "22:32:17",
        "end_time": "07:32:17"
    }]
    
## Building
- Used pipenv as virtual environment for development . Provided a requirement.txt file for dependency management and project installation.

## Deploy to Heroku
- Used heroku cli for app creation and interface to connect to github and deploy.
