from django.db import models
from django.conf import settings

import uuid


class Topic(models.Model):

    class Meta:
        db_table = "topic"

    id          = models.UUIDField( default=uuid.uuid4, primary_key=True, editable=False )
    comment     = models.CharField(verbose_name="コメント",max_length=2000)
    user        = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="投稿者",on_delete=models.CASCADE)


    def __str__(self):
        return self.comment
