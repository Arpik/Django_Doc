import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

class QuestionModelTests(TestCase):
    
    def test_was_published_recently_with_old_question(self):
        """ 
            was_published_recently() returns False for questions whose pub_date
            is older than 1 day
        """
        time = timezone.now() - detetime.timedelta(days = 1, seconds = 1)
        old_question = Question(pub_date = time)
        self.assertIs(old_question.was_published_recently(), False)
