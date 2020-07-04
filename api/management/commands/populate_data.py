import json
from django.core.management.base import BaseCommand
from api.models import User, ActivityPeriod


class Command(BaseCommand):
    help = 'Create user activity record from JSON'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **options):
        with open(options['path'], 'r') as f:
            data = json.load(f)
        print(data)
        for d in data['members']:
            print(d)
            user_data = User(user_id=d['id'],real_name=d['real_name'],tz=d['tz'])
            user_data.save()
            for ap in d['activity_periods']:
                ap_data = ActivityPeriod(user=user_data, start_time=ap['start_time'], end_time=ap['end_time'])
                ap_data.save()
        self.stdout.write(self.style.SUCCESS('Successfully created plans'))