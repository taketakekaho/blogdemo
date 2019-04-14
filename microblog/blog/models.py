from django.db import models

class Blog(models.Model):
    #投稿
    content = models.CharField(max_length=140)
    #投稿日時:自動的に作成時点の日時を保存
    posted_date = models.DateTimeField(auto_now_add=True)
