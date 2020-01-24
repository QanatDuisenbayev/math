# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.conf.urls import url
from django.conf import settings


def generic_filename(instance, filename):
	filename = instance.slug + '.jpg'
	return "{0}/{1}".format(instance, filename)



class Category(models.Model):

	name = models.CharField(max_length=50)
	slug = models.SlugField()
	text = models.TextField(null=True)
	image = models.ImageField(upload_to=generic_filename, blank=True, null=True)

	def __str__(self):
		return self.name


	def get_absolute_url(self):
		return reverse('category-detail', kwargs={'slug': self.slug})



class Elementary_math(models.Model):

	category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True)
	title  	 = models.CharField(max_length=120)
	slug 	 = models.SlugField()
	image 	 = models.ImageField(upload_to=generic_filename, blank=True, null=True)
	content  = models.TextField()
	likes 	 = models.PositiveIntegerField(default=0)
	video	 = models.FileField(upload_to='user_videos/',null=True)


	#  QUESTIONS 
	question1 = models.TextField(blank=True, null=True)
	answer1   = models.IntegerField(blank=True, null=True)
	block1    = models.TextField(blank=True, null=True)
	question2 = models.TextField(blank=True, null=True)
	answer2   = models.IntegerField(blank=True, null=True)
	block2    = models.TextField(blank=True, null=True)
	question3 = models.TextField(blank=True, null=True)
	answer3   = models.IntegerField(blank=True, null=True)
	block3    = models.TextField(blank=True, null=True)
	question4 = models.TextField(blank=True, null=True)
	answer4   = models.IntegerField(blank=True, null=True)
	block4    = models.TextField(blank=True, null=True)
	question5 = models.TextField(blank=True, null=True)
	answer5   = models.IntegerField(blank=True, null=True)
	block5    = models.TextField(blank=True, null=True)
	# users_reaction for show in template pass the test
	users_reaction = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='users_reaction', blank=True, null=True)
	
	def __str__(self):

		return self.title

	def get_absolute_url(self):
		return reverse('elementary-detail', kwargs={'slug': self.slug})


class Beginner_math(models.Model):

	title 	= models.CharField(max_length=120)
	slug 	= models.SlugField()
	image 	= models.ImageField(upload_to=generic_filename, blank=True, null=True)
	content = models.TextField()
	video = models.TextField(null=True)

	#  QUESTIONS 
	question1 = models.TextField(blank=True, null=True)
	answer1   = models.IntegerField(blank=True, null=True)
	block1    = models.TextField(blank=True, null=True)
	question2 = models.TextField(blank=True, null=True)
	answer2   = models.IntegerField(blank=True, null=True)
	block2    = models.TextField(blank=True, null=True)
	question3 = models.TextField(blank=True, null=True)
	answer3   = models.IntegerField(blank=True, null=True)
	block3    = models.TextField(blank=True, null=True)
	question4 = models.TextField(blank=True, null=True)
	answer4   = models.IntegerField(blank=True, null=True)
	block4    = models.TextField(blank=True, null=True)
	question5 = models.TextField(blank=True, null=True)
	answer5   = models.IntegerField(blank=True, null=True)
	block5    = models.TextField(blank=True, null=True)
	
	def __str__(self):

		return self.title

	def get_absolute_url(self):
		return reverse('beginner-detail', kwargs={'slug': self.slug})

#User wich online now
class UserAccount(models.Model):

	user        = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='logged_in_user', null=True ,on_delete=models.CASCADE)
	session_key = models.CharField(max_length=32, null=True, blank=True)

	def __str__(self):
		return self.user.username


class UserAll(models.Model):

	user        = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
	active      = models.BooleanField(default=False)
	exam1       = models.IntegerField(default=0)
	exam2  	    = models.IntegerField(default=0)
	exam3  	    = models.IntegerField(default=0)
	exam4  	    = models.IntegerField(default=0)
	exam5       = models.IntegerField(default=0)
	exam6  	    = models.IntegerField(default=0)
	exam7  	    = models.IntegerField(default=0)
	exam8  	    = models.IntegerField(default=0)
	exam9  	    = models.IntegerField(default=0)
	exam10 	    = models.IntegerField(default=0)
	exam11 	    = models.IntegerField(default=0)

	def __str__(self):
		return self.user.username

	def get_absolute_url(self):
		return reverse('account_view', kwargs={'user': user.username})



class Exam(models.Model):

	category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True)
	title 	= models.CharField(max_length=120, null=True)
	slug = models.SlugField()
	#1
	question_1 = models.CharField(max_length = 500)
	option1_1 = models.CharField(max_length = 20)
	option2_1 = models.CharField(max_length = 20)
	option3_1 = models.CharField(max_length = 20)
	option4_1 = models.CharField(max_length = 20)
	answer_1 = models.CharField(max_length = 20)
	#2
	question_2 = models.CharField(max_length = 500)
	option1_2 = models.CharField(max_length = 20)
	option2_2 = models.CharField(max_length = 20)
	option3_2 = models.CharField(max_length = 20)
	option4_2 = models.CharField(max_length = 20)
	answer_2 = models.CharField(max_length = 20)
	#3
	question_3 = models.CharField(max_length = 500)
	option1_3 = models.CharField(max_length = 20)
	option2_3 = models.CharField(max_length = 20)
	option3_3 = models.CharField(max_length = 20)
	option4_3 = models.CharField(max_length = 20)
	answer_3 = models.CharField(max_length = 20)
	#4
	question_4 = models.CharField(max_length = 500)
	option1_4 = models.CharField(max_length = 20)
	option2_4 = models.CharField(max_length = 20)
	option3_4 = models.CharField(max_length = 20)
	option4_4 = models.CharField(max_length = 20)
	answer_4 = models.CharField(max_length = 20)
	#5
	question_5 = models.CharField(max_length = 500)
	option1_5 = models.CharField(max_length = 20)
	option2_5 = models.CharField(max_length = 20)
	option3_5 = models.CharField(max_length = 20)
	option4_5 = models.CharField(max_length = 20)
	answer_5 = models.CharField(max_length = 20)
	#6
	question_6 = models.CharField(max_length = 500)
	option1_6 = models.CharField(max_length = 20)
	option2_6 = models.CharField(max_length = 20)
	option3_6 = models.CharField(max_length = 20)
	option4_6 = models.CharField(max_length = 20)
	answer_6 = models.CharField(max_length = 20)
	#7
	question_7 = models.CharField(max_length = 500)
	option1_7 = models.CharField(max_length = 20)
	option2_7 = models.CharField(max_length = 20)
	option3_7 = models.CharField(max_length = 20)
	option4_7 = models.CharField(max_length = 20)
	answer_7 = models.CharField(max_length = 20)
	#8
	question_8 = models.CharField(max_length = 500)
	option1_8 = models.CharField(max_length = 20)
	option2_8 = models.CharField(max_length = 20)
	option3_8 = models.CharField(max_length = 20)
	option4_8 = models.CharField(max_length = 20)
	answer_8 = models.CharField(max_length = 20)
	#9
	question_9 = models.CharField(max_length = 500)
	option1_9 = models.CharField(max_length = 20)
	option2_9 = models.CharField(max_length = 20)
	option3_9 = models.CharField(max_length = 20)
	option4_9 = models.CharField(max_length = 20)
	answer_9 = models.CharField(max_length = 20)
	#10
	question_10 = models.CharField(max_length = 500)
	option1_10 = models.CharField(max_length = 20)
	option2_10 = models.CharField(max_length = 20)
	option3_10 = models.CharField(max_length = 20)
	option4_10 = models.CharField(max_length = 20)
	answer_10 = models.CharField(max_length = 20)
	#11
	question_11 = models.CharField(max_length = 500)
	option1_11 = models.CharField(max_length = 20)
	option2_11 = models.CharField(max_length = 20)
	option3_11 = models.CharField(max_length = 20)
	option4_11 = models.CharField(max_length = 20)
	answer_11 = models.CharField(max_length = 20)
	#12
	question_12 = models.CharField(max_length = 500)
	option1_12 = models.CharField(max_length = 20)
	option2_12 = models.CharField(max_length = 20)
	option3_12 = models.CharField(max_length = 20)
	option4_12 = models.CharField(max_length = 20)
	answer_12 = models.CharField(max_length = 20)
	#13
	question_13 = models.CharField(max_length = 500)
	option1_13 = models.CharField(max_length = 20)
	option2_13= models.CharField(max_length = 20)
	option3_13 = models.CharField(max_length = 20)
	option4_13 = models.CharField(max_length = 20)
	answer_13 = models.CharField(max_length = 20)
	#14
	question_14 = models.CharField(max_length = 500)
	option1_14 = models.CharField(max_length = 20)
	option2_14 = models.CharField(max_length = 20)
	option3_14 = models.CharField(max_length = 20)
	option4_14 = models.CharField(max_length = 20)
	answer_14 = models.CharField(max_length = 20)
	#15
	question_15 = models.CharField(max_length = 500)
	option1_15 = models.CharField(max_length = 20)
	option2_15 = models.CharField(max_length = 20)
	option3_15 = models.CharField(max_length = 20)
	option4_15 = models.CharField(max_length = 20)
	answer_15 = models.CharField(max_length = 20)
	#16
	question_16 = models.CharField(max_length = 500)
	option1_16 = models.CharField(max_length = 20)
	option2_16 = models.CharField(max_length = 20)
	option3_16 = models.CharField(max_length = 20)
	option4_16 = models.CharField(max_length = 20)
	answer_16 = models.CharField(max_length = 20)
	#17
	question_17 = models.CharField(max_length = 500)
	option1_17 = models.CharField(max_length = 20)
	option2_17 = models.CharField(max_length = 20)
	option3_17 = models.CharField(max_length = 20)
	option4_17 = models.CharField(max_length = 20)
	answer_17 = models.CharField(max_length = 20)
	#18
	question_18 = models.CharField(max_length = 500)
	option1_18 = models.CharField(max_length = 20)
	option2_18 = models.CharField(max_length = 20)
	option3_18 = models.CharField(max_length = 20)
	option4_18 = models.CharField(max_length = 20)
	answer_18 = models.CharField(max_length = 20)
	#19
	question_19 = models.CharField(max_length = 500)
	option1_19 = models.CharField(max_length = 20)
	option2_19 = models.CharField(max_length = 20)
	option3_19 = models.CharField(max_length = 20)
	option4_19 = models.CharField(max_length = 20)
	answer_19 = models.CharField(max_length = 20)
	#20
	question_20 = models.CharField(max_length = 500)
	option1_20 = models.CharField(max_length = 20)
	option2_20 = models.CharField(max_length = 20)
	option3_20 = models.CharField(max_length = 20)
	option4_20 = models.CharField(max_length = 20)
	answer_20 = models.CharField(max_length = 20)


	def __str__(self):

		return self.title

	def get_absolute_url(self):
		return reverse('exam', kwargs={'slug': self.slug})