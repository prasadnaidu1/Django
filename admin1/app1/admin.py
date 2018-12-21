from django.contrib import admin

# Register your models here.
from.models import Course
from.models import Faculity
from.models import NewCourse




admin.site.register(Course)
admin.site.register(Faculity)
admin.site.register(NewCourse)