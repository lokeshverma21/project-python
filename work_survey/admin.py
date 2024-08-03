from django.contrib import admin
# Register your models here.
from .models import Question,Choice


#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text"]

    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)


