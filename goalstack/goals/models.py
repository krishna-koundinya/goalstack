from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel
# Create your models here.

class Goal(TimeStampedModel):
    class Goaltype(models.TextChoices):
        UNSPECIFIED = "unspecified", "Unspecified"
        TIME_BOUND = "time-bound", "Time-Bound"
        COUNT_BOUND = "count-bound", "Count-Bound"
        ABSTAIN_LIMIT = "abstain-or-limit", "Abstain-Or-Limit"
        
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    title = models.CharField("Goal", max_length=255)
    description = models.TextField("Description", blank=True)
    goaltype = models.CharField("Type", max_length=20, choices=Goaltype.choices, default=Goaltype.UNSPECIFIED)

    def __str__(self):
        return self.title




