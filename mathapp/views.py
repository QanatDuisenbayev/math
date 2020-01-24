# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from mathapp.models import Elementary_math, UserAccount, Category, Beginner_math, UserAll, Exam
from mathapp.forms import RegistrationForm, LoginForm, VideoForm
from django.contrib.auth import get_user_model, authenticate, login, logout
from .forms import SignupForm

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage





User = get_user_model()


class MainList(ListView):

	model = Elementary_math
	template_name = 'index.html'

	def get_context_data(self, *args, **kwargs):
		context = super(MainList, self).get_context_data(*args, **kwargs)
		context['articles'] = self.model.objects.all()
		return context


class CategoryListView(ListView):

	model = Category
	template_name = 'category.html'

	def get_context_data(self, *args, **kwargs):
		user = self.kwargs.get('user')
		context = super(CategoryListView, self).get_context_data(*args, **kwargs)
		context['categories'] = self.model.objects.all()
		context['articles'] = Elementary_math.objects.all()
		context['current_user'] = UserAll.objects.get(user=self.request.user)
		return context


class CategoryDetailView(DetailView):

	model = Category
	template_name = "category_detail.html"

	def get_context_data(self, *args, **kwargs):
		context = super(CategoryDetailView, self).get_context_data(*args, **kwargs)
		user = self.kwargs.get('user')
		context['category'] = self.get_object()
		context['articles_from_category'] = self.get_object().elementary_math_set.all()
		context['exam_from_category'] = self.get_object().exam_set.all()
		context['current_user'] = UserAll.objects.get(user=self.request.user)
		return context


class ElementaryDetailView(DetailView):
	model = Elementary_math
	template_name = "elementary-detail.html"
	def get_context_data(self, *args, **kwargs):
		context = super(ElementaryDetailView, self).get_context_data(*args, **kwargs)
		user = self.kwargs.get('user')
		context['articles'] = self.model.objects.all()
		context['article'] = self.get_object()
		context['current_user'] = UserAll.objects.get(user=self.request.user)
		return context


class ExamView(DetailView):

	model = Exam
	template_name = "exam.html"

	def get_context_data(self, *args, **kwargs):
		context = super(ExamView, self).get_context_data(*args, **kwargs)
		user = self.kwargs.get('user')
		context['exams'] = self.model.objects.all()
		context['exam'] = self.get_object()
		context['current_user'] = UserAll.objects.get(user=self.request.user)
		return context


#for beginner
class BeginnerListView(ListView):

	model = Beginner_math
	template_name = 'beginner_math.html'

	def get_context_data(self, *args, **kwargs):
		context = super(BeginnerListView, self).get_context_data(*args, **kwargs)
		context['articles'] = self.model.objects.all()
		return context


class BeginnerDetailView(DetailView):
	
	model = Beginner_math
	template_name = "beginner-detail.html"
	def get_context_data(self, *args, **kwargs):
		context = super(BeginnerDetailView, self).get_context_data(*args, **kwargs)
		user = self.kwargs.get('user')
		context['articles'] = self.model.objects.all()
		context['article'] = self.get_object()
		#context['current_user'] = UserAccount.objects.get(user=self.request.user)
		return context
#end beginner


class UserReactionView(View):

	template_name = 'elementary-detail.html'

	def get(self, request, *args, **kwargs):
		elementary_math_id = self.request.GET.get('elementary_math_id')
		elementary_math = Elementary_math.objects.get(id=elementary_math_id)
		if (request.user not in elementary_math.users_reaction.all()):
			elementary_math.users_reaction.add(request.user)
			elementary_math.save()



class LoginView(View):

	template_name = 'login.html'

	def get(self, request, *args, **kwargs):

		form = LoginForm(request.POST or None)
		context = {
			'form': form
		}
		return render(self.request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		form = LoginForm(request.POST or None)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user:
				login(self.request, user)
				return HttpResponseRedirect('/')
		context = {
			'form': form
		}
		return render(self.request, self.template_name, context)

class UserAccountView(DetailView):

	template_name = 'user_account.html'

	def get(self, request, *args, **kwargs):
		user = self.kwargs.get('user')
		current_user = UserAll.objects.get(user=User.objects.get(username=user))
		context = {
			'current_user' : current_user
		}
		return render(self.request, self.template_name, context)


class BuyView(ListView):

	model = Elementary_math
	template_name = 'buy.html'

	def get_context_data(self, *args, **kwargs):
		user = self.kwargs.get('user')
		context = super(BuyView, self).get_context_data(*args, **kwargs)
		context['current_user'] = UserAll.objects.get(user=self.request.user)
		return context


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('<div class="container">Тіркеуді аяқтау үшін электрондық поштамен растаңыз</div>')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
    	user.is_active = True
    	user.save()
    	login(request, user)
    	UserAll.objects.create(user=User.objects.get(username=user.username))
    	return redirect('base_view')
    else:
        return HttpResponse('Іске қосу сілтемесі жарамсыз!')


