from django.db import models
from django import forms
from django.contrib.auth.models import User,UserManager

class Course(models.Model):
	"""
	A saved course has a NAME
	create a course
	>>> course = Course.objects.create(name="testCourse", description="a description")

	The name should now be set.
	>>> course.name
	'testCourse'
	"""
	id=models.AutoField(primary_key=True)
	name = models.CharField(max_length=25)
	description = models.CharField(max_length=125)
	def __unicode__(self):
		return self.name


class UserCourse(models.Model):
	"""
	>>> user = User.objects.create_user('testUser','ms@cleancode.se', 'topsecret')	
	>>> userTwo = User.objects.create_user('testUser2','ms@cleancode.se', 'topsecret2')
	>>> course = Course.objects.create(name="testCourse", description="a description")
	>>> UserCourse.objects.count()
	0
	>>> userCourse = UserCourse.objects.create(user=user,course=course)

	The user asigned to the course should now have a course.
	>>> UserCourse.objects.filter(user=user).count()
	1

	But the other user shouldnt
	>>> UserCourse.objects.filter(user=userTwo).count()
	0
	"""
	user = models.ForeignKey(User)
	course = models.ForeignKey(Course)
	def __unicode__(self):
		return self.user.username +" | "+ self.course.name

class CourseForm(forms.Form):
	name = forms.CharField(max_length=25)
	description = forms.CharField(max_length=125)
	def __unicode__(self):
		return self.name