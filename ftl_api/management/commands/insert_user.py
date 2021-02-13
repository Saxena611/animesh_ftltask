from django.core.management.base import BaseCommand
from django.utils import timezone
from django.utils.crypto import get_random_string
from ftl_api.models import User

class Command(BaseCommand):
    help = 'Inserts User into the model'

    def add_arguments(self, parser):
        parser.add_argument('total',type=int,help='Number of user to be created')
    
    def handle(self, *args, **kwargs):
        total = kwargs['total']
        
        for i in range(total):
            user_id = get_random_string()
            obj = User(id=user_id,real_name = get_random_string(),tz=get_random_string())
            obj.save()
            self.stdout.write(self.style.SUCCESS('User "%s" added !' % (user_id)))
            