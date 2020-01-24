# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from mathapp.models import Elementary_math, Category, UserAccount, Beginner_math, UserAll, Exam



class ArticleAdmin(admin.ModelAdmin):

	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category)
admin.site.register(Beginner_math)
admin.site.register(Elementary_math, ArticleAdmin)
admin.site.register(UserAccount)
admin.site.register(UserAll)
admin.site.register(Exam)
