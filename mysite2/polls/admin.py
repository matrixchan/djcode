from django.contrib import admin

# Register your models here.
from polls.models import Choice,Question

#admin.site.register(Question)

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3



class QuestionAdmin(admin.ModelAdmin):
   # fields = ['pub_date','question_text']
   fieldsets = [
    (None,                  {'fields':['question_text']}),
       ('Date information',    {'fields':['pub_date'], 'classes':['collapse']})
   ]
   inlines = [ChoiceInline]

admin.site.register(Question,QuestionAdmin)

