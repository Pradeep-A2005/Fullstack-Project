from django.contrib import admin

from django.contrib import admin
from .models import Student,AdminMark,TeamFeedbackMark,ReviewerMark

admin.site.register(Student)
admin.site.register(AdminMark)
admin.site.register(TeamFeedbackMark)
admin.site.register(ReviewerMark)






