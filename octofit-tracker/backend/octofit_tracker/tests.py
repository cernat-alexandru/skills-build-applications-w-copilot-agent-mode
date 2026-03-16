from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(name='Test', email='test@example.com', team='marvel')
        self.assertEqual(user.name, 'Test')

class TeamModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='marvel', members=['Iron Man'])
        self.assertEqual(team.name, 'marvel')

class ActivityModelTest(TestCase):
    def test_activity_creation(self):
        activity = Activity.objects.create(user='Test', activity='Running', duration=30)
        self.assertEqual(activity.activity, 'Running')

class LeaderboardModelTest(TestCase):
    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(team='marvel', points=100)
        self.assertEqual(leaderboard.team, 'marvel')

class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(user='Test', workout='Cardio', suggestion='Run')
        self.assertEqual(workout.workout, 'Cardio')
