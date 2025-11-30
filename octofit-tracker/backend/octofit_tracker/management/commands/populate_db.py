from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel.name)
        captain = User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel.name)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc.name)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc.name)

        # Activities
        Activity.objects.create(user=ironman.name, type='Running', duration=30, date='2025-11-01')
        Activity.objects.create(user=batman.name, type='Cycling', duration=45, date='2025-11-02')
        Activity.objects.create(user=superman.name, type='Swimming', duration=60, date='2025-11-03')
        Activity.objects.create(user=captain.name, type='Yoga', duration=20, date='2025-11-04')

        # Leaderboard
        Leaderboard.objects.create(team=marvel.name, points=100)
        Leaderboard.objects.create(team=dc.name, points=90)

        # Workouts
        Workout.objects.create(name='Morning Cardio', description='Cardio for all levels', difficulty='Easy')
        Workout.objects.create(name='Strength Training', description='Build muscle strength', difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
