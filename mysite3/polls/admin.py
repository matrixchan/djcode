from django.contrib import admin

# Register your models here.
from polls.models import Poll,Choice

#admin.site.register(Poll)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    #fields = ['pub_date','question']
    fieldsets = [
        (None,              {'fields':['question']}),
        ('Date information',{'fields':['pub_date'],'classes':['collapse']}),
    ]

    list_display = ('question','pub_date','was_published_recently' )
    list_filter = ['pub_date']
    search_fields = ['question']
    inlines = [ChoiceInline]

   # list_dispaly = ('question','pub_date','was_published_recently' )
admin.site.register(Poll,PollAdmin)
