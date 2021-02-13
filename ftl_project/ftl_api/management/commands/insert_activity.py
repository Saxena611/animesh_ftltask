from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.utils.crypto import get_random_string
from ftl_api.models import User,ActivityPeriod
from datetime import datetime,timedelta

class Command(BaseCommand):
    help = 'Insert session activity into the model'

    def add_arguments(self, parser):
        parser.add_argument('userid',type=str,help='User whose random activity needs to be stored .')
        parser.add_argument('total',type=int,help='Number of sessions to be inserted .')
    
    def handle(self, *args, **kwargs):
        userid = kwargs['userid']
        total = kwargs['total']
        try :
            # lets get the user
            obj = User.objects.get(id=userid)
        except User.DoesNotExist:
            obj = None
            self.stdout.write(self.style.ERROR('User Not Present in database "%s" !' % (obj)))
            return

        for i in range(total):
            # random adding an hour to current time
            curr = datetime.now()
            endt = curr + timedelta(hours=9)
            # let get it formatted! 2021-02-12
            session_date = curr.strftime("%Y-%m-%d")
            start_time = curr.strftime("%H:%M:%S")
            end_time = endt.strftime("%H:%M:%S")
            # map it to the database
            temp_obj = ActivityPeriod(user=obj,session_date=curr.date(),start_time=start_time,end_time=end_time)
            temp_obj.save()
            self.stdout.write(self.style.SUCCESS('Random User Activity Logged ! "%s" !' % (temp_obj)))
            
            