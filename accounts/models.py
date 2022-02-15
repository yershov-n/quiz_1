from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True)
    avatar = models.ImageField(upload_to='profile/', default='default.png')
    birthday = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    rating = models.PositiveSmallIntegerField(default=0)

    class Meta(AbstractUser.Meta):
        pass

    def __str__(self):
        return self.username

    def update_rating(self, num_correct_answers, num_incorrect_answers):
        point = num_correct_answers - num_incorrect_answers

        if self.rating + point < 0:
            self.rating = 0
        else:
            self.rating = self.rating + point

        self.save()
