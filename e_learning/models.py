from django.db import models
from django import forms
from django.contrib.auth.models import User

class Course(models.Model):
	id=models.AutoField(primary_key=True)
	name = models.CharField(max_length=25)
	description = models.CharField(max_length=125)
	def __unicode__(self):
		return self.name


class UserCourse(models.Model):
	user = models.ForeignKey(User)
	course = models.ForeignKey(Course)
	def __unicode__(self):
		return self.user.username +" | "+ self.course.name

class CourseForm(forms.Form):
	name = forms.CharField(max_length=25)
	description = forms.CharField(max_length=125)
	def __unicode__(self):
		return self.name