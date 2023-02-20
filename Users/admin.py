from django.contrib import admin
from .models import Questions, Answer, Section, Profile


class adminGrade(admin.ModelAdmin):
    fields = ('user', 'test1', 'test2', 'test3')
    
    
class adminQuestion(admin.ModelAdmin):
    fields = ['question_field', 'section']
    
    
# admin.site.register(Grade,adminGrade)
admin.site.register(Questions, adminQuestion)
admin.site.register(Answer)
admin.site.register(Section)
admin.site.register(Profile)

