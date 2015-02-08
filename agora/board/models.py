from django.db import models

# Create your models here.
class Post(models.Model):
	tag = models.CharField(max_length=20)
	text = models.CharField(max_length=300)
	time = models.DateField(null=True)
	score = models.SmallIntegerField(null=True)
	comments = models.ForeignKey('Post', null=True)

class User(models.Model):
	name = models.CharField(max_length=25)
	birthday = models.DateField(null=True)
	score = models.SmallIntegerField(null=True)
	email = models.CharField(max_length=30)
	password = models.CharField(max_length=20, null=True)
	Posts = models.ForeignKey('Post', null=True)