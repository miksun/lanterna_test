from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from e_learning.models import Course, UserCourse, CourseForm
from django.template import RequestContext

@login_required
def index(request):
	course_list = UserCourse.objects.all()
	form = CourseForm();
	csrfContext = RequestContext(request)
	return render_to_response('courseList.html', {"userCourses": course_list,
		"form": form},csrfContext)


@login_required
def save(request):
	form = CourseForm(request.POST)
	if(form.is_valid()):
		course = Course(name=form.cleaned_data["name"], description=form.cleaned_data["description"])
		course.save();
		uc = UserCourse(user=request.user, course=course)
		uc.save();
	return HttpResponseRedirect("/")

