import pytest 

pytestmark = pytest.amrk.django_db

from ..models import Goal

def test____str__():
    # Use Faker to create dummy user data. Then create test using that user.
    # randy = User.objects.get(username='randomUser')
    # goal = Goal.objects.create(user=randy, title = 'Coffee', description='Have 1 per day!', goaltype=Goal.Goaltype.ABSTAIN_LIMIT)

    pass