from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_user_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        user = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=team.name)
        self.assertEqual(user.name, 'Iron Man')
        self.assertEqual(user.team, 'Marvel')

    def test_activity_creation(self):
        activity = Activity.objects.create(user='Iron Man', type='Running', duration=30, date='2025-11-01')
        self.assertEqual(activity.type, 'Running')

    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(team='Marvel', points=100)
        self.assertEqual(lb.points, 100)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Morning Cardio', description='Cardio for all levels', difficulty='Easy')
        self.assertEqual(workout.difficulty, 'Easy')
